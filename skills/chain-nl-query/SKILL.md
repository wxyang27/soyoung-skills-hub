---
name: chain-nl-query
description: Use when turning a natural-language data request about the chain (连锁) business into a correct, standard-caliber SQL query (and optionally running it). Triggers on 自然语言取数、取数、帮我查/拉一下数据、这个指标怎么算、写个SQL、某指标是多少、新客/老客/核销/支付/GMV/客单价/升单/渗透率/待核销/门店/品项/私域 等连锁指标问数. Grounded in the company 指标字典 (19 atomic + 132 derived + 112 user fields + 288 dashboard metrics) and 库表地图 (49 tables). Asks the requester to clarify whenever the metric caliber, time window, object, or field mapping is ambiguous.
---

# 连锁 · 自然语言取数（NL → 标准口径 SQL）

## 这个 Skill 做什么

把一句自然语言的取数需求，翻译成**符合公司标准口径**的、可执行的 SQL（需要时再执行、如实返回数据）。
核心原则一句话：

> **先定指标口径，再定表，再定时间与维度，再写 SQL。任何一步不确定且会改变结果，就先向提问者确认，绝不臆造口径。**

本 Skill **只做取数**：把需求翻译成正确口径的 SQL，并（按需）执行、如实返回数据。
**不做经营诊断、原因归因、复盘、量价拆解或策略建议**——「为什么变差 / 怎么追回来 / 该怎么做」这类不在本 Skill 范围内。本 Skill 的终点是「拿到正确口径的数」，不是「解读数」。

## 何时使用 / 不使用

**使用：**
- 「帮我查 / 拉一下 / 算一下」某个连锁指标、某段时间、某个对象的数。
- 「这个指标怎么算 / 口径是什么 / 用哪张表」。
- 把看板上看到的指标名对回标准口径并取数。
- 圈用户人群 / 取用户画像字段。

**不使用：**
- 不依赖公司口径和库表的通用 SQL 教学。
- ETL / 建模 / 调度开发。
- 纯经营诊断与策略复盘（用分析类 skill）。

## 取数主流程（5 步）

### Step 1 · 解析需求 → 取数四要素
把问题拆成结构化要素，缺哪个心里要有数：

1. **指标**：要算什么（核销收入？支付 GMV？客单价？渗透率？某用户字段？）
2. **对象 / 维度**：看整体，还是按 门店 / 城市 / 区域 / 渠道 / 品项 / 新老客 / 员工 拆？是某一个具体对象，还是要排行/对比？
3. **时间**：哪段时间？按什么业务日期锚定（支付日 / 核销日）？
4. **过滤口径**：含不含 0 元单？含不含大师团？线上/线下？连锁/医美/好物？

> 解析后先**一句话复述需求**，确认你理解对了，再往下走。

### Step 2 · 匹配指标口径（按优先级查字典）
**先查字典，再写 SQL。** 匹配顺序：

1. **衍生指标精确匹配** → 见 [02-derived-metrics.md](references/02-derived-metrics.md)（132 个，如「新客核销收入」「大单品核销客单价」直接命中）。
2. **原子指标 + 维度组合** → 用户的「维度词 + 指标词」可拼装（如「私域 + 核销人次」= 原子「核销人次」+ `cx_first_channel='私域'`）。原子见 [01-atomic-metrics.md](references/01-atomic-metrics.md)，维度字段名见 [04-dimensions.md](references/04-dimensions.md)。
3. **用户画像字段** → 用户级问题（首单/末单/累计/某用户标签）见 [03-user-profile-fields.md](references/03-user-profile-fields.md)。
4. **看板指标映射** → 用户报的是某看板上的名字，查 [07-dashboard-metrics.md](references/07-dashboard-metrics.md)。⚠ 其中约 259/288 未进字典，命中这类**必须走澄清协议确认口径**。
5. **都没有** → 不要硬造。走澄清协议：问能否用原子指标拼装，或请用户给定义/公式/源表。

为命中的指标生成一张**口径卡片**（指标 / 定义 / 源表 / 必加过滤 / 可用维度 / 已知风险），再继续。

### Step 3 · 定表 + 解析维度与时间
- **选表**：优先 DM/DWS 宽表，宽表缺字段或要单笔明细才下钻 DWD。表清单见 [05-tables.md](references/05-tables.md)。
- **维度字段名以实际 SQL 为准**（字典登记名常与实表不符），核对 [04-dimensions.md](references/04-dimensions.md) 的「字段名差异表」。
- **时间**：把口语时间翻成 SQL，注意 `dp`（快照分区）≠ 业务日期（发生时间）。多天范围用业务日期框，别用多天 `dp`。详见 [08-sql-conventions.md](references/08-sql-conventions.md) §4。

### Step 4 · 组装 SQL（守约定）
遵守 [08-sql-conventions.md](references/08-sql-conventions.md)：必带分区；核销加 `is_valid=1`、支付加 `is_paydate_cash=0`、待核销加 `left_num>0`；比率用 `NULLIF` 防除零、先分子分母再相除；有 JOIN 放大风险时先聚合再关联。

### Step 5 · 自检 + 输出（按需执行）
输出前做四查：**口径**（过滤/分母/时间是否合字典）、**粒度**（JOIN 是否重复累计）、**字段**（字段名是否真实存在，不一致已声明）、**结构**（分项能否回到总盘）。
然后按「输出格式」给结果。若环境可执行，见「取数执行」。

---

## ⭐ 澄清与追问协议（核心）

取数最大的风险是**用错口径却看起来对**。因此在写出最终 SQL 前，对照下面的**歧义检查清单**逐项判断：

> 对每一项问两个问题：(a) 这一点从需求里能确定吗？(b) 不同选择会显著改变结果吗？
> **只有「不能确定」且「会改变结果」的项，才需要向提问者确认。** 其余按默认假设执行并在输出里声明。

### 歧义检查清单（高风险 → 倾向追问）
1. **指标口径多义**：用户说「收入」可能是核销收入(`exe_income`) / 核销GMV(`exe_amount`) / 支付GMV(`pay_gmv`)；说「客单价」要确认核销 vs 支付。
2. **含不含 0 元 / 大师团**：影响收入、客单价、订单数结构（整体 / 非0元 / 非0非大师，见 04 §4）。
3. **时间范围 + 时间锚点**：「最近」= 近7/30/90 天？「上月」要完整自然月吗？按**支付日**还是**核销日**统计？
4. **对象粒度**：看整体，还是按某维度拆？指名某门店/城市但未给具体 ID/名称？要单值还是排行？
5. **新客口径**：支付域新客是 `is_pay_new`、核销域是 `is_new`，二者口径不同；用户说「新客」要落到哪个域。
6. **字段名不一致**：字典登记名 ≠ 实表名（`is_master`↔`revenue_category`、`channel_type`↔`cx_first_channel`、`product_name`↔`standard_name`）。能查真实表就先预览核对；不能就声明按字典 SQL 字段执行。
7. **品项字段二义**：品项指标默认 `standard_name REGEXP`，但「渗透率」用 `product_name`——做渗透率/结果异常时确认。
8. **指标不在字典**：命中看板未登记指标，或字典完全没有 → 必须确认口径/定义，不能臆造。
9. **跨体系混用**：私域 `union_id` / 有赞订单 / 连锁门店履约 口径不互通，涉及多体系先点明。

### 怎么问（一次问清，别挤牙膏）
- **合并提问**：把当前所有需要澄清的高风险点合成**一组问题，最多 3 个**，一次性问完。
- **每个问题给选项 + 默认推荐**：让用户点选而不是开放问答；标出推荐项（写明「(默认/推荐)」）和不同选择的影响。
- **在交互式环境**（如 Claude Code / 支持选项卡的客户端）优先用**结构化单/多选提问**；纯文本环境就用紧凑编号列表。
- **低风险不打断**：能用默认安全口径解决的，直接做，把假设写进输出的「口径与假设」栏，让用户事后一眼能纠。

### 提问模板（纯文本环境）
```
在取数前我需要和你确认 N 个口径点（其余我按默认处理并在结果里标注）：

1. 【指标口径】你说的“收入”是指：
   A. 核销收入 exe_income（默认/推荐，最常用经营口径）
   B. 核销GMV exe_amount（含未实收的吊牌口径）
   C. 支付GMV pay_gmv（收款口径，非核销）
2. 【时间】“最近”指：A. 近7天  B. 近30天(默认)  C. 上一个完整自然月  D. 其他（请给起止）
   并确认按 [支付日] 还是 [核销日] 统计？
3. 【范围】要 A. 全连锁整体(默认)  B. 按门店拆/某门店（请给门店）  C. 按渠道/品项拆

你可以只回复编号+字母（如 1A 2B-核销日 3A），没回的我走默认。
```

> 取数完成后，**始终在输出末尾保留「口径与假设 / 待确认」一栏**，把所有默认假设和未决项列出，方便提问者复核与回滚。

---

## 关键口径速查（覆盖约 80% 问数，免翻 reference）

**核销主表** `soyoung_dw.dm_opt_qy_user_execution_record_all_d`（过滤 `dp=CURRENT_DATE()-1 AND is_valid=1`）
- 核销GMV `SUM(exe_amount)` · 核销收入 `SUM(exe_income)` · 核销服务点 `SUM(exe_cnt)`
- 核销人数 `COUNT(DISTINCT customer_id)` · 核销人次 `COUNT(DISTINCT verify_date_id)` · 核销订单数 `COUNT(DISTINCT main_order_id)`
- 核销客单价 `SUM(exe_income)/NULLIF(COUNT(DISTINCT verify_date_id),0)`（人次口径待确认）
- 升单：`is_up=1`；升单率/加购率/渗透率见 02 复合指标完整 SQL

**支付主表** `soyoung_dw.dm_opt_qy_order_info_all_d`（过滤 `dp=CURRENT_DATE()-1 AND is_paydate_cash=0`）
- 支付GMV `SUM(pay_gmv)` · 支付订单数 `COUNT(DISTINCT main_order_id)` · 支付人数 `COUNT(DISTINCT uid)`
- 支付客单价 `SUM(pay_gmv)/NULLIF(COUNT(DISTINCT CONCAT(uid,pay_date)),0)`
- 待核销：加 `left_num>0`，待核销GMV `SUM(left_gmv)`、待核销服务点 `SUM(left_num)`

**维度过滤（实表字段名）**：新客`is_new=1`(核销)/`is_pay_new=1`(支付)；大师团`revenue_category='大师团'`；大单品/常规品`revenue_category in ('大单品','常规品')`；渠道`cx_first_channel in ('私域','公域','老带新')`；品项`standard_name REGEXP '<品项>'`；0元`exe_income=0`(核销)/`pay_gmv=0`(支付)。

**高频关联键**：`tenant_id`(门店主键，≠hospital_id) · `customer_id`≠`crm_customer_id`(需确认映射) · `order_id` vs `main_order_id`(很多口径按主单) · `product_id`≠`item_product_id` · `visit_id`(履约) · `union_id`(私域专用) · `crm_user_id`(员工)。

## 默认假设（信息不全但低风险时直接用，并在输出声明）
- 时间：默认最近一个完整统计周期（日表 T+1，`dp=CURRENT_DATE()-1`）；范围不明默认近 30 天。
- 核销默认 `is_valid=1`；支付默认 `is_paydate_cash=0`；待核销默认 `left_num>0`。
- 收入类默认给「整体」口径（含 0 元、含大师团），并提示可拆「非0元 / 非0非大师」。
- 「收入」默认按**核销收入**理解（最常用经营口径），但与支付场景冲突时必须确认。
- 维度字段名默认采用**实际 SQL 字段名**（见 04），并注明与字典登记名的差异。

## 输出格式
````markdown
**需求复述**：<一句话>

**口径卡片**
- 指标 / 定义：
- 源表：
- 必加过滤：
- 维度 / 时间：

**SQL**
```sql
<可执行 SQL>
```

**结果**（若已执行）：<数据表 / 数值。只如实呈现数据本身，不做业务解读、归因或建议>

**口径与假设 / 待确认**
- 假设：<列出所有默认假设>
- 待确认：<列出未决高风险项，或写“无”>
````
（未执行时省略「结果」；纯口语提问可只给 SQL + 假设。）

## 取数执行（可选，按部署环境）
本 Skill 默认产出 SQL；是否执行取决于部署环境：
- 若环境提供查询工具/接口（如本 Skill 自带的 `scripts/query_runner.py`、或环境已有的 SQL runner / `query_odps_dataframe` 接口 / MCP 数据工具），按「连通性测试 → 样例预览 → 正式聚合」顺序执行。
- 若无执行能力，则只产出 SQL，并提示用户在其数仓客户端运行。
- 执行细节与可移植说明见 [scripts/README.md](scripts/README.md)。
- ⚠ 只读取数。不要在取数 Skill 里执行写/删/改语句。

## Reference 地图
- [01-atomic-metrics.md](references/01-atomic-metrics.md) — 19 原子指标（定义/聚合/SQL）
- [02-derived-metrics.md](references/02-derived-metrics.md) — 132 衍生指标（索引 + 过滤模板 + 复合 SQL）
- [03-user-profile-fields.md](references/03-user-profile-fields.md) — 112 用户画像字段（用户级）
- [04-dimensions.md](references/04-dimensions.md) — 维度字典 + **字段名差异裁决**（先看这个）
- [05-tables.md](references/05-tables.md) — 49 张核心表地图 + 关联键 + 避坑
- [06-data-sources.md](references/06-data-sources.md) — 指标字典口径的底表目录
- [07-dashboard-metrics.md](references/07-dashboard-metrics.md) — 288 看板指标 → 标准口径映射
- [08-sql-conventions.md](references/08-sql-conventions.md) — 分区/过滤/时间翻译/方言/骨架
- [examples.md](references/examples.md) — NL → 澄清 → SQL 完整示例

## 底线
不臆造指标定义、字段含义、关联关系。查到的是「用公司标准口径、正确表、正确字段」的可信 SQL；不确定且影响结果时，先问清楚再取数。
