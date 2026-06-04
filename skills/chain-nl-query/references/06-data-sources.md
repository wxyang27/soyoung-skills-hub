# 数据源目录（指标字典口径）

> 来源：指标字典 · 数据源目录 sheet。这是**指标字典层面**最常用的少量底表（与 05-tables.md 的 49 张全量表互补）。

| ID | 表名 | 简称 | 库 | 业务说明 | 主要字段 | 更新 | 分区 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC001 | `dm_opt_qy_user_execution_record_all_d` | 核销记录宽表 | soyoung_dw | 连锁业务核销记录全量日表，包含用户、品项、金额、服务点等维度 | exe_amount, exe_income, exe_cnt, uid, customer_id, verify_date_id, order_id, is_new, is_master, is_valid, product_name, income_type, channel_type | 日更(T+1) | `dp` | 核心事实表，大部分核销/升单指标来源 |
| SRC002 | `dm_opt_qy_order_info_all_d` | 订单信息日表 | soyoung_dw | 连锁业务订单信息全量日表 | order_id, pay_amount, uid, pay_date, refund_flag | 日更(T+1) | `dp` | 支付GMV/订单数等指标来源 |
| SRC003 | `dwd_ord_order_qzy_fact_all_d` | 订单事实表 | soyoung_dw | 订单明细事实表，含支付与核销信息 | order_id, uid, pay_amount, pay_date, channel, business_type | 日更(T+1) | `dp` | 用户画像支付字段来源(线上/线下/医美/好物) |
| SRC004 | `dwd_ord_order_qy_execution_record_all_d` | 核销执行记录表 | soyoung_dw | 核销执行记录明细 | uid, verify_date, exe_amount, exe_income | 日更(T+1) | `dp` | 部分用户画像核销字段来源 |
| SRC005 | `dwd_inp_private_user_fact_all_d` | 私域用户事实表 | soyoung_dw | 私域用户标签与加C状态 | uid, is_private, is_valid_add_c, is_wz_add_c, is_store_add_c, is_group | 日更(T+1) | `dp` | 加C相关字段来源 |
| SRC006 | `dwd_md_xcx_all_log_d` | 小程序/APP日志表 | soyoung_dw | APP和小程序的用户登录与活跃日志 | uid, login_date, platform | 日更(T+1) | `dp` | 小程序/APP活跃字段来源 |
| SRC007 | `dwd_opt_qy_reserve_all_d` | 预约记录表 | soyoung_dw | 用户预约记录 | uid, reserve_date, order_id, gmv | 日更(T+1) | `dp` | 预约相关字段来源 |
