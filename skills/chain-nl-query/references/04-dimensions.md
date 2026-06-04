# 维度字典 & 字段名差异（取数最易踩坑处）

> 来源：指标字典 · 维度字典 sheet + 各 sheet SQL 实证对比。
> **本文件是字段名歧义的权威裁决处。组装 SQL 前必须核对这里。**

## 1. 标准维度（10 个）

| ID | 维度 | 字典登记字段 | 取值范围 | 影响指标 |
| --- | --- | --- | --- | --- |
| DIM001 | 新客/老客 | `is_new` | 1=新客, 0=老客 | 核销全系 + 升单 |
| DIM002 | 大师团 | `is_master`（见下方⚠） | 1=是, 0=否 | 核销全系 + 升单 |
| DIM003 | 收入分类 | `income_type`（见下方⚠） | 大单品 / 常规品 | 核销全系 + 升单 |
| DIM004 | 获客渠道 | `channel_type`（见下方⚠） | 私域 / 公域 / 老带新 | 核销全系 + 升单 |
| DIM005 | 品项名称 | `product_name`（见下方⚠） | 自由文本，**支持 REGEXP** | 品项渗透率/加购率/升单率 |
| DIM006 | 订单金额(0元单) | `exe_amount` / `pay_amount` | 0元 / 非0元 | 0元单占比、0元核销订单数 |
| DIM007 | 支付渠道 | `channel`（线上/线下） | 线上 / 线下 | 用户画像支付字段 |
| DIM008 | 业务领域 | `business_type` | 连锁 / 医美 / 好物 | 用户画像支付字段 |
| DIM009 | 时间粒度 | `dp` / `verify_date` | 日/周/月/季/90天滚动 | 所有指标 |
| DIM010 | 门店 | `store_id` / `store_name` | 门店ID/名称 | 门店维度看板 |

## 2. ⚠ 字段名差异表（字典登记名 ≠ 实际 SQL 用名）

维度字典 sheet 里登记的「对应字段」与衍生指标 sheet 里**实际跑数 SQL** 用的字段名不一致。
**取数以实际 SQL 字段名为准**（下表「实际 SQL 字段」列），并在输出里注明。
能预览/查询真实表时，务必先核对真实表结构再定稿。

| 维度 | 字典登记名 | **实际 SQL 字段（以此为准）** | 实际取值 / 写法 |
| --- | --- | --- | --- |
| 大师团 | `is_master = 1` | `revenue_category = '大师团'` | revenue_category 同时承载大师团/大单品/常规品三类 |
| 收入分类·大单品 | `income_type='大单品'` | `revenue_category = '大单品'` | — |
| 收入分类·常规品 | `income_type='常规品'` | `revenue_category = '常规品'` | — |
| 获客渠道 | `channel_type` | `cx_first_channel` | `'私域'` / `'公域'` / `'老带新'` |
| 品项名称 | `product_name` | 多数指标用 `standard_name REGEXP '<品项>'` | 见下方 ⚠⚠ |
| 新客（支付域） | `is_new` | **`is_pay_new`** | 支付主题表用 is_pay_new，核销主题表才用 is_new |

> ⚠⚠ 品项字段二义性：绝大多数品项指标用 `standard_name REGEXP '...'`，
> **但「渗透率」(D132) 的 SQL 用了 `product_name REGEXP '...'`**。两者是否等价未确认。
> 取数品项指标时：默认用 `standard_name`；若做渗透率或结果异常，需向用户/真实表确认用 `standard_name` 还是 `product_name`。

## 3. 同一业务概念在不同主题表里的字段差异

| 概念 | 核销主题 `dm_opt_qy_user_execution_record_all_d` | 支付主题 `dm_opt_qy_order_info_all_d` |
| --- | --- | --- |
| 新客标记 | `is_new` | `is_pay_new` |
| 人数 | `COUNT(DISTINCT customer_id)` | `COUNT(DISTINCT uid)` |
| 人次 | `COUNT(DISTINCT verify_date_id)` | `COUNT(DISTINCT CONCAT(uid, pay_date))` |
| 订单数 | `COUNT(DISTINCT main_order_id)` | `COUNT(DISTINCT main_order_id)` |
| 金额-GMV | `SUM(exe_amount)` | `SUM(pay_gmv)` |
| 金额-收入 | `SUM(exe_income)` | （支付域无核销收入概念） |
| 有效/退款过滤 | `is_valid = 1` | `is_paydate_cash = 0`（剔除当日退款） |
| 0元单 | `exe_income = 0` | `pay_gmv = 0` |
| 待核销过滤 | — | `left_num > 0`（金额 `left_gmv`、服务点 `left_num`） |

## 4. 「整体」口径的三层惯例

收入/客单类指标常需分三层看，默认给「整体」，必要时按澄清协议确认是否要拆：

1. **整体**：含 0 元、含大师团（不加额外过滤）
2. **非 0 元**：`AND exe_income > 0`
3. **非 0 非大师**：`AND exe_income > 0 AND revenue_category <> '大师团'`

## 5. 升单相关取值

| 字段 | 取值 | 含义 |
| --- | --- | --- |
| `is_up` | 1 | 发生升单 |
| `ord_up_type_name` | `'原单'` / `'升单'` | 升单类型，用于「相控微针升单率」「加购率」等比率 |

## 6. 大单品品项枚举（出现在多个 REGEXP 里）

`standard_name REGEXP 'BBL HERO|奇迹童颜|新一代热玛吉|爱拉丝提'`

- 「BBL HERO」业务别名为「爱拉丝提」。
- 「大单品品项核销X」类指标用上面这一串 REGEXP，而「大单品核销X」类用 `revenue_category = '大单品'`，两者口径不同，勿混。
