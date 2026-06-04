#!/usr/bin/env python3
"""
mc_query.py — MaxCompute (ODPS) 查询工具

用法:
  python mc_query.py schema <table_name> [--output file.txt]
  python mc_query.py sql "<SELECT 语句>" [--csv result.csv] [--limit N]
  python mc_query.py partitions <table_name> [--latest]

凭据配置（按优先级）:
  1. 环境变量: ODPS_ACCESS_ID, ODPS_SECRET_ACCESS_KEY, ODPS_PROJECT_NAME, ODPS_ENDPOINT
  2. 当前目录或 Skill 根目录下的 .env.odps 文件
"""

import os
import sys
import csv
import re
from pathlib import Path

try:
    from odps import ODPS
except ImportError:
    print("错误: 未安装 pyodps，请运行: pip install pyodps")
    sys.exit(1)


# ─── 凭据加载 ────────────────────────────────────────────────────────────────

def load_env_file(filepath: str) -> dict:
    """从 .env.odps 文件加载键值对"""
    env = {}
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, _, value = line.partition('=')
                    env[key.strip()] = value.strip()
    return env


def get_config() -> dict:
    """获取 MaxCompute 连接配置（环境变量优先 > .env.odps 文件）"""
    # 尝试加载 .env.odps
    env_file = {}
    for path in ['.env.odps', os.path.join(os.path.dirname(__file__), '..', '.env.odps')]:
        env_file.update(load_env_file(path))

    config = {
        'access_id': os.environ.get('ODPS_ACCESS_ID') or env_file.get('ODPS_ACCESS_ID'),
        'secret_key': os.environ.get('ODPS_SECRET_ACCESS_KEY') or env_file.get('ODPS_SECRET_ACCESS_KEY'),
        'project': os.environ.get('ODPS_PROJECT_NAME') or env_file.get('ODPS_PROJECT_NAME') or 'soyoung_dw',
        'endpoint': os.environ.get('ODPS_ENDPOINT') or env_file.get('ODPS_ENDPOINT')
                    or 'http://service.cn-beijing.maxcompute.aliyun.com/api',
    }

    missing = [k for k in ('access_id', 'secret_key') if not config[k]]
    if missing:
        print(f"错误: 缺少凭据配置 {missing}")
        print("请设置环境变量或创建 .env.odps 文件，详见 SKILL.md")
        sys.exit(1)

    return config


# ─── 连接管理 ────────────────────────────────────────────────────────────────

def create_odps_client() -> ODPS:
    """创建并返回 ODPS 客户端实例"""
    config = get_config()
    o = ODPS(config['access_id'], config['secret_key'],
             project=config['project'], endpoint=config['endpoint'])
    return o


# ─── 安全校验 ────────────────────────────────────────────────────────────────

# 允许的操作关键词（只读）
ALLOWED_PREFIXES = ('select', 'with', 'show', 'describe', 'desc', 'explain')
# 禁止的操作关键词
BLOCKED_KEYWORDS = (
    'insert', 'update', 'delete', 'drop', 'create', 'alter',
    'truncate', 'merge', 'load', 'unload', 'grant', 'revoke'
)


def is_read_only(sql: str) -> bool:
    """校验 SQL 是否为只读操作"""
    cleaned = re.sub(r'--.*$', '', sql, flags=re.MULTILINE)  # 去掉注释
    cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)  # 去掉块注释
    cleaned = cleaned.strip().lower()

    if not cleaned:
        return False

    first_word = cleaned.split()[0]
    if first_word not in ALLOWED_PREFIXES:
        return False

    # 二次检查：禁止关键词不能出现在顶层语句中
    for kw in BLOCKED_KEYWORDS:
        pattern = rf'\b{kw}\b'
        if re.search(pattern, cleaned):
            # 排除子查询中的 SELECT ... FROM ... WHERE x IN (SELECT ...)
            # 简单策略：如果禁止词出现在 SELECT 之前，拒绝
            kw_pos = cleaned.find(kw)
            select_pos = cleaned.find('select')
            if kw_pos < select_pos or select_pos == -1:
                return False

    return True


# ─── 表结构查询 ──────────────────────────────────────────────────────────────

def get_table_schema(o: ODPS, table_name: str) -> dict:
    """获取表结构信息，返回结构化字典"""
    t = o.get_table(table_name)

    columns = []
    for col in t.table_schema.columns:
        columns.append({
            'name': col.name,
            'type': str(col.type),
            'comment': col.comment or '',
        })

    partitions = []
    for col in t.table_schema.partitions:
        partitions.append({
            'name': col.name,
            'type': str(col.type),
            'comment': col.comment or '',
        })

    return {
        'project': o.project,
        'table_name': t.name,
        'owner': t.owner,
        'creation_time': str(t.creation_time),
        'last_modified': str(t.last_data_modified_time),
        'comment': t.comment or '',
        'columns': columns,
        'partitions': partitions,
    }


def print_schema(schema: dict, output_file: str = None):
    """打印或导出表结构"""
    lines = []
    lines.append(f"项目: {schema['project']}")
    lines.append(f"表名: {schema['table_name']}")
    lines.append(f"Owner: {schema['owner']}")
    lines.append(f"创建时间: {schema['creation_time']}")
    lines.append(f"最后修改时间: {schema['last_modified']}")
    if schema['comment']:
        lines.append(f"表注释: {schema['comment']}")

    # 普通字段
    cols = schema['columns']
    lines.append("")
    lines.append("=" * 90)
    lines.append(f"普通字段 ({len(cols)} 个)")
    lines.append("=" * 90)
    lines.append(f"{'序号':<5} {'字段名':<35} {'类型':<20} {'注释'}")
    lines.append(f"{'-'*5} {'-'*35} {'-'*20} {'-'*30}")
    for i, col in enumerate(cols, 1):
        lines.append(f"{i:<5} {col['name']:<35} {col['type']:<20} {col['comment']}")

    # 分区字段
    parts = schema['partitions']
    if parts:
        lines.append("")
        lines.append("=" * 90)
        lines.append(f"分区字段 ({len(parts)} 个)")
        lines.append("=" * 90)
        lines.append(f"{'序号':<5} {'字段名':<35} {'类型':<20} {'注释'}")
        lines.append(f"{'-'*5} {'-'*35} {'-'*20} {'-'*30}")
        for i, col in enumerate(parts, 1):
            lines.append(f"{i:<5} {col['name']:<35} {col['type']:<20} {col['comment']}")

    text = "\n".join(lines)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"表结构已保存到: {output_file}")
    else:
        print(text)

    print(f"\n共 {len(cols)} 个普通字段, {len(parts)} 个分区字段")


# ─── SQL 查询 ────────────────────────────────────────────────────────────────

def run_sql_query(o: ODPS, sql: str, limit: int = None) -> dict:
    """执行只读 SQL 查询，返回结构化结果"""
    if not is_read_only(sql):
        raise ValueError(f"安全校验失败：仅允许只读查询（SELECT / WITH），拒绝写操作。\nSQL: {sql[:200]}")

    if limit and 'limit' not in sql.lower():
        sql = f"{sql.rstrip().rstrip(';')} LIMIT {limit}"

    result = {'columns': [], 'rows': [], 'count': 0}

    with o.execute_sql(sql).open_reader() as reader:
        result['columns'] = [col.name for col in reader._schema.columns]
        for record in reader:
            row = {col: record[col] for col in result['columns']}
            result['rows'].append(row)
        result['count'] = len(result['rows'])

    return result


def print_query_result(result: dict, csv_file: str = None):
    """打印或导出查询结果"""
    if csv_file:
        with open(csv_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=result['columns'])
            writer.writeheader()
            for row in result['rows']:
                # 转换复杂类型为字符串
                clean_row = {k: str(v) if not isinstance(v, (int, float, str, type(None))) else v
                             for k, v in row.items()}
                writer.writerow(clean_row)
        print(f"查询结果已保存到: {csv_file}")
        print(f"共 {result['count']} 条记录")
    else:
        print(f"查询返回 {result['count']} 条记录")
        print("=" * 100)
        for row in result['rows']:
            for col_name in result['columns']:
                val = row[col_name]
                print(f"{col_name:<35} : {val}")
            print("=" * 100)


# ─── 分区查询 ────────────────────────────────────────────────────────────────

def get_partitions(o: ODPS, table_name: str, latest_only: bool = False) -> list:
    """获取表的分区列表"""
    t = o.get_table(table_name)
    partitions = list(t.partitions)

    if latest_only and partitions:
        return [partitions[-1]]
    return partitions


# ─── CLI 入口 ────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    command = sys.argv[1].lower()
    o = create_odps_client()

    if command == 'schema':
        if len(sys.argv) < 3:
            print("用法: python mc_query.py schema <table_name> [--output file.txt]")
            sys.exit(1)
        table_name = sys.argv[2]
        output_file = None
        if '--output' in sys.argv:
            idx = sys.argv.index('--output')
            output_file = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None
        schema = get_table_schema(o, table_name)
        print_schema(schema, output_file)

    elif command == 'sql':
        if len(sys.argv) < 3:
            print('用法: python mc_query.py sql "<SELECT 语句>" [--csv result.csv] [--limit N]')
            sys.exit(1)
        sql = sys.argv[2]
        csv_file = None
        limit = None
        if '--csv' in sys.argv:
            idx = sys.argv.index('--csv')
            csv_file = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None
        if '--limit' in sys.argv:
            idx = sys.argv.index('--limit')
            limit = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else None
        result = run_sql_query(o, sql, limit)
        print_query_result(result, csv_file)

    elif command == 'partitions':
        if len(sys.argv) < 3:
            print("用法: python mc_query.py partitions <table_name> [--latest]")
            sys.exit(1)
        table_name = sys.argv[2]
        latest_only = '--latest' in sys.argv
        parts = get_partitions(o, table_name, latest_only)
        print(f"表 {table_name} 共有 {len(list(o.get_table(table_name).partitions))} 个分区")
        for p in parts:
            print(f"  {p.name}")

    else:
        print(f"未知命令: {command}")
        print("支持的命令: schema, sql, partitions")
        sys.exit(1)


if __name__ == '__main__':
    main()
