# 连锁数仓 · 库表地图（49 张核心表）

> 来源：《【经管中心】一文掌握连锁数据库表！》。取数选表的唯一权威清单。
> 分层口诀：新人优先 **DM / DWS** 宽表；只有宽表缺字段或要单笔明细时才下钻 **DWD**。

## 数仓分层

| 层级 | 名称 | 说明 |
| --- | --- | --- |
| DIM | 维度层 | 提供门店、员工、产品、活动等基础属性，是分析必备的“字典表”。 |
| DWD | 明细层 | 单笔业务事实记录（订单、核销、预约、到访…），颗粒度最细。 |
| DWS | 汇总层 | 对业务过程做轻度聚合，按门店/品项/员工等维度汇总。 |
| DM | 数据集市 | 面向分析场景的宽表，字段丰富、拿来即用，新人优先选择。 |

## 主题总览与优先级（P0 必须掌握 / P1 重点 / P2 按需）

| 主题 | 覆盖内容 | 建议主表 | 优先级 | 表数 |
| --- | --- | --- | --- | --- |
| 连锁核心 | 门店经营总览、核心收入和核销指标 | dws_opt_qy_core_summary_all_d dws_opt_qy_tenant_topic_d | P0 | 2 |
| 交易 | 支付、开单、核销、好物子单 | dm_opt_qy_order_info_all_d dm_opt_qy_user_execution_record_all_d | P0 | 7 |
| 用户 | 客户基础、生命周期、标签、回访、裂变 | dm_opt_qy_user_summary_info_all_d dim_user_qy_crm_customer_info_all_d | P0 | 7 |
| 门店 | 门店属性、机构映射、目标、资源饱和度 | dim_qy_tenant_info_all_d dws_opt_qy_tenant_topic_d | P0 | 4 |
| 产品 | 商品、品项、赛道、标准品、设备/耗材映射 | dim_opt_qy_item_product_all_d dim_product_info | P1 | 4 |
| 履约 | 预约、到访、咨询、治疗、资源占用 | dwd_opt_qy_reserve_all_d dm_opt_qy_visit_record_all_d | P1 | 5 |
| 员工 | 员工信息、产能、排班、派单、目标 | dwd_inp_qy_crm_admin_user_all_d dws_inp_qy_staff_topic_all_d | P1 | 6 |
| 私域 | 加C、加群、企微互动、私域成交 | dws_inp_private_user_union_id_topic_d dwd_inp_private_user_fact_all_d | P1 | 6 |
| 评价 | 站内评价、美团评价、口碑汇总 | dws_content_qy_evaluate_summary_all_d | P2 | 3 |
| 供应链 | 库存、出入库、进销存、高价值耗材分析 | dwd_qy_sc_product_entry_exit_detail_all_d dm_ware_tenant_stock_stats_all_d | P2 | 5 |

## 表地图详解

> ✔ TIP: 新人建议~优先使用 DM 和 DWS 层的宽表，只有当宽表缺少字段或需要单笔明细时，再下钻到 DWD 层！

### 主题：连锁核心

#### 经营总览　`dws_opt_qy_core_summary_all_d`　[DWS]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 连锁核心日统计，适合看门店、品项、渠道、员工等维度的经营表现。 |
| 核心维度 | st_day, tenant_id, customer_id, product_id, product_track, consultant_name, channel_category_name |
| 常见指标 | exe_amount, exe_income, exe_cnt, customer_is_new |
| 常用关联键 | tenant_id, customer_id, product_id |
| 推荐用法 | 做连锁整体经营盘点、赛道分析、门店对比时优先从这里起步。 |

> ⚠ WARN: 这是汇总层，不适合追单笔订单或单条核销明细。

#### 门店经营总览　`dws_opt_qy_tenant_topic_d`　[DWS]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 门店主题宽表，适合看预约、到访、治疗、员工产能、评价等门店经营指标。 |
| 核心维度 | tenant_id, tenant_name, tenant_alias_name |
| 常见指标 | income, exe_user_cnt, reserve_cnt, reserve_arrive_cnt, consultant_wait_time, treat_time |
| 常用关联键 | tenant_id |
| 推荐用法 | 做门店日报、门店健康度、区域经营复盘时直接使用。 |

> ⚠ WARN: 更偏门店经营过程，不是支付或核销底表。

### 主题：交易

#### 支付订单　`dwd_ord_order_qzy_fact_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 支付订单事实底表，是支付口径的重要源头。 |
| 核心维度 | order_id, user_id, hospital_id, pay_order_id, product_id |
| 常见指标 | gmv, is_payed, pay_date, is_used, use_date |
| 常用关联键 | order_id, user_id, hospital_id |
| 推荐用法 | 需要严格追支付过程或补支付状态字段时使用。 |

> ⚠ WARN: 字段多且偏底层，常规分析更建议先用支付主题宽表。

#### 支付主题　`dm_opt_qy_order_info_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 支付主题宽表，适合直接做 GMV、支付人数、使用情况、商品支付分析。 |
| 核心维度 | order_id, main_order_id, crm_customer_id, product_id, verify_hospital_id |
| 常见指标 | pay_gmv, is_used, pay_date, use_date |
| 常用关联键 | order_id, main_order_id, crm_customer_id, product_id |
| 推荐用法 | 做支付专题时优先用它，再按需要下钻到事实表。 |

> ⚠ WARN: 分析用户时要确认 crm_customer_id 与 customer_id 的映射关系。

#### 开单　`dwd_ord_order_store_order_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 线下开单明细，适合补充门店开单信息和业务来源。 |
| 核心维度 | order_id, store_id, customer_id, create_user_id, create_advice_id |
| 常见指标 | billing_date, order_type |
| 常用关联键 | order_id, customer_id, store_id |
| 推荐用法 | 研究开单到支付、开单到履约的链路时使用。 |

> ⚠ WARN: 和支付、核销关联时先确认主单/同步单口径。

#### 核销记录　`dwd_ord_order_qy_execution_record_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 核销主记录，适合追执行时间、服务名称、执行金额等。 |
| 核心维度 | execution_id, order_id, customer_id, clinic_id, doctor_id |
| 常见指标 | executed_time, quantity, amount |
| 常用关联键 | execution_id, order_id, customer_id |
| 推荐用法 | 做核销时间线、履约主记录分析时使用。 |

> ⚠ WARN: 明细颗粒不如 detail 表细。

#### 核销明细　`dwd_ord_order_qy_execution_record_detail_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 核销明细底表，适合看条目级金额拆分、执行员工、同步订单信息。 |
| 核心维度 | detail_id, execution_id, tenant_id, order_id, product_id, doctor_id, nurse_id, consultant_id |
| 常见指标 | quantity, amount, executed_date |
| 常用关联键 | detail_id, execution_id, order_id, tenant_id |
| 推荐用法 | 需要单条核销拆解、角色归因、订单条目追踪时使用。 |

> ⚠ WARN: 和宽表相比使用门槛更高，但明细能力最强。

#### 核销主题　`dm_opt_qy_user_execution_record_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 连锁核销主题宽表，已补用户、门店、支付、医生、咨询师等分析字段。 |
| 核心维度 | execution_id, customer_id, item_product_id, tenant_id, doctor_id, consultant_id, order_id |
| 常见指标 | exe_income, exe_amount, executed_time, pay_date |
| 常用关联键 | execution_id, order_id, main_order_id, customer_id, tenant_id |
| 推荐用法 | 做支付到核销转化、品项核销、咨询师/医生贡献分析时优先用它。 |

> ⚠ WARN: 这是最常用的核销主题表，优先级高于 DWD 明细表。

#### 有赞交易补充　`dwd_ord_order_yz_qzy_child_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 有赞子单明细，适合补充好物订单和私域成交。 |
| 核心维度 | tid, oid, sku_id, pay_time, buyer_nick |
| 常见指标 | payment, total_fee |
| 常用关联键 | tid, oid, sku_id |
| 推荐用法 | 做私域好物订单、渠道成交补充时使用。 |

> ⚠ WARN: 这是有赞体系，不要直接套用连锁门店履约口径。

### 主题：产品

#### 赛道/品项映射　`dim_opt_qy_item_product_all_d`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 商分维护的赛道和品项映射表，是连锁品项统计的重要口径表。 |
| 核心维度 | item_product_name, item_standard, market_standard, first, second, third |
| 常见指标 | 无直接指标，主要提供分类口径 |
| 常用关联键 | item_product_name |
| 推荐用法 | 做赛道、品项、标准品分析时优先接入。 |

> ⚠ WARN: 线下维护属性较多，使用前确认是否是当前生效版本。

#### 产品基础信息　`dim_product_info`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 产品基本信息表，包含菜单、品牌、价格、分类等产品属性。 |
| 核心维度 | product_id, hospital_id, brand_id, title, industrial_menu1_id, industrial_menu2_id |
| 常见指标 | price_online |
| 常用关联键 | product_id, hospital_id |
| 推荐用法 | 做产品属性分析或补品牌、分类时使用，连锁商品常加 is_qy=1 过滤。 |

> ⚠ WARN: product_id 和 item_product_id 不是一回事。

#### 品项-耗材关系　`dim_qy_product_ware_relation_all_d`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 品项与耗材关系表，用于将业务品项和供应链库存打通。 |
| 核心维度 | product_id, ware/product relation |
| 常见指标 | 无直接指标 |
| 常用关联键 | product_id, item_product_id |
| 推荐用法 | 分析核销带来的耗材消耗时使用。 |

> ⚠ WARN: 适合做专题分析，不是日常通用表。

#### 标准品映射　`dim_opt_qy_standard_product_correspondence_info`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 标准品项和商品映射关系，用于跨商品做统一归类。 |
| 核心维度 | standard product mapping |
| 常见指标 | 无直接指标 |
| 常用关联键 | product_id, item_product_id |
| 推荐用法 | 做跨门店统一品项统计时使用。 |

> ⚠ WARN: 适合解决不同门店商品命名不统一的问题。

### 主题：供应链

#### 产品维表　`dim_qy_sc_warehouse_product_info_all_d`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 资产库产品信息维表，适合看规格、单位、成本价、安全库存等。 |
| 核心维度 | product_id, item_product_id, product_name, spec, unit |
| 常见指标 | cost_price, safe_stock, initial_stock_num |
| 常用关联键 | product_id, item_product_id |
| 推荐用法 | 做库存分析、耗材成本分析时先用它补维度。 |

> ⚠ WARN: 要和业务产品表区分，供应链口径更偏资产和库存。

#### 出入库明细　`dwd_qy_sc_product_entry_exit_detail_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 出入库明细宽表，适合看采购、领用、报损、调拨等过程。 |
| 核心维度 | entry_exit_number, approval_type, approval_subtype, business_type, supplier_name, product_id |
| 常见指标 | product_quantity |
| 常用关联键 | entry_exit_number, product_id |
| 推荐用法 | 分析库存变动原因或追单据来源时使用。 |

> ⚠ WARN: 业务类型多，分析前要先过滤 approval_type/business_type。

#### 进销存汇总　`dws_qy_sc_financial_pss_stats_all_d`　[DWS]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 财务资产进销存汇总表。 |
| 核心维度 | 门店 * 批次号 |
| 常见指标 | 进销存相关汇总指标 |
| 常用关联键 | tenant_id, product_id |
| 推荐用法 | 做月度资产进销存盘点时优先使用。 |

> ⚠ WARN: 更偏财务汇总，必要时再下钻出入库明细。

#### 库存汇总　`dws_qy_sc_ware_stock_stats_all_d`　[DWS]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 高价值耗材库存和消耗汇总表。 |
| 核心维度 | tenant_id, product_id, 日期 |
| 常见指标 | 库存、消耗、周转类指标 |
| 常用关联键 | tenant_id, product_id |
| 推荐用法 | 做高价值针剂库存周转、耗用趋势时使用。 |

> ⚠ WARN: 适合高价值耗材专题，不一定覆盖全部耗材。

#### 门店库存分析　`dm_ware_tenant_stock_stats_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 门店 x 产品库存分析表，适合直接看库存结构。 |
| 核心维度 | tenant_id, product_id |
| 常见指标 | 库存、消耗、预警相关指标 |
| 常用关联键 | tenant_id, product_id |
| 推荐用法 | 给业务方做库存分析看板时优先使用。 |

> ⚠ WARN: 若要追业务单据原因，需要回到 DWD 出入库表。

### 主题：用户

#### 客户基础信息　`dim_user_qy_crm_customer_info_all_d`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | CRM 客户基础资料，包含姓名、性别、会员等级、归属员工、渠道等。 |
| 核心维度 | id/customer_id, name, mobile, membership_level, consultant_id, doctor_id, channel_name |
| 常见指标 | 无直接指标 |
| 常用关联键 | customer_id, consultant_id, doctor_id, organization_id |
| 推荐用法 | 用户分析、客户归属、会员分层时作为基础维表使用。 |

> ⚠ WARN: 字段较全，注意个人信息使用合规。

#### 用户主题　`dm_opt_qy_user_summary_info_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 用户主题宽表，适合看首单、末单、复购、生命周期、咨询师归属等。 |
| 核心维度 | crm_customer_id, organization_id, consultant_id, user_id |
| 常见指标 | first_order_date_qy, first_order_cnt_qy, last_order_date_qy, total_order_cnt_qy |
| 常用关联键 | crm_customer_id, consultant_id, organization_id |
| 推荐用法 | 做新客、老客、复购、人群分层时优先使用。 |

> ⚠ WARN: 要先确认 crm_customer_id 和 customer_id 的映射。

#### 用户标签　`dwd_opt_qy_crm_customer_customer_tag_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 用户标签关系表。 |
| 核心维度 | customer_id, tag_id |
| 常见指标 | 无直接指标 |
| 常用关联键 | customer_id, tag_id |
| 推荐用法 | 做标签人群包、活动圈选时使用。 |

> ⚠ WARN: 分析前先确认标签口径和更新时间。

#### 客户业务信息　`dwd_opt_qy_crm_customer_biz_info_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 客户业务补充信息，如备注、业务侧补充字段。 |
| 核心维度 | customer_id |
| 常见指标 | 无直接指标 |
| 常用关联键 | customer_id |
| 推荐用法 | 补充客户业务字段或运营备注时使用。 |

> ⚠ WARN: 字段业务性强，先看样例再使用。

#### 回访计划　`dwd_opt_qy_customer_followup_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 回访明细，适合看回访计划、完成情况、回访员工。 |
| 核心维度 | customer_id, followup record |
| 常见指标 | 回访状态、时间相关字段 |
| 常用关联键 | customer_id, employee_id |
| 推荐用法 | 做回访执行率、回访后转化分析时使用。 |

> ⚠ WARN: 经常需要和用户、门店、员工表联动使用。

#### 裂变活动　`dwd_opt_qy_fission_relationship_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 裂变活动关系和奖励领取明细。 |
| 核心维度 | 活动参与关系 |
| 常见指标 | 奖励领取、裂变链路相关指标 |
| 常用关联键 | customer_id, activity_id |
| 推荐用法 | 分析裂变活动效果和拉新关系时使用。 |

> ⚠ WARN: 需要联动活动维表看活动属性。

#### 活动维表　`dim_opt_qy_activity_info_all_d`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 连锁活动信息维表。 |
| 核心维度 | activity_id |
| 常见指标 | 无直接指标 |
| 常用关联键 | activity_id |
| 推荐用法 | 和裂变、营销活动分析配套使用。 |

> ⚠ WARN: 单独使用价值有限，通常做维度补充。

### 主题：评价

#### 评价明细　`dwd_content_post_qy_evaluate_detail_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 连锁评价详情，适合看评价内容、评分、来源。 |
| 核心维度 | 门店/评价明细 |
| 常见指标 | 评分、评价时间 |
| 常用关联键 | tenant_id, customer_id |
| 推荐用法 | 差评明细分析、评价内容分析时使用。 |

> ⚠ WARN: 明细较细，先按时间和门店过滤。

#### 评价汇总　`dws_content_qy_evaluate_summary_all_d`　[DWS]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 评价主题汇总表，适合看好评率、差评率、评价量。 |
| 核心维度 | tenant_id, 日期 |
| 常见指标 | 评价量、评分、好评率/差评率类指标 |
| 常用关联键 | tenant_id |
| 推荐用法 | 门店口碑分析、区域评价盘点时优先使用。 |

> ⚠ WARN: 做文本内容分析时需要下钻明细表。

#### 外部口碑　`dwd_content_meituan_evaluate_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 美团点评评价详情。 |
| 核心维度 | 门店/评价明细 |
| 常见指标 | 评分、评价时间 |
| 常用关联键 | 门店映射键 |
| 推荐用法 | 做外部平台口碑监控时使用。 |

> ⚠ WARN: 通常需要补门店映射表才能对齐连锁门店口径。

### 主题：履约

#### 预约　`dwd_opt_qy_reserve_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 连锁预约表，适合看预约时间、状态、预约来源、预约员工。 |
| 核心维度 | reserve_id, customer_id, tenant_id, employee_id |
| 常见指标 | reserve_status, start_time, end_time |
| 常用关联键 | reserve_id, customer_id, tenant_id, visit_id |
| 推荐用法 | 做预约量、预约到访转化、预约来源分析时使用。 |

> ⚠ WARN: 预约和到访并非一一对应，要结合 visit_id 和时间判断。

#### 轻自营预约　`dwd_opt_qzy_reserve_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 轻自营预约表，用于补充 qzy 预约过程。 |
| 核心维度 | reserve_id |
| 常见指标 | 预约状态相关字段 |
| 常用关联键 | reserve_id, user_id |
| 推荐用法 | 只在涉及 qzy 口径时使用。 |

> ⚠ WARN: 连锁主线分析大多优先用 qy 预约表。

#### 到访记录　`dwd_opt_qy_visit_log_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 用户到院记录明细，适合看签到、检测、咨询、治疗等全过程节点。 |
| 核心维度 | visit_id, customer_id, tenant_id, employee_id |
| 常见指标 | appointment_time, check_in_time, testing_time, consultation_time |
| 常用关联键 | visit_id, customer_id, tenant_id |
| 推荐用法 | 做到访转化、节点流转、客户到院分析时使用。 |

> ⚠ WARN: 过程字段多，先搞清楚各时间字段含义再统计。

#### 到访时长主题　`dm_opt_qy_visit_record_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 到访各节点时长宽表，适合看等待时长、咨询时长、治疗时长。 |
| 核心维度 | visit_id, customer_id |
| 常见指标 | wait_advice_time, advice_time, wait_treat_time, treat_time |
| 常用关联键 | visit_id, customer_id |
| 推荐用法 | 做履约效率、门店排队体验、流程瓶颈分析时优先用它。 |

> ⚠ WARN: 这是衍生宽表，异常值分析时要回到 visit log。

#### 资源占用　`dwd_opt_qy_crm_resources_occupy_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 资源占用表，适合算咨询/治疗资源的使用情况。 |
| 核心维度 | resource occupy record |
| 常见指标 | 占用时长相关字段 |
| 常用关联键 | tenant_id, employee_id, visit_id |
| 推荐用法 | 做资源利用率、房间/设备/人员时长分析时使用。 |

> ⚠ WARN: 通常和到访或员工排班联合分析更有价值。

### 主题：员工

#### 员工信息　`dwd_inp_qy_crm_admin_user_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | CRM 员工信息主表，包含角色、手机号、飞书账号、门店归属等。 |
| 核心维度 | crm_user_id, crm_user_name, role_name, tenant_id, sy_hospital_id |
| 常见指标 | 无直接指标 |
| 常用关联键 | crm_user_id, tenant_id, sy_hospital_id |
| 推荐用法 | 员工画像、角色分布、员工归属分析时作为基础表使用。 |

> ⚠ WARN: 咨询师、医生、护士等角色分析都要回到这张表统一身份。

#### 员工主题　`dws_inp_qy_staff_topic_all_d`　[DWS]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 员工主题汇总表，适合做员工产能、目标达成、员工表现分析。 |
| 核心维度 | 员工 * 日期/周期 |
| 常见指标 | 员工业绩和产能相关指标 |
| 常用关联键 | crm_user_id, tenant_id |
| 推荐用法 | 做咨询师、医生、护士绩效或团队表现看板时优先使用。 |

> ⚠ WARN: 具体指标口径需要结合业务说明确认。

#### 排班　`dwd_opt_qy_crm_admin_schedule_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 员工排期表。 |
| 核心维度 | 员工 * 日期/时段 |
| 常见指标 | 排班状态、班次时间 |
| 常用关联键 | employee_id, tenant_id |
| 推荐用法 | 做排班覆盖、忙闲度、服务资源保障分析时使用。 |

> ⚠ WARN: 和到访、资源占用联动价值更高。

#### 派单　`dwd_opt_qy_crm_customer_allocate_record_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 派单记录表，适合看客户如何分配给员工。 |
| 核心维度 | customer allocation record |
| 常见指标 | 派单时间、派单类型 |
| 常用关联键 | customer_id, employee_id, tenant_id |
| 推荐用法 | 做咨询师分配、客户归属流转分析时使用。 |

> ⚠ WARN: 需要确认派单场景和是否包含历史变更。

#### 目标　`dim_opt_qy_income_target_m`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 门店月度目标表。 |
| 核心维度 | tenant_id, month |
| 常见指标 | 目标值 |
| 常用关联键 | tenant_id |
| 推荐用法 | 做门店目标达成分析时使用。 |

> ⚠ WARN: 通常是线下维护数据，先确认更新及时性。

#### 员工目标　`dim_opt_qy_staff_monthly_target`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 员工月度目标表。 |
| 核心维度 | employee_id, month |
| 常见指标 | 目标值 |
| 常用关联键 | employee_id, tenant_id |
| 推荐用法 | 做员工 KPI 达成分析时使用。 |

> ⚠ WARN: 和实际产出汇总表联动使用。

### 主题：门店

#### 门店维表　`dim_qy_tenant_info_all_d`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 连锁门店信息表，包含城市、面积、床位、开业时间、阶段等。 |
| 核心维度 | tenant_id, tenant_name, city_id, city_name, area_name, sy_hospital_id |
| 常见指标 | bed_cnt, tenant_square, tenant_age |
| 常用关联键 | tenant_id, sy_hospital_id |
| 推荐用法 | 所有门店分析都建议优先接这张维表补属性。 |

> ⚠ WARN: tenant_id 才是连锁门店主键，不要直接拿 hospital_id 代替。

#### 机构维表　`dim_hospital_info`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 新氧机构维表，用于接平台机构口径。 |
| 核心维度 | hospital_id |
| 常见指标 | 机构基础属性 |
| 常用关联键 | hospital_id, sy_hospital_id |
| 推荐用法 | 当需要对接新氧平台口径时补充使用。 |

> ⚠ WARN: 与连锁门店表不是同一套主键体系。

#### 门店目标　`dim_opt_qy_hospital_income_target_m`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 连锁门店目标表。 |
| 核心维度 | tenant/hospital * month |
| 常见指标 | 目标收入 |
| 常用关联键 | tenant_id, hospital_id |
| 推荐用法 | 门店达成分析时配合门店经营表使用。 |

> ⚠ WARN: 目标口径要和实际收入表保持一致。

#### 资源饱和度　`dm_opt_qy_area_tenant_resource_stats_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 门店/大区资源饱和度分析表。 |
| 核心维度 | area, tenant |
| 常见指标 | 资源使用、饱和度类指标 |
| 常用关联键 | tenant_id, area_id |
| 推荐用法 | 做大区资源配置和门店产能预警时使用。 |

> ⚠ WARN: 更偏管理分析，先明确业务定义再解读。

### 主题：私域

#### 加C/加群明细　`dwd_inp_private_user_fact_all_d`　[DWD]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 私域加 C 和加群用户明细，是私域分析的底表。 |
| 核心维度 | union_id, external_userid, qywx_user_id, group_id, add_date |
| 常见指标 | add_c_cnt/add_group related fields |
| 常用关联键 | union_id, qywx_user_id, group_id |
| 推荐用法 | 做渠道、员工、群聊的私域新增和沉淀分析时使用。 |

> ⚠ WARN: 私域口径更多用 union_id，不要直接混用用户体系键。

#### 私域用户主题　`dws_inp_private_user_union_id_topic_d`　[DWS]

| 项 | 内容 |
| --- | --- |
| 功能说明 | union_id 粒度私域主题汇总，适合看加 C、加群、支付、转化。 |
| 核心维度 | union_id |
| 常见指标 | add_c_cnt, add_group_cnt, pay_order_gmv, qy_pay_order_gmv, qzy_pay_order_gmv |
| 常用关联键 | union_id |
| 推荐用法 | 做私域用户质量、渠道转化时优先使用。 |

> ⚠ WARN: 适合人群汇总，不适合还原逐条私聊行为。

#### 私域员工　`dim_inp_private_staff_info_all_d`　[DIM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 私域员工信息表。 |
| 核心维度 | private staff |
| 常见指标 | 无直接指标 |
| 常用关联键 | qywx_user_id, staff_id |
| 推荐用法 | 做私域员工归属和员工绩效分析时使用。 |

> ⚠ WARN: 和 CRM 员工体系可能需要映射。

#### 私域加C主题　`dm_inp_private_user_addc_fact_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 加 C 后建档、支付、互动等行为统计。 |
| 核心维度 | union_id, 渠道, 员工 |
| 常见指标 | 加 C 后支付/建档/互动相关指标 |
| 常用关联键 | union_id, qywx_user_id |
| 推荐用法 | 做私域拉新质量和加 C 后转化效率分析。 |

> ⚠ WARN: 适合效果分析，不适合还原明细路径。

#### 私域互动　`dm_inp_private_user_interact_summary_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 员工企微消息互动汇总。 |
| 核心维度 | 员工, 用户, 日期/周期 |
| 常见指标 | 消息互动相关指标 |
| 常用关联键 | union_id, qywx_user_id |
| 推荐用法 | 做员工互动效率、触达深度分析时使用。 |

> ⚠ WARN: 需结合加 C 主题或支付主题看最终转化。

#### 私域KPI　`dm_opt_private_weiban_kpi_data_all_d`　[DM]

| 项 | 内容 |
| --- | --- |
| 功能说明 | 私域 KPI 看板数据表。 |
| 核心维度 | 门店/员工/日期 |
| 常见指标 | 私域 KPI 相关指标 |
| 常用关联键 | tenant_id, qywx_user_id |
| 推荐用法 | 给业务看 KPI 或周月报时优先使用。 |

> ⚠ WARN: 更偏看板口径，异常明细需回溯明细表。

## 常用关联键速查

| 关联键 | 说明 | 使用场景 |
| --- | --- | --- |
| tenant_id | 连锁门店主键 | 几乎所有表都有，是最核心的关联键 |
| customer_id | 客户ID | 用户、交易、履约、回访等场景 |
| crm_customer_id | CRM客户ID | 和 customer_id 不一定相同，要确认映射关系 |
| order_id | 订单ID | 支付、开单、核销场景串联 |
| execution_id | 核销执行ID | 核销记录和明细之间关联 |
| visit_id | 到访ID | 预约、到访、资源占用等履约场景 |
| product_id | 商品ID | 产品、交易、供应链场景 |
| item_product_id | 品项ID | 和 product_id 不同，品项口径用这个 |
| union_id | 私域用户ID | 私域体系的核心键，不要混用其他用户键 |
| crm_user_id | 员工ID | 员工信息、产能、排班等场景 |
| sy_hospital_id | 新氧机构ID | 对接新氧平台口径时使用 |

## 注意事项与避坑指南

- ℹ NOTE: tenant_id 才是连锁门店主键，不要直接拿 hospital_id 代替。两者不是同一套体系。
- ℹ NOTE: 私域体系的核心键是 union_id，不要直接混用 customer_id 等其他用户体系的键。
- ℹ NOTE: 预约和到访并非一一对应。做转化分析时要结合 visit_id 和时间判断。
- ✔ TIP: 做供应链分析时，先过滤 approval_type 和 business_type，业务类型多且杂。
- ✔ TIP: 门店目标和员工目标通常是线下维护的数据，使用前先确认更新及时性。
- ✔ TIP: 新人分析优先用 DM 和 DWS 层的宽表。只有当宽表缺少字段或需要明细时，再下钻到 DWD 层。
- ⚠ WARN: 有赞体系的订单不能直接套用连锁门店履约口径。分析时要区分数据来源。
- ⚠ WARN: 个人信息使用要注意合规。客户基础信息表中包含敏感字段，取数时注意脱敏。
- ⚠ WARN: crm_customer_id 和 customer_id 不一定相同。做用户分析时一定要先确认映射关系。
- ⚠ WARN: product_id 和 item_product_id 是两个不同的 ID 体系。产品表和品项表关联时要区分清楚。
