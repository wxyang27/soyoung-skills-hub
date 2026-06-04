# SQL 约定与时间口径

> 这是组装可执行 SQL 的工程规范。所有取数 SQL 都应遵守。

## 1. SQL 方言

- 目标引擎是 **ODPS / MaxCompute（Hive 语法族）**。
- 常用函数：`DATE_SUB`、`CURRENT_DATE()`、`DATE_FORMAT`、`SUBSTR`、`REGEXP`、`CONCAT`、`COLLECT_SET`、`DENSE_RANK() OVER(...)`、`NULLIF`、`COALESCE`、`IF`、`CASE WHEN`。
- 字符串等值用单引号：`revenue_category = '大单品'`。
- 部署到其它引擎（如 Hive/Spark/Presto/StarRocks）时：先确认 `CURRENT_DATE()` 与 `DATE_SUB` 行为，再按需替换日期函数。

## 2. 分区与时效（必加，不可省）

- 多数主题/汇总日表是 **T+1**，分区字段 `dp`，标准写法二选一：
  - `dp = CURRENT_DATE() - 1`
  - `dp = DATE_SUB(CURRENT_DATE(), 1)`
- **库存表 `dws_qy_sc_ware_stock_stats_all_d` 分区字段是 `pt`**，不是 `dp`。
- JOIN 维表时，维表也要带自己的分区，例如 `dim_product_info c ON ... AND c.dp = CURRENT_DATE() - 1`。
- 绝不允许不带分区直接扫全表。

## 3. 各域标准过滤（默认必加）

| 业务域 | 主表 | 默认过滤 |
| --- | --- | --- |
| 核销 | `dm_opt_qy_user_execution_record_all_d` | `dp = CURRENT_DATE()-1` + `is_valid = 1` |
| 支付 | `dm_opt_qy_order_info_all_d` | `dp = CURRENT_DATE()-1` + `is_paydate_cash = 0` |
| 待核销 | `dm_opt_qy_order_info_all_d` | `dp = CURRENT_DATE()-1` + `left_num > 0` |
| 用户画像-支付 | `dwd_ord_order_qzy_fact_all_d` | `dp = CURRENT_DATE()-1` + `bus_type IN ('新氧优享','连锁')` + `is_ass_hospital = 1` + `is_payed = 1` + `pay_date != COALESCE(cash_back_date,0)` |
| 库存 | `dws_qy_sc_ware_stock_stats_all_d` | `pt = DATE_SUB(CURRENT_DATE(),1)` |

用户画像-支付域的线上/线下/医美切分：
- 线上：`app_id <> 126`
- 线下：`app_id = 126`
- 医美（排除好物）：JOIN `dim_product_info`，`(track <> '好物' OR track IS NULL)`

## 4. 时间范围翻译（口语 → SQL）

`dp` 是「数据快照分区」，恒等于昨天（T+1 最新一版全量）。**业务时间范围**通常另用业务日期字段过滤（核销看 `executed_date`，支付看 `pay_date`/`verify_date`）。下表 `<biz_date>` 代表对应业务日期字段。

| 口语 | 业务时间过滤 | 说明 |
| --- | --- | --- |
| 昨天 / 日 | `<biz_date> = DATE_SUB(CURRENT_DATE(),1)` | 单日 |
| 近 7 天 | `<biz_date> BETWEEN DATE_SUB(CURRENT_DATE(),7) AND DATE_SUB(CURRENT_DATE(),1)` | 滚动 7 天 |
| 近 30 天 | `<biz_date> BETWEEN DATE_SUB(CURRENT_DATE(),30) AND DATE_SUB(CURRENT_DATE(),1)` | 滚动 30 天 |
| 近 90 天 / 90天滚动 | `<biz_date> BETWEEN DATE_SUB(DATE_SUB(CURRENT_DATE(),1),89) AND DATE_SUB(CURRENT_DATE(),1)` | 截至昨天的滚动 90 天（见 D132 渗透率） |
| 本月 MTD | `<biz_date> >= DATE_FORMAT(CURRENT_DATE(),'yyyy-MM-01') AND <biz_date> <= DATE_SUB(CURRENT_DATE(),1)` | 月初至昨天 |
| 上个月（完整） | `<biz_date> >= 上月1号 AND <biz_date> <= 上月末` | 需算月首月末，建议确认是否要完整自然月 |
| 某活动期 | `<biz_date> BETWEEN '<start>' AND '<end>'` | 活动起止需用户给定 |

> ⚠ `dp`（快照）与业务日期（发生时间）是两回事：
> - 只取「最新一版数据里某业务时间段的发生量」→ 固定 `dp = 昨天`，再用 `<biz_date>` 框业务区间。
> - 字典里大量单日示例 SQL 只有 `dp = 昨天`、没单独业务日期，等价于「看昨天发生的量」。扩成多天时务必补 `<biz_date>` 区间，别用多天 `dp`（会重复累计全量快照）。

## 5. 比率 / 复合指标安全写法

- 分母一律 `NULLIF(分母, 0)` 防除零。
- 比率指标**先分别算分子分母，再在外层相除**，不要在明细行上直接除。
- 客单价：`SUM(exe_income) / NULLIF(COUNT(DISTINCT verify_date_id), 0)`。
  - ⚠ 字典明确标注：核销客单价用 `verify_date_id` 统计人次，**是否完全等同「核销人次」待确认**（见 01 A003 备注）。高精度场景需确认。

## 6. 粒度 / JOIN 防重复累计

- 写 SQL 前先想清楚：主表颗粒度？指标颗粒度？JOIN 后会不会放大行数？
- 高风险时：**先在子查询里聚合到统一粒度，再 JOIN**。
- 「首单/末单」类用 `DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC|DESC)` 取 `rn = 1`（见 03 用户画像字段）。

## 7. 安全的取数顺序（强烈建议）

1. 连通性：`SELECT 1 AS x`
2. 样例预览：只取必要字段 + `LIMIT 10`，确认字段真实存在、值符合预期
3. 正式聚合：带全部过滤 + 维度 `GROUP BY`
4. 如需下钻，再加细维度

禁止：一上来 `SELECT *` 扫大表、不带分区、先大宽 JOIN 再聚合。

## 8. 可复制骨架

```sql
-- 核销类：先把过滤放进 base，再聚合
WITH base AS (
  SELECT tenant_id, customer_id, verify_date_id, main_order_id,
         exe_amount, exe_income, exe_cnt, is_new, revenue_category, cx_first_channel
  FROM   soyoung_dw.dm_opt_qy_user_execution_record_all_d
  WHERE  dp = CURRENT_DATE() - 1
  AND    is_valid = 1
  -- AND  <业务时间区间，多天时加>
  -- AND  <维度过滤，如 is_new = 1 / revenue_category='大单品' / standard_name REGEXP 'BBL HERO'>
)
SELECT
  is_new,                                                      -- 维度（按需 GROUP BY）
  SUM(exe_amount)                                  AS 核销gmv,
  SUM(exe_income)                                  AS 核销收入,
  SUM(exe_cnt)                                     AS 核销服务点数,
  COUNT(DISTINCT customer_id)                      AS 核销人数,
  COUNT(DISTINCT verify_date_id)                   AS 核销人次,
  COUNT(DISTINCT main_order_id)                    AS 核销订单数,
  SUM(exe_income)/NULLIF(COUNT(DISTINCT verify_date_id),0) AS 核销客单价
FROM base
GROUP BY is_new
;
```

```sql
-- 支付类
SELECT
  SUM(pay_gmv)                                          AS 支付gmv,
  COUNT(DISTINCT main_order_id)                         AS 支付订单数,
  COUNT(DISTINCT uid)                                   AS 支付人数,
  SUM(pay_gmv)/NULLIF(COUNT(DISTINCT CONCAT(uid,pay_date)),0) AS 支付客单价
FROM soyoung_dw.dm_opt_qy_order_info_all_d
WHERE dp = CURRENT_DATE() - 1
AND   is_paydate_cash = 0
-- AND is_pay_new = 1            -- 新客（注意支付域用 is_pay_new）
;
```
