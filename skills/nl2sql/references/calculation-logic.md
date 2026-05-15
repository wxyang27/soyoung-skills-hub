# ③ 计算逻辑库

> 每个指标的"正确打开方式"——常见错误 + 标准公式

## 核心规则

### 规则 1：_all_d 表的正确用法

```
❌ 错误：dp='2026-05-13' → 取了截至5/13全量历史
✅ 正确：dp='最新日期' + executed_date='2026-05-13'

原因：_all_d 是天级全量快照（All-Day），不是增量表。
dp 决定用哪个快照版本，executed_date 决定取哪天发生的数据。
```

### 规则 2：dp 取最新可用

```
最新 dp 通常 = 昨天（T+1 延迟）
检查方法：SELECT MAX(dp) FROM table_name
```

### 规则 3：核销 vs 支付

```
核销(executed)：实际到院消费 → 用 dm_opt_qy_user_execution_record_all_d
支付(pay)：下单付款 → 用 dm_opt_qy_order_info_all_d
连锁业务以核销口径为准
```

### 规则 4：渠道字段名

| 层级 | 正确字段 | 错误字段 |
|------|---------|---------|
| 一级 | cx_first_channel | ~~channel_type~~ |
| 二级 | cx_second_channel | ~~channel~~ |
| 三级 | cx_third_channel | — |

### 规则 5：客单价的分母

```
客单价 = SUM(exe_income) / COUNT(DISTINCT verify_date_id)  ← 人次
ARPU   = SUM(exe_income) / COUNT(DISTINCT customer_id)     ← 人头
```

### 规则 6：MaxCompute 语法差异

```
- ORDER BY 必须配 LIMIT（否则报错）
- 分区表必须指定 dp 过滤（否则全表扫描报错）
- 字符串用单引号
- 子查询建议加别名
```

## 常见错误速查

| 错误现象 | 根因 | 正确做法 |
|---------|------|---------|
| 数值极大(8亿) | dp过滤没用executed_date | dp+executed_date双过滤 |
| 结果为0 | dp日期还不存在(今天) | 用昨天或更早的dp |
| 字段不存在 | 字段名与表不匹配 | 查DESC确认字段名 |
| ORDER BY报错 | 没加LIMIT | 加LIMIT 500 |
| 全表扫描报错 | 没指定dp | 加dp=具体日期 |
