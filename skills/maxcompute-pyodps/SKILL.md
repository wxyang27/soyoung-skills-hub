---
name: maxcompute-pyodps
description: 通过 PyODPS 连接阿里云 MaxCompute (ODPS)，执行表结构查看、SQL 查询等数据操作。触发词包括：MaxCompute、ODPS、PyODPS、连接数仓、查表结构、执行SQL、取数、dim/dws/dwd/ads/dm表查询。支持环境变量或 .env.odps 配置凭据，内置安全校验（只读 SELECT）。
---

# MaxCompute · PyODPS 连接与查询

## 这个 Skill 做什么

通过 PyODPS SDK 连接阿里云 MaxCompute 数仓，完成：

1. **查看表结构**（字段名、类型、注释、分区信息）
2. **执行只读 SQL 查询**（SELECT / WITH）
3. **获取分区信息**（最新分区、分区列表）
4. **导出数据到文件**（CSV / TXT）

> 核心原则：**凭据从环境变量读取，绝不硬编码；只允许只读查询，拒绝写/删/改/DDL。**

## 何时使用 / 不使用

**使用：**
- 需要连接 MaxCompute 查看表结构、字段信息
- 执行 SQL 查询取数
- 检查表的分区状态
- 批量导出数据到本地文件

**不使用：**
- 写数据、建表、删表、改表结构（用 DataWorks 或 odpscmd）
- 调度任务开发（用 DataWorks 调度）
- 非 MaxCompute 数仓（如 Hive/StarRocks/Doris，需另配客户端）

## 前置准备

### 1. 安装依赖

```bash
pip install pyodps
```

### 2. 配置凭据（二选一）

**方式 A：环境变量（推荐）**

```bash
# Linux / macOS
export ODPS_ACCESS_ID=your_access_id
export ODPS_SECRET_ACCESS_KEY=your_secret
export ODPS_PROJECT_NAME=soyoung_dw
export ODPS_ENDPOINT=http://service.cn-beijing.maxcompute.aliyun.com/api

# Windows PowerShell
$env:ODPS_ACCESS_ID="your_access_id"
$env:ODPS_SECRET_ACCESS_KEY="your_secret"
$env:ODPS_PROJECT_NAME="soyoung_dw"
$env:ODPS_ENDPOINT="http://service.cn-beijing.maxcompute.aliyun.com/api"
```

**方式 B：.env.odps 文件（放在运行目录或 Skill 根目录）**

```ini
ODPS_ACCESS_ID=your_access_id
ODPS_SECRET_ACCESS_KEY=your_secret
ODPS_PROJECT_NAME=soyoung_dw
ODPS_ENDPOINT=http://service.cn-beijing.maxcompute.aliyun.com/api
```

> ⚠ `.env.odps` 文件不要提交到 Git，已在 `.gitignore` 中排除。

### 3. Endpoint 选择

| 网络环境 | Endpoint |
|---------|----------|
| **公网（推荐）** | `http://service.cn-beijing.maxcompute.aliyun.com/api` |
| 阿里内网 | `http://service.cn-beijing.maxcompute.aliyun-inc.com/api` |
| VPC 内网 | `http://service.cn-beijing-vpc.maxcompute.aliyun-inc.com/api` |

> **重要**：公网 endpoint 域名是 `aliyun.com`（不是 `aliyuncs.com`），DNS 解析验证通过。如果 `aliyun.com` 不通，可尝试经典网络 `http://service.odps.aliyun.com/api`。

## 使用流程

### 场景 1：查看表结构

```bash
python scripts/mc_query.py schema <table_name>
```

示例：
```bash
python scripts/mc_query.py schema dim_product_info
python scripts/mc_query.py schema dws_order_detail --output schema.txt
```

输出包含：表名、Owner、创建/修改时间、所有字段（名称、类型、注释）、分区字段。

### 场景 2：执行 SQL 查询

```bash
python scripts/mc_query.py sql "<SELECT 语句>"
```

示例：
```bash
# 查最新分区的某条记录
python scripts/mc_query.py sql "SELECT * FROM soyoung_dw.dim_product_info WHERE dp = MAX_PT('soyoung_dw.dim_product_info') AND product_id = 11687092 LIMIT 1"

# 统计近7天订单
python scripts/mc_query.py sql "SELECT dp, COUNT(*) AS cnt FROM soyoung_dw.dwd_order_detail WHERE dp >= '2026-05-28' GROUP BY dp ORDER BY dp"

# 导出到 CSV
python scripts/mc_query.py sql "SELECT product_id, title, price_online FROM dim_product_info WHERE dp = MAX_PT('soyoung_dw.dim_product_info') LIMIT 100" --csv result.csv
```

### 场景 3：查看分区信息

```bash
python scripts/mc_query.py partitions <table_name>
python scripts/mc_query.py partitions <table_name> --latest   # 只看最新分区
```

### 场景 4：在 Agent 代码中直接调用

```python
from scripts.mc_query import create_odps_client, get_table_schema, run_sql_query

# 建立连接
o = create_odps_client()

# 获取表结构
schema = get_table_schema(o, "dim_product_info")
for col in schema["columns"]:
    print(f"{col['name']:<30} {col['type']:<15} {col['comment']}")

# 执行查询
result = run_sql_query(o, "SELECT product_id, title FROM dim_product_info WHERE dp = MAX_PT('soyoung_dw.dim_product_info') AND product_id = 11687092 LIMIT 1")
for row in result["rows"]:
    print(row)
```

## 安全约束

1. **只读校验**：SQL 必须以 `SELECT` 或 `WITH` 开头，拒绝 INSERT/UPDATE/DELETE/CREATE/DROP/ALTER/TRUNCATE 等写操作
2. **凭据隔离**：Access Key 只从环境变量或 `.env.odps` 读取，不硬编码、不进版本库
3. **敏感字段**：手机号、身份证等字段按需脱敏，只取分析必要列
4. **权限说明**：当前子账号 `shujuzhinengbu` 具有 SELECT 权限，但**无 Download（Tunnel）权限**。因此：
   - `execute_sql().open_reader()` 可正常工作（走 REST API）
   - `table.open_reader()` 会报 4019 错误（走 Tunnel），需改用 SQL 方式读取

## 常见问题

### Q: DNS 解析失败（getaddrinfo failed）
检查 endpoint 域名是否为 `aliyun.com`（公网），不是 `aliyuncs.com`。可用 `nslookup` 验证：
```bash
nslookup service.cn-beijing.maxcompute.aliyun.com
```

### Q: 权限不足（NoPermission / 4019）
- SELECT 权限不足 → 联系管理员授权
- Download（Tunnel）权限不足 → 改用 `execute_sql().open_reader()` 而非 `table.open_reader()`

### Q: 表不存在或无数据
- 确认 project 名称正确（默认 `soyoung_dw`）
- 分区表必须带分区条件，否则全表扫描可能超时

## 依赖

- Python >= 3.8
- pyodps（`pip install pyodps`）
- 网络可达 MaxCompute endpoint
