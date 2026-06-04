# MaxCompute 连接配置与排错参考

## 1. Endpoint 完整列表

### 北京区域（cn-beijing）

| 网络类型 | Endpoint | DNS 可解析 | 说明 |
|---------|----------|-----------|------|
| 公网 | `http://service.cn-beijing.maxcompute.aliyun.com/api` | ✅ | **推荐**，任何网络环境可用 |
| 经典网络 | `http://service.odps.aliyun.com/api` | ✅ | 旧版公网地址，兼容用 |
| 阿里内网 | `http://service.cn-beijing.maxcompute.aliyun-inc.com/api` | ✅（仅内网） | 阿里云办公网 |
| VPC 内网 | `http://service.cn-beijing-vpc.maxcompute.aliyun-inc.com/api` | ✅（仅 VPC） | ECS/VPC 环境 |

### DNS 验证方法

```bash
# Linux / macOS
nslookup service.cn-beijing.maxcompute.aliyun.com
dig service.cn-beijing.maxcompute.aliyun.com

# Windows
nslookup service.cn-beijing.maxcompute.aliyun.com
```

预期返回公网 IP（如 39.107.x.x / 8.145.x.x）。如果返回 "Non-existent domain"，说明域名有误或网络受限。

### 常见错误

| 域名 | 问题 |
|------|------|
| `service.cn-beijing.maxcompute.aliyuncs.com` | ❌ 域名不存在，DNS 解析失败 |
| `service.cn-beijing.maxcompute.aliyun.com` | ✅ 正确公网域名 |

> **记忆要点**：MaxCompute 公网域名后缀是 `aliyun.com`，不是 `aliyuncs.com`（后者是 OSS 等其他产品的域名格式）。

## 2. 账号与权限

### 当前配置（数据智能部子账户）

| 配置项 | 值 |
|--------|---|
| 子账户 | shujuzhinengbu@1266397640687477.onaliyun.com |
| 所属部门 | 数据智能部 |
| 默认 Project | soyoung_dw |

### 权限矩阵

| 操作 | 权限状态 | 说明 |
|------|---------|------|
| SELECT（SQL 查询） | ✅ 已授权 | 通过 `execute_sql().open_reader()` 读取 |
| Download（Tunnel 下载） | ❌ 未授权 | `table.open_reader()` 会报 4019 错误 |
| CREATE TABLE | 需确认 | 建表权限需联系管理员 |
| INSERT / WRITE | 需确认 | 写数据权限需联系管理员 |

### 权限不足的解决方案

**4019 NoPermission 错误**（Download 权限不足）：
```python
# ❌ 会报错
with table.open_reader() as reader:
    for record in reader:
        ...

# ✅ 改用 SQL 查询
sql = "SELECT * FROM table_name WHERE dp = '2026-06-03' LIMIT 10"
with o.execute_sql(sql).open_reader() as reader:
    for record in reader:
        ...
```

**申请权限**：联系 MaxCompute 项目管理员，授予 `odps:Download` 权限：
```sql
-- 管理员执行
GRANT Download ON TABLE dim_product_info TO USER RAM$xxx;
```

## 3. PyODPS 常用操作速查

### 连接

```python
from odps import ODPS

o = ODPS(access_id, secret_key, project='soyoung_dw',
         endpoint='http://service.cn-beijing.maxcompute.aliyun.com/api')
```

### 表操作

```python
# 获取表对象
t = o.get_table('dim_product_info')

# 查看表是否存在
o.exist_table('dim_product_info')  # True / False

# 列出项目下所有表
for t in o.list_tables():
    print(t.name)

# 按前缀筛选
for t in o.list_tables(prefix='dim_'):
    print(t.name)
```

### 分区操作

```python
t = o.get_table('dim_product_info')

# 列出所有分区
for p in t.partitions:
    print(p.name)  # 如 dp='2026-06-03'

# 最新分区
latest = list(t.partitions)[-1]
print(latest.name)

# SQL 中引用最新分区
sql = "SELECT * FROM dim_product_info WHERE dp = MAX_PT('soyoung_dw.dim_product_info') LIMIT 1"
```

### 查询执行

```python
# 基本查询
sql = "SELECT product_id, title FROM dim_product_info WHERE dp = '2026-06-03' LIMIT 10"
with o.execute_sql(sql).open_reader() as reader:
    for record in reader:
        print(record['product_id'], record['title'])

# 获取列名
with o.execute_sql(sql).open_reader() as reader:
    columns = [col.name for col in reader._schema.columns]
    print(columns)

# 结果转 pandas DataFrame
import pandas as pd
with o.execute_sql(sql).open_reader() as reader:
    df = reader.to_pandas()
```

### MAX_PT 函数

`MAX_PT` 是 MaxCompute 内置函数，返回指定表的最新分区值：
```sql
-- 用法
SELECT * FROM table_name WHERE dp = MAX_PT('project.table_name')

-- 注意：参数需要带 project 名
-- MAX_PT('soyoung_dw.dim_product_info')  →  '2026-06-03'
```

## 4. 网络连通性排查

```bash
# 1. DNS 解析
nslookup service.cn-beijing.maxcompute.aliyun.com

# 2. HTTP 连通性（不是 ping，MaxCompute 不响应 ICMP）
curl -v http://service.cn-beijing.maxcompute.aliyun.com/api

# 3. Python 快速测试
python -c "
from odps import ODPS
o = ODPS('id', 'key', project='soyoung_dw',
         endpoint='http://service.cn-beijing.maxcompute.aliyun.com/api')
print(o.exist_table('dim_product_info'))
"
```

## 5. 数据量与性能建议

| 场景 | 建议 |
|------|------|
| 全表扫描 | 分区表必须带分区条件，避免超时 |
| 大结果集 | 用 `LIMIT` 或写入临时表，避免内存溢出 |
| 多次查询 | 复用 ODPS 客户端实例，避免重复建连 |
| 复杂分析 | 优先用 SQL 聚合，避免拉取明细到本地计算 |
