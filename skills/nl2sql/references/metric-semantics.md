# ① 指标语义库

> 将"老客收入""新客 GMV""核销人次"等业务语言映射到 `表.字段 + 过滤条件`

## 收入类

| 业务名称 | 别名 | 表 | 字段 | 聚合 | 关键过滤 |
|---------|------|-----|------|------|---------|
| 核销收入 | 收入、营收、销售额 | dm_opt_qy_user_execution_record_all_d | exe_income | SUM | is_valid=1 |
| 支付 GMV | 支付金额、GMV | dm_opt_qy_order_info_all_d | pay_amount | SUM | is_payed=1 |
| 核销 GMV | verify_gmv | dm_opt_qy_user_execution_record_all_d | exe_amount | SUM | is_valid=1 |
| 待核销 GMV | left_gmv | dm_opt_qy_order_info_all_d | left_gmv | SUM | is_payed=1 |

**核销 vs 支付：** 连锁业务以核销口径为准。支付 = 下单未消费，核销 = 实际到院消费。

## 客户量类

| 业务名称 | 别名 | 计算逻辑 |
|---------|------|---------|
| 核销人数 | 客户数、人头 | COUNT(DISTINCT customer_id) |
| 核销人次 | 到院次数 | COUNT(DISTINCT verify_date_id) |
| 核销订单数 | 订单数 | COUNT(DISTINCT order_id) |
| 新客人数 | 新客户数 | 同上 + is_new=1 |
| 老客人数 | 老客户数 | 同上 + is_new=0 |

**关键区分：** 人数用 customer_id，人次用 verify_date_id。同一人不同天到院算多人次。

## 客单价类

| 业务名称 | 别名 | 计算逻辑 |
|---------|------|---------|
| 核销客单价 | 客单价、ASP | SUM(exe_income) / COUNT(DISTINCT verify_date_id) |
| 首次客单价 | first_asp | SUM(首次当天 exe_income) / COUNT(DISTINCT verify_date_id) |
| ARPU | 人均收入 | SUM(exe_income) / COUNT(DISTINCT customer_id) |
| 单服务点收入 | rev_per_svc | SUM(exe_income) / SUM(exe_cnt) |

**关键区分：** 客单价分母是人次(verify_date_id)，不是人头(customer_id)。

## 留存/LTV 类

| 业务名称 | 别名 | 计算逻辑 |
|---------|------|---------|
| 90天留存率 | retention | 首次后1-90天有再次核销的人头/总人头 |
| 365天 LTV | LTV | 首次后365天内 SUM(exe_income) / 总人头 |
| 增量 LTV | inc_ltv | LTV_Y - LTV_X（某时段内新增人均收入） |

## 服务点类

| 业务名称 | 别名 | 计算逻辑 |
|---------|------|---------|
| 核销服务点数 | 服务点、点数 | SUM(exe_cnt) |
| 单次服务点数 | svc_per_visit | SUM(exe_cnt) / COUNT(DISTINCT verify_date_id) |

## 新老客定义

- **新客(is_new=1)：** 该客户全历史首次核销。由 ETL 预计算，非 SQL 实时判断。
- **老客(is_new=0)：** 非首次核销。
- **注意：** is_new 在 `_all_d` 全量快照中 = 截至该 dp 日期的状态，不是 executed_date 当天的状态。
