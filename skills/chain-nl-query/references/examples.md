# 取数示例（NL → 澄清 → SQL）

展示主流程与澄清协议如何落地。重点看「什么时候直接做、什么时候先问」。

---

## 例 1 · 低风险，直接做（不打断）

**用户**：昨天核销收入多少？

**识别**：指标=核销收入(`exe_income`)；对象=整体；时间=昨天(单日)；过滤=默认。
四要素齐全且无高风险歧义 → 不追问，直接取数，假设写进输出。

```sql
SELECT SUM(exe_income) AS 核销收入
FROM   soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    is_valid = 1
;
```
**口径与假设**：整体口径（含 0 元、含大师团）；「昨天」按数据快照 `dp=CURRENT_DATE()-1`（T+1）；如需「非0元/非0非大师」可再拆。

---

## 例 2 · 维度拆分 + 轻量时间确认

**用户**：上周私域和公域的核销人次分别是多少？

**识别**：指标=核销人次(`COUNT(DISTINCT verify_date_id)`)；维度=获客渠道(`cx_first_channel`，私域/公域)；时间=上周（需明确是哪 7 天 + 按核销日）。
渠道、指标都明确；唯一高风险是「上周」的具体区间与时间锚点 → 一个轻确认。

> 「上周」我按**上一个完整自然周（周一~周日）、以核销日 `executed_date` 统计**取，可以吗？或你要「近 7 天滚动」？

确认后（以近 7 天滚动、核销日为例）：
```sql
SELECT cx_first_channel AS 获客渠道,
       COUNT(DISTINCT verify_date_id) AS 核销人次
FROM   soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    is_valid = 1
AND    executed_date BETWEEN DATE_SUB(CURRENT_DATE(),7) AND DATE_SUB(CURRENT_DATE(),1)
AND    cx_first_channel IN ('私域','公域')
GROUP BY cx_first_channel
;
```
**待确认**：「上周」的口径（自然周 vs 近7天）与业务日期字段名（`executed_date`，以真实表为准）。

---

## 例 3 · 高风险多义，先合并追问

**用户**：最近收入怎么样？

**识别**：多处高风险歧义——「收入」多义、「最近」不明、对象不明。直接取数极易错。
→ 触发澄清协议，合并最多 3 问，每问给默认：

> 取数前确认 3 点（其余走默认并标注）：
> 1. **「收入」口径**：A. 核销收入 `exe_income`（默认/推荐，经营常用）B. 核销GMV `exe_amount` C. 支付GMV `pay_gmv`（收款口径）
> 2. **时间**：A. 近7天 B. 近30天（默认）C. 上一个完整自然月 D. 其他（给起止）
> 3. **范围**：A. 全连锁整体（默认）B. 按门店/区域拆 C. 按渠道或品项拆
>
> 回复如「1A 2B 3A」即可；不回的按默认。

（按 1A 2B 3A）：
```sql
SELECT SUM(exe_income) AS 核销收入
FROM   soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    is_valid = 1
AND    executed_date BETWEEN DATE_SUB(CURRENT_DATE(),30) AND DATE_SUB(CURRENT_DATE(),1)
;
```

---

## 例 4 · 复合指标 + 字段二义提醒

**用户**：BBL HERO 的渗透率？

**识别**：命中衍生指标 D132「BBL HERO渗透率」=（90日内核销过该品项的用户数 / 总核销用户数）。
两个已知风险**主动提示**（无需阻塞，但要声明）：① 90 天滚动窗口；② 渗透率 SQL 用 `product_name` 而非其它品项指标的 `standard_name`，是否等价待确认。

```sql
SELECT ROUND(
         COUNT(DISTINCT CASE WHEN product_name REGEXP 'BBL HERO' THEN customer_id END) * 1.0
         / NULLIF(COUNT(DISTINCT customer_id), 0), 4) AS 渗透率
FROM   soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    executed_date BETWEEN DATE_SUB(DATE_SUB(CURRENT_DATE(),1),89) AND DATE_SUB(CURRENT_DATE(),1)  -- 截至昨天滚动90天
AND    is_valid = 1
;
```
**待确认**：品项字段 `product_name` vs `standard_name`（其余品项指标用后者）；90 天窗口是否符合预期。

---

## 例 5 · 用户画像 / 人群圈选

**用户**：圈出累计支付金额超过 2 万的连锁用户。

**识别**：用户级问题 → 查 03 用户画像字段，命中 U012「连锁累计订单支付金额gmv」。沿用其底表与标准过滤，外层加阈值。

```sql
SELECT user_id, SUM(pay_gmv) AS 连锁累计支付gmv
FROM   soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    bus_type IN ('新氧优享','连锁')
AND    pay_date != COALESCE(cash_back_date, 0)
AND    is_ass_hospital = 1
AND    is_payed = 1
GROUP BY user_id
HAVING SUM(pay_gmv) > 20000
;
```
**口径与假设**：累计=全历史（最新快照）；「连锁」含新氧优享；已剔除当日退款单。

---

## 例 6 · 指标不在字典，必须确认

**用户**：盯盘看板上的「整体人均服务点数」帮我取一下。

**识别**：查 07 看板指标映射——该指标「是否在指标字典 = 否」，无标准 SQL。**不能臆造**。
→ 追问口径：

> 「整体人均服务点数」未进标准指标字典，我需要确认口径：
> 1. 分子是 **核销服务点数 `SUM(exe_cnt)`** 吗？
> 2. 分母「人均」的「人」是 **核销人数 `COUNT(DISTINCT customer_id)`** 还是 **核销人次 `COUNT(DISTINCT verify_date_id)`**？
> 3. 时间与范围（默认近30天/全连锁）？
>
> 确认后我按 `分子/NULLIF(分母,0)` 取数。

（若用户确认：人均=按人数）
```sql
SELECT SUM(exe_cnt) / NULLIF(COUNT(DISTINCT customer_id), 0) AS 人均服务点数
FROM   soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    is_valid = 1
;
```

---

## 例 7 · 新客口径跨域（is_pay_new vs is_new）

**用户**：上月新客支付 GMV 和新客核销收入。

**识别**：两个指标分属支付域与核销域，「新客」字段不同——支付用 `is_pay_new`、核销用 `is_new`。主动用正确字段，并声明。

```sql
-- 新客支付GMV（支付域 → is_pay_new）
SELECT SUM(pay_gmv) AS 新客支付gmv
FROM   soyoung_dw.dm_opt_qy_order_info_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    is_paydate_cash = 0
AND    is_pay_new = 1
AND    pay_date >= '<上月1号>' AND pay_date <= '<上月末>'
;

-- 新客核销收入（核销域 → is_new）
SELECT SUM(exe_income) AS 新客核销收入
FROM   soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE  dp = CURRENT_DATE() - 1
AND    is_valid = 1
AND    is_new = 1
AND    executed_date >= '<上月1号>' AND executed_date <= '<上月末>'
;
```
**待确认**：上月自然月起止日期（请确认或由环境日期函数计算）；两个域的「新客」定义不同已分别用 `is_pay_new` / `is_new`。
