# 原子指标字典（19 个）

> 来源：指标字典 · 原子指标字典 sheet。原子指标是所有衍生指标的拼装基础。
> 默认分区 `dp = DATE_SUB(CURRENT_DATE(),1)`（T+1）。核销加 `is_valid = 1`；支付加 `is_paydate_cash = 0`（剔除当日退款）。

## 速查表

| ID | 指标 | 英文 | 业务域 | 聚合方式 | 单位 | 源表 | 衍生数 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A001 | 核销gmv | verify_gmv | 核销 | `SUM(金额字段)` | 元 | `dm_opt_qy_user_execution_record_all_d` | 9 |
| A002 | 核销收入 | verify_income | 核销 | `SUM(金额字段)` | 元 | `dm_opt_qy_user_execution_record_all_d` | 9 |
| A003 | 核销客单价 | verify_avg_price | 核销 | `SUM(收入) / COUNT(DISTINCT 人次)` | 元/人次 | `dm_opt_qy_user_execution_record_all_d` | 10 |
| A004 | 核销服务点数 | verify_service_points | 核销 | `SUM(exe_cnt)` | 个 | `dm_opt_qy_user_execution_record_all_d` | 9 |
| A005 | 核销人数 | verify_user_cnt | 核销 | `COUNT(DISTINCT uid)` | 人 | `dm_opt_qy_user_execution_record_all_d` | 0 |
| A006 | 核销人次 | verify_visit_cnt | 核销 | `COUNT(DISTINCT verify_date_id)` | 人次 | `dm_opt_qy_user_execution_record_all_d` | 12 |
| A007 | 核销订单数 | verify_order_cnt | 核销 | `COUNT(DISTINCT order_id)` | 单 | `dm_opt_qy_user_execution_record_all_d` | 19 |
| A008 | 支付gmv | pay_gmv | 支付 | `SUM(金额字段)` | 元 | `dm_opt_qy_order_info_all_d` | 4 |
| A009 | 支付订单数 | pay_order_cnt | 支付 | `COUNT(DISTINCT order_id)` | 单 | `dm_opt_qy_order_info_all_d` | 6 |
| A010 | 支付人数 | pay_user_cnt | 支付 | `COUNT(DISTINCT uid)` | 人 | `dm_opt_qy_order_info_all_d` | 4 |
| A011 | 支付客单价 | pay_avg_price | 支付 | `SUM(收入) / COUNT(DISTINCT 人次)` | 元/人次 | `dm_opt_qy_order_info_all_d` | 4 |
| A012 | 待核销gmv | pending_verify_gmv | 支付 | `SUM(金额字段)` | 元 | `dm_opt_qy_order_info_all_d` | 4 |
| A013 | 待核销服务点 | pending_verify_sp | 支付 | `SUM(exe_cnt)` | 个 | `dm_opt_qy_order_info_all_d` | 4 |
| A014 | 待核销订单数 | pending_verify_order_cnt | 支付 | `COUNT(DISTINCT order_id)` | 单 | `dm_opt_qy_order_info_all_d` | 0 |
| A015 | 升单订单数 | upsell_order_cnt | 核销 | `COUNT(DISTINCT order_id)` | 单 | `dm_opt_qy_user_execution_record_all_d` | 9 |
| A016 | 升单人数 | upsell_user_cnt | 核销 | `COUNT(DISTINCT uid)` | 人 | `dm_opt_qy_user_execution_record_all_d` | 9 |
| A017 | 升单人次 | upsell_visit_cnt | 核销 | `COUNT(DISTINCT verify_date_id)` | 人次 | `dm_opt_qy_user_execution_record_all_d` | 9 |
| A018 | 库存数 | inventory_cnt | 库存 | `` | 件 | `dws_qy_sc_ware_stock_stats_all_d` | 0 |
| A019 | 相控微针升单率 | micro_needle_upsell_rate | 核销 | `分子指标 / 分母指标` | % | `dm_opt_qy_user_execution_record_all_d` | 0 |

## 完整定义与 SQL

### A001 核销gmv（verify_gmv）

- 业务域：核销　单位：元　数据类型：DECIMAL
- 定义：统计周期内，连锁业务总核销gmv
- 计算逻辑：`SUM(金额字段)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_amount) 核销gmv
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     is_valid = 1
```

### A002 核销收入（verify_income）

- 业务域：核销　单位：元　数据类型：DECIMAL
- 定义：统计周期内，连锁业务总核销收入
- 计算逻辑：`SUM(金额字段)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_income) 核销收入
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     is_valid = 1
```

### A003 核销客单价（verify_avg_price）

- 业务域：核销　单位：元/人次　数据类型：DECIMAL
- 定义：统计周期内，总核销收入/总核销人次
- 计算逻辑：`SUM(收入) / COUNT(DISTINCT 人次)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`
- ⚠ 备注：⚠ 原SQL使用verify_date_id统计人次，请确认是否等同于核销人次

```sql
SELECT SUM(exe_income)/COUNT(DISTINCT verify_date_id) 核销客单价
FROM  soyoung_dw.dm_opt_qy_user_execution_record_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1) 
AND is_valid = 1
```

### A004 核销服务点数（verify_service_points）

- 业务域：核销　单位：个　数据类型：INT
- 定义：统计周期内，总核销服务点数
- 计算逻辑：`SUM(exe_cnt)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_cnt) 核销服务点数
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     is_valid = 1
```

### A005 核销人数（verify_user_cnt）

- 业务域：核销　单位：人　数据类型：INT
- 定义：统计周期内，总核销用户数
- 计算逻辑：`COUNT(DISTINCT uid)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT COUNT(DISTINCT customer_id) 核销人数
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     is_valid = 1
```

### A006 核销人次（verify_visit_cnt）

- 业务域：核销　单位：人次　数据类型：INT
- 定义：统计周期内，总核销人次
- 计算逻辑：`COUNT(DISTINCT verify_date_id)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  count(DISTINCT verify_date_id) 核销人次
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     is_valid = 1
```

### A007 核销订单数（verify_order_cnt）

- 业务域：核销　单位：单　数据类型：INT
- 定义：统计周期内，总核销订单数
- 计算逻辑：`COUNT(DISTINCT order_id)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  count(DISTINCT main_order_id) 核销订单数
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     is_valid = 1
```

### A008 支付gmv（pay_gmv）

- 业务域：支付　单位：元　数据类型：DECIMAL
- 定义：统计周期内，总支付gmv(剔除当日退款)
- 计算逻辑：`SUM(金额字段)`
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
select sum(pay_gmv) as 支付gmv
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_paydate_cash = 0
;
```

### A009 支付订单数（pay_order_cnt）

- 业务域：支付　单位：单　数据类型：INT
- 定义：统计周期内，总支付订单数(剔除当日退款)
- 计算逻辑：`COUNT(DISTINCT order_id)`
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
select count(disticnt main_order_id) as 支付订单数
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_paydate_cash = 0
;
```

### A010 支付人数（pay_user_cnt）

- 业务域：支付　单位：人　数据类型：INT
- 定义：统计周期内，总支付人数(剔除当日退款)
- 计算逻辑：`COUNT(DISTINCT uid)`
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
SELECT  COUNT(DISTINCT uid) as 支付人数
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_paydate_cash = 0
;
```

### A011 支付客单价（pay_avg_price）

- 业务域：支付　单位：元/人次　数据类型：DECIMAL
- 定义：统计周期内，总支付GMV/总支付人次(剔除当日退款)
- 计算逻辑：`SUM(收入) / COUNT(DISTINCT 人次)`
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
SELECT sum(pay_gmv)/count(distinct concat(uid,pay_date)) as 支付客单价
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_paydate_cash = 0
;
```

### A012 待核销gmv（pending_verify_gmv）

- 业务域：支付　单位：元　数据类型：DECIMAL
- 定义：统计周期内，总待核销gmv
- 计算逻辑：`SUM(金额字段)`
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
SELECT  
sum(left_gmv) as 待核销gmv
FROM  soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND left_num > 0
;
```

### A013 待核销服务点（pending_verify_sp）

- 业务域：支付　单位：个　数据类型：INT
- 定义：统计周期内，总待核销服务点
- 计算逻辑：`SUM(exe_cnt)`
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
SELECT  
sum(left_num) as 待核销服务点
FROM  soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND left_num > 0
;
```

### A014 待核销订单数（pending_verify_order_cnt）

- 业务域：支付　单位：单　数据类型：INT
- 定义：统计周期内，总待核销订单数
- 计算逻辑：`COUNT(DISTINCT order_id)`
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
SELECT  
COUNT(DISTINCT main_order_id) as 待核销订单数
FROM  soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND left_num > 0
;
```

### A015 升单订单数（upsell_order_cnt）

- 业务域：核销　单位：单　数据类型：INT
- 定义：统计周期内，升单的总订单数
- 计算逻辑：`COUNT(DISTINCT order_id)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  
COUNT(DISTINCT main_order_id) as 升单订单数
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d 
WHERE   dp = DATE_SUB(current_date(),1)
 AND     is_up = 1
 AND     is_valid = 1
```

### A016 升单人数（upsell_user_cnt）

- 业务域：核销　单位：人　数据类型：INT
- 定义：统计周期内，升单的总用户数
- 计算逻辑：`COUNT(DISTINCT uid)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  
COUNT(DISTINCT customer_id) AS 升单人数
 FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d 
WHERE   dp = DATE_SUB(current_date(),1)
AND     is_up = 1
 AND     is_valid = 1
```

### A017 升单人次（upsell_visit_cnt）

- 业务域：核销　单位：人次　数据类型：INT
- 定义：统计周期内，升单的总人次
- 计算逻辑：`COUNT(DISTINCT verify_date_id)`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  COUNT(DISTINCT verify_date_id) AS 升单人次
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(current_date(),1)
AND     is_up = 1
AND     is_valid = 1
```

### A018 库存数（inventory_cnt）

- 业务域：库存　单位：件　数据类型：INT
- 定义：截止至今，总库存数量
- 计算逻辑：``
- 源表：`soyoung_dw.dws_qy_sc_ware_stock_stats_all_d`

```sql
SELECT ware_name,
        ROUND(SUM(warehouse_stock_num_td), 0) AS 库存数
    FROM soyoung_dw.dws_qy_sc_ware_stock_stats_all_d
    WHERE pt = DATE_SUB(CURRENT_DATE(), 1)
    GROUP BY ware_name
```

### A019 相控微针升单率（micro_needle_upsell_rate）

- 业务域：核销　单位：%　数据类型：DECIMAL
- 定义：统计周期内，原单为相控微针且当日发生升单的核销人次/相控微针原单核销人次
- 计算逻辑：`分子指标 / 分母指标`
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT a.standard_name ,COUNT(DISTINCT IF(b.verify_date_id IS NOT NULL,a.verify_date_id,NULL)) / COUNT(DISTINCT a.verify_date_id)升单率
FROM    (
            SELECT  standard_name
                    ,verify_date_id
            FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d 
            WHERE   dp = DATE_SUB(current_date(),1)
            and     is_valid = 1
            AND     standard_name REGEXP '相控微针'
            AND     ord_up_type_name = '原单'
        ) a
LEFT JOIN   (
                SELECT  
                         standard_name
                         ,verify_date_id 
                FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d 
                WHERE   dp = DATE_SUB(current_date(),1)
                AND     ord_up_type_name = '升单'
                AND     is_valid = 1
            ) b
ON     a.verify_date_id = b.verify_date_id
GROUP BY a.standard_name
;
```
