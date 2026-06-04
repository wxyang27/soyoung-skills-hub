# 取数执行（可选）

本 Skill 的核心产物是**正确口径的 SQL**。是否执行、用什么执行，取决于部署环境。

## 三种部署形态

1. **只生成 SQL（最通用）**
   不配置任何执行器，Skill 产出 SQL，用户拿到自己的数仓客户端（DataWorks / odpscmd / DBeaver 等）运行。
   部署到任何环境都成立，零依赖。

2. **用自带的 `query_runner.py`（ODPS / MaxCompute）**
   ```bash
   pip install pyodps
   # 设置凭据（环境变量，或在 Skill 目录放 .env.odps）
   export ODPS_ACCESS_ID=...           # 或写进 .env.odps
   export ODPS_SECRET_ACCESS_KEY=...
   export ODPS_PROJECT_NAME=soyoung_dw
   export ODPS_ENDPOINT=http://service.cn-beijing.maxcompute.aliyun.com/api

   python3 scripts/query_runner.py "SELECT 1 AS x"
   python3 scripts/query_runner.py --file q.sql --limit 50
   python3 scripts/query_runner.py "SELECT ..." --csv result.csv
   ```
   - **只读**：仅允许 `SELECT` / `WITH`，拒绝写/删/改/DDL 和多语句。
   - `--check-only` 只做安全校验不执行。

3. **接入环境已有的查询能力**
   若部署环境已有 SQL runner、`query_odps_dataframe` 之类的接口、或数据类 MCP 工具，直接用那个执行，把本脚本当后备即可。

## `.env.odps` 示例（放在 Skill 根目录或运行目录，勿提交到代码库）
```
ODPS_ACCESS_ID=your_access_id
ODPS_SECRET_ACCESS_KEY=your_secret
ODPS_PROJECT_NAME=soyoung_dw
ODPS_ENDPOINT=http://service.cn-beijing.maxcompute.aliyun.com/api
```

## 换数仓引擎
SQL 是 ODPS/MaxCompute（Hive 语法族）方言。若目标是 Hive/Spark/Presto/StarRocks：
- 复用 `query_runner.py` 的只读校验 `is_read_only()`；
- 把 `run_query()` 换成对应客户端；
- 注意替换日期函数（`CURRENT_DATE()` / `DATE_SUB` 行为差异）。见 `references/08-sql-conventions.md`。

## 安全
- 取数 Skill 只做**只读查询**。绝不在此执行写/删/改。
- 凭据只放环境变量或 `.env.odps`，不要硬编码、不要进版本库。
- 用户敏感字段（手机号、姓名等）按需脱敏，只取分析必要列。
