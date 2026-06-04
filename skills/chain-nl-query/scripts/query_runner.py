#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""可选的只读取数执行器（ODPS / MaxCompute）。

本 Skill 的核心产物是 SQL；执行是可选的、依赖部署环境。
这个脚本是一个**自包含、只读**的执行器，便于「部署到别的地方」后立即可用：
  - 凭据从环境变量或同目录/上层目录的 .env.odps 读取
  - 只允许 SELECT / WITH 查询，拒绝任何写/删/改/DDL
  - 依赖 pyodps（`pip install pyodps`）；未安装时给出友好提示而不报错退出

用法：
  python3 query_runner.py "SELECT 1 AS x"
  python3 query_runner.py --file my.sql
  echo "SELECT ..." | python3 query_runner.py -
  python3 query_runner.py "SELECT ..." --csv out.csv

环境变量（或 .env.odps，每行 KEY=VALUE）：
  ODPS_ACCESS_ID, ODPS_SECRET_ACCESS_KEY, ODPS_PROJECT_NAME, ODPS_ENDPOINT

若部署到非 ODPS 引擎（Hive/Spark/Presto/StarRocks 等），把 run_query() 换成
对应客户端即可；只读校验 is_read_only() 可原样复用。
"""
from __future__ import annotations
import argparse
import os
import re
import sys
from pathlib import Path

WRITE_KEYWORDS = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|MERGE|REPLACE|"
    r"GRANT|REVOKE|SET|USE|MSCK|LOAD|UNLOAD|ADD\s+JAR|CALL)\b",
    re.IGNORECASE,
)


def strip_sql_comments(sql: str) -> str:
    sql = re.sub(r"--[^\n]*", " ", sql)            # line comments
    sql = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)  # block comments
    return sql.strip()


def is_read_only(sql: str) -> tuple[bool, str]:
    body = strip_sql_comments(sql)
    if not body:
        return False, "空 SQL。"
    # collapse trailing semicolons; reject multiple statements
    stmts = [s for s in body.split(";") if s.strip()]
    if len(stmts) > 1:
        return False, "只允许单条查询语句（检测到多条以 ; 分隔的语句）。"
    head = stmts[0].lstrip().split(None, 1)[0].upper()
    if head not in ("SELECT", "WITH"):
        return False, f"只允许 SELECT / WITH 查询，检测到以 {head} 开头。"
    if WRITE_KEYWORDS.search(stmts[0]):
        return False, "检测到写/DDL 关键字，已拒绝。本执行器只读。"
    return True, ""


def load_env(skill_dir: Path) -> None:
    """从 .env.odps 补充环境变量（不覆盖已存在的）。"""
    for cand in (Path.cwd() / ".env.odps", skill_dir / ".env.odps", skill_dir.parent / ".env.odps"):
        if cand.is_file():
            for line in cand.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
            return


def get_odps():
    try:
        from odps import ODPS  # type: ignore
    except ImportError:
        sys.exit(
            "未安装 pyodps。执行取数需要：pip install pyodps\n"
            "（若只需要生成 SQL，可忽略本脚本，直接把 SQL 拿到你的数仓客户端运行。）"
        )
    missing = [k for k in ("ODPS_ACCESS_ID", "ODPS_SECRET_ACCESS_KEY",
                           "ODPS_PROJECT_NAME", "ODPS_ENDPOINT") if not os.environ.get(k)]
    if missing:
        sys.exit("缺少环境变量：" + ", ".join(missing) +
                 "\n请设置环境变量或在 .env.odps 中提供。")
    return ODPS(
        os.environ["ODPS_ACCESS_ID"],
        os.environ["ODPS_SECRET_ACCESS_KEY"],
        project=os.environ["ODPS_PROJECT_NAME"],
        endpoint=os.environ["ODPS_ENDPOINT"],
    )


def run_query(sql: str, limit_rows: int):
    o = get_odps()
    rows = []
    with o.execute_sql(sql).open_reader() as reader:
        cols = None
        for i, rec in enumerate(reader):
            if i >= limit_rows:
                break
            d = dict(zip(rec._name_indexes.keys(), rec.values)) if hasattr(rec, "_name_indexes") \
                else {c: rec[c] for c in (cols or [])}
            rows.append(d)
    return rows


def print_table(rows):
    if not rows:
        print("(0 行)")
        return
    cols = list(rows[0].keys())
    widths = {c: max(len(str(c)), *(len(str(r.get(c, ""))) for r in rows)) for c in cols}
    line = " | ".join(str(c).ljust(widths[c]) for c in cols)
    print(line)
    print("-+-".join("-" * widths[c] for c in cols))
    for r in rows:
        print(" | ".join(str(r.get(c, "")).ljust(widths[c]) for c in cols))
    print(f"\n({len(rows)} 行)")


def main():
    ap = argparse.ArgumentParser(description="只读取数执行器（ODPS）")
    ap.add_argument("sql", nargs="?", help="SQL 字符串；'-' 表示从 stdin 读取")
    ap.add_argument("--file", help="从文件读取 SQL")
    ap.add_argument("--limit", type=int, default=200, help="最多返回行数（默认 200）")
    ap.add_argument("--csv", help="把结果写到 CSV 文件")
    ap.add_argument("--check-only", action="store_true", help="只做只读校验，不执行")
    args = ap.parse_args()

    if args.file:
        sql = Path(args.file).read_text(encoding="utf-8")
    elif args.sql == "-" or (not args.sql and not sys.stdin.isatty()):
        sql = sys.stdin.read()
    elif args.sql:
        sql = args.sql
    else:
        ap.error("请提供 SQL（位置参数 / --file / stdin）。")

    ok, msg = is_read_only(sql)
    if not ok:
        sys.exit(f"拒绝执行：{msg}")
    if args.check_only:
        print("只读校验通过。")
        return

    load_env(Path(__file__).resolve().parent)
    rows = run_query(sql, args.limit)

    if args.csv:
        import csv
        with open(args.csv, "w", newline="", encoding="utf-8-sig") as f:
            if rows:
                wcsv = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                wcsv.writeheader()
                wcsv.writerows(rows)
        print(f"已写出 {len(rows)} 行到 {args.csv}")
    else:
        print_table(rows)


if __name__ == "__main__":
    main()
