# 用户画像字段（112 个 · 用户级）

> 来源：指标字典 · 用户画像字段 sheet。这些是**用户级**字段（一个用户一行），用于人群圈选 / 用户分层 / 画像。
> 多数来自 `dwd_ord_order_qzy_fact_all_d`，含首单/末单/累计 × 线上/线下/医美/好物 等切片，普遍用 `DENSE_RANK() OVER(PARTITION BY user_id ORDER BY pay_date)` 取首末。

## 全量索引

| ID | 字段名称 | 板块 | 子分类 | 粒度 | 数据类型 | 源表 | 定义 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U001 | 连锁首单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户的首单支付日期 |
| U002 | 连锁首日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户首次支付当天的订单量 |
| U003 | 连锁首日订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户首次支付当天的支付金额gmv |
| U004 | 连锁首日支付品项数 | 用户板块 | 支付 | 用户级 | VARCHAR | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户首次支付当天的支付品项数 |
| U005 | 连锁首日支付品项的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户首次支付当天的支付品项列表 |
| U006 | 连锁最近订单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户末次订单的支付日期 |
| U007 | 连锁最近一天日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户末次支付当天的订单量 |
| U008 | 连锁最近一天日订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户末次支付当天的支付金额gmv |
| U009 | 连锁最近一天日支付品项数 | 用户板块 | 支付 | 用户级 | VARCHAR | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户末次支付当天的支付品项数 |
| U010 | 连锁最近一天日支付品项的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户末次支付当天的支付品项列表 |
| U011 | 连锁累计订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户累计支付的订单量 |
| U012 | 连锁累计订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户累计支付的支付金额gmv |
| U013 | 连锁累计支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户累计支付的支付品项数 |
| U014 | 连锁累计支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁用户累计支付的支付品项列表 |
| U015 | 连锁线上首单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户的首单支付日期 |
| U016 | 连锁线上首日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户首次支付当天的订单量 |
| U017 | 连锁线上首日订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户首次支付当天的支付金额gmv |
| U018 | 连锁线上首日支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户首次支付当天的支付品项数 |
| U019 | 连锁线上首日支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户首次支付当天的支付品项列表 |
| U020 | 连锁线上最近订单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户末次订单的支付日期 |
| U021 | 连锁线上最近一天日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户末次支付当天的订单量 |
| U022 | 连锁线上最近一天日订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户末次支付当天的支付金额gmv |
| U023 | 连锁线上最近一天日支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户末次支付当天的支付品项数 |
| U024 | 连锁线上最近一天日支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户末次支付当天的支付品项列表 |
| U025 | 连锁线上累计订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户累计支付的订单量 |
| U026 | 连锁线上累计订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户累计支付的支付金额gmv |
| U027 | 连锁线上累计支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户累计支付的支付品项数 |
| U028 | 连锁线上累计支付项目list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线上用户累计支付的支付品项列表 |
| U029 | 连锁线下首单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户的首单支付日期 |
| U030 | 连锁线下首日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户首次支付当天的订单量 |
| U031 | 连锁线下首日订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户首次支付当天的支付金额gmv |
| U032 | 连锁线下首日支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户首次支付当天的支付品项数 |
| U033 | 连锁线下首日支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户首次支付当天的支付品项列表 |
| U034 | 连锁线下最近订单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户末次订单的支付日期 |
| U035 | 连锁线下最近一天日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户末次支付当天的订单量 |
| U036 | 连锁线下最近一天日订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户末次支付当天的支付金额gmv |
| U037 | 连锁线下最近一天日支付spu数 | 用户板块 | 支付 | 用户级 | VARCHAR | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户末次支付当天的支付品项数 |
| U038 | 连锁线下最近一天日支付spu的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户末次支付当天的支付品项列表 |
| U039 | 连锁线下累计订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户累计支付的订单量 |
| U040 | 连锁线下累计订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户累计支付的支付金额gmv |
| U041 | 连锁线下累计支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户累计支付的支付品项数 |
| U042 | 连锁线下累计支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 每个连锁线下用户累计支付的支付品项列表 |
| U043 | 医美首单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域的首单支付日期 |
| U044 | 医美首日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域的首次支付当天的订单量 |
| U045 | 医美首日订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域首次支付当天的支付金额gmv |
| U046 | 医美首日支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域首次支付当天的支付品项数 |
| U047 | 医美首日支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域首次支付当天的支付品项列表 |
| U048 | 医美最近一次订单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域末次订单的支付日期 |
| U049 | 医美最近一天日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域末次支付当天的订单量 |
| U050 | 医美最近一天日订单支付支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域末次支付当天的支付金额gmv |
| U051 | 医美最近一天日支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域末次支付当天的支付品项数 |
| U052 | 医美最近一天日支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域末次支付当天的支付品项列表 |
| U053 | 医美累计订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域累计支付的订单量 |
| U054 | 医美累计订单支付支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域累计支付的订单金额gmv |
| U055 | 医美累计支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域累计支付的项目数 |
| U056 | 医美累计支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在医美领域累计支付项目的list |
| U057 | 好物首单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域的首单支付日期 |
| U058 | 好物首日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域的首次支付当天的订单量 |
| U059 | 好物首日订单支付支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域首次支付当天的支付金额gmv |
| U060 | 好物首日支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域首次支付当天的支付品项数 |
| U061 | 好物首日支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域首次支付当天的支付品项列表 |
| U062 | 好物最近一次订单日期 | 用户板块 | 支付 | 用户级 | DATE | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域末次订单的支付日期 |
| U063 | 好物最近一天日订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域末次支付当天的订单量 |
| U064 | 好物最近一天日订单支付支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域末次支付当天的支付金额gmv |
| U065 | 好物最近一天日支付spu数 | 用户板块 | 支付 | 用户级 | VARCHAR | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域末次支付当天的支付品项数 |
| U066 | 好物最近一天日支付spu的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域末次支付当天的支付品项列表 |
| U067 | 好物累计订单数量 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域累计支付的订单量 |
| U068 | 好物累计订单支付金额gmv | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域累计支付的订单金额gmv |
| U069 | 好物累计支付项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域累计支付的项目数 |
| U070 | 好物累计支付项目的list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 连锁用户在好物领域累计支付项目的list |
| U071 | 实际支付GMV，剔除退款，换购，转增 | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 剔除退款，换购，转增后，用户的实际支付gmv |
| U072 | 实际支付项目list剔除退款，换购，转增 | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 剔除退款，换购，转增后，用户的实际支付项目list |
| U073 | 实际支付订单数，剔除剔除退款，换购，转增 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 剔除退款，换购，转增后，用户的实际支付订单数 |
| U074 | 待核销订单数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 用户购买后还未核销的订单数 |
| U075 | 待核销订单金额 | 用户板块 | 支付 | 用户级 | DECIMAL | `dwd_ord_order_qzy_fact_all_d` | 用户购买后还未核销的订单金额gmv |
| U076 | 待核销项目数 | 用户板块 | 支付 | 用户级 | INT | `dwd_ord_order_qzy_fact_all_d` | 用户购买后还未核销的项目数 |
| U077 | 待核销项目list | 用户板块 | 支付 | 用户级 | STRING/ARRAY | `dwd_ord_order_qzy_fact_all_d` | 用户购买后还未核销的项目列表 |
| U078 | 首次核销日期 | 用户板块 | 核销 | 用户级 | DATE | `dwd_ord_order_qy_execution_record_all_d` | 用户的首次核销日期 |
| U079 | 首次核销gmv | 用户板块 | 核销 | 用户级 | DECIMAL | `dwd_ord_order_qy_execution_record_all_d` | 用户的首次核销金额gmv |
| U080 | 首次核销收入（不含税gmv/1.06） | 用户板块 | 核销 | 用户级 | DECIMAL | `dwd_ord_order_qy_execution_record_all_d` | 用户的首次核销收入 |
| U081 | 首次核销服务点数 | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户的首次核销的服务点数 |
| U082 | 首次核销项目数 | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户首次核销的项目数 |
| U083 | 首次核销项目数的list | 用户板块 | 核销 | 用户级 | STRING/ARRAY | `dwd_ord_order_qy_execution_record_all_d` | 用户首次核销的项目数的list |
| U084 | 最近一次核销日期 | 用户板块 | 核销 | 用户级 | DATE | `dwd_ord_order_qy_execution_record_all_d` | 用户的末次核销日期 |
| U085 | 最近一次核销gmv | 用户板块 | 核销 | 用户级 | DECIMAL | `dwd_ord_order_qy_execution_record_all_d` | 用户的末次核销金额gmv |
| U086 | 最近一次核销收入（不含税 | 用户板块 | 核销 | 用户级 | DECIMAL | `dwd_ord_order_qy_execution_record_all_d` | 用户的末次核销收入 |
| U087 | 最近一次核销服务点数 | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户的末次核销的服务点数 |
| U088 | 最近一次核销项目数 | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户末次核销的项目数 |
| U089 | 最近一次核销项目list | 用户板块 | 核销 | 用户级 | STRING/ARRAY | `dwd_ord_order_qy_execution_record_all_d` | 用户末次核销的项目数的list |
| U090 | 累计核销gmv | 用户板块 | 核销 | 用户级 | DECIMAL | `dwd_ord_order_qy_execution_record_all_d` | 用户的累计核销金额gmv |
| U091 | 累计核销收入（不含税gmv/1.06） | 用户板块 | 核销 | 用户级 | DECIMAL | `dwd_ord_order_qy_execution_record_all_d` | 用户的累计核销收入 |
| U092 | 累计核销服务点数 | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户的累计核销服务点数 |
| U093 | 累计核销项目数 | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户的累计核销项目数 |
| U094 | 累计核销项目list | 用户板块 | 核销 | 用户级 | STRING/ARRAY | `dwd_ord_order_qy_execution_record_all_d` | 用户的累计核销的项目list |
| U095 | 非本月末次核销时间 | 用户板块 | 核销 | 用户级 | VARCHAR | `dwd_ord_order_qy_execution_record_all_d` | 用户在当前月之前的末次核销日期 |
| U096 | 累计核销次数（按天去重） | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户的累计核销次数（同一天多次核销算一次） |
| U097 | 非本月累计核销次数（按天去重） | 用户板块 | 核销 | 用户级 | INT | `dwd_ord_order_qy_execution_record_all_d` | 用户非本月的累计核销次数（同一天多次核销算一次） |
| U098 | 大师团核销gmv | 用户板块 | 核销 | 用户级 | DECIMAL | `dwd_ord_order_qy_execution_record_all_d` | 用户在大师团核销的gmv |
| U099 | 是否私域用户 | 用户板块 | 加c | 用户级 | BOOLEAN | `dwd_inp_private_user_fact_all_d` | 是否私域用户 |
| U100 | 是否私域账号有效加c | 用户板块 | 加c | 用户级 | BOOLEAN | `dwd_inp_private_user_fact_all_d` | 是否私域账号有效加c |
| U101 | 是否网咨账号有效加c | 用户板块 | 加c | 用户级 | BOOLEAN | `dwd_inp_private_user_fact_all_d` | 是否网咨账号有效加c |
| U102 | 是否门店咨询账号有效加c | 用户板块 | 加c | 用户级 | BOOLEAN | `dwd_inp_private_user_fact_all_d` | 是否门店咨询账号有效加c |
| U103 | 是否加群 | 用户板块 | 加c | 用户级 | BOOLEAN | `dwd_inp_private_user_fact_all_d` | 是否加群 |
| U104 | app首次登陆日期 | 用户板块 | 小程序 | 用户级 | DATE | `dwd_md_xcx_all_log_d` | 用户首次登陆app的日期 |
| U105 | app末次登陆日期 | 用户板块 | 小程序 | 用户级 | DATE | `dwd_md_xcx_all_log_d` | 用户末次登陆app的日期 |
| U106 | app近30天活跃天数 | 用户板块 | 小程序 | 用户级 | INT | `dwd_md_xcx_all_log_d` | 用户近30天在app的活跃天数 |
| U107 | 小程序首次登陆日期 | 用户板块 | 小程序 | 用户级 | DATE | `dwd_md_xcx_all_log_d` | 用户首次登陆小程序的日期 |
| U108 | 小程序末次登陆日期 | 用户板块 | 小程序 | 用户级 | DATE | `dwd_md_xcx_all_log_d` | 用户末次登陆小程序的日期 |
| U109 | 小程序近30天活跃天数 | 用户板块 | 小程序 | 用户级 | INT | `dwd_md_xcx_all_log_d` | 用户近30天在小程序的活跃天数 |
| U110 | 最近有效预约日期 | 用户板块 | 预约 | 用户级 | DATE | `dwd_opt_qy_reserve_all_d` | 用户最近的有效预约日期 |
| U111 | 最近有效预约订单list | 用户板块 | 预约 | 用户级 | STRING/ARRAY | `dwd_opt_qy_reserve_all_d` | 用户最近的有效预约订单列表 |
| U112 | 最近有效预约gmv | 用户板块 | 预约 | 用户级 | DECIMAL | `dwd_opt_qy_reserve_all_d` | 用户最近的有效预约订单的订单金额gmv |

## 完整 SQL（逐字段）

字段高度模板化（首/末/累计 × 线上 `app_id<>126` / 线下 `app_id=126` / 医美 `track<>'好物'` / 好物）。完整 SQL 如下：

### U001 连锁首单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户的首单支付日期

```sql
SELECT  DISTINCT a.user_id
        ,SUBSTR(a.pay_date,1,10) 连锁首单日期
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) a
WHERE   a.rn = 1
;
```

### U002 连锁首日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户首次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 连锁首日订单数量
FROM    (
            SELECT  main_order_id
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U003 连锁首日订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户首次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 连锁首日订单支付金额gmv
FROM    (
            SELECT  pay_gmv
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U004 连锁首日支付品项数
- 用户板块 / 支付 · 用户级 · VARCHAR　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户首次支付当天的支付品项数

```sql
SELECT  d.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁首日支付品项数
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U005 连锁首日支付品项的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户首次支付当天的支付品项列表

```sql
SELECT  d.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁首日支付品项的list
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U006 连锁最近订单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户末次订单的支付日期

```sql
SELECT  DISTINCT a.user_id
        ,SUBSTR(a.pay_date,1,10) 连锁最近订单日期
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) a
WHERE   a.rn = 1
;
```

### U007 连锁最近一天日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户末次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 连锁最近一天日订单数量
FROM    (
            SELECT  main_order_id
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U008 连锁最近一天日订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户末次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 连锁最近一天日订单支付金额gmv
FROM    (
            SELECT  pay_gmv
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U009 连锁最近一天日支付品项数
- 用户板块 / 支付 · 用户级 · VARCHAR　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户末次支付当天的支付品项数

```sql
SELECT  d.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁最近一天日支付品项数
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U010 连锁最近一天日支付品项的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户末次支付当天的支付品项列表

```sql
SELECT  d.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁最近一天日支付品项的list
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U011 连锁累计订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户累计支付的订单量

```sql
SELECT  user_id
        ,COUNT(DISTINCT main_order_id) 连锁累计订单数量
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,0)
AND     is_ass_hospital = 1
AND     is_payed = 1
GROUP BY user_id
;
```

### U012 连锁累计订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户累计支付的支付金额gmv

```sql
SELECT  user_id
        ,SUM(pay_gmv) 连锁累计订单支付金额gmv
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,0)
AND     is_ass_hospital = 1
AND     is_payed = 1
GROUP BY user_id
;
```

### U013 连锁累计支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户累计支付的支付品项数

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁累计支付项目数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info c
ON      a.pid = c.product_id
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.dp = CURRENT_DATE() - 1
AND     c.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
GROUP BY a.user_id
;
```

### U014 连锁累计支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁用户累计支付的支付品项列表

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁累计支付项目的list
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info c
ON      a.pid = c.product_id
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.dp = CURRENT_DATE() - 1
AND     c.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
GROUP BY a.user_id
;
```

### U015 连锁线上首单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户的首单支付日期

```sql
SELECT  DISTINCT a.user_id
        ,SUBSTR(a.pay_date,1,10) 连锁线上首单日期
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) a
WHERE   a.rn = 1
;
```

### U016 连锁线上首日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户首次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 连锁线上首日订单数量
FROM    (
            SELECT  main_order_id
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U017 连锁线上首日订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户首次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 连锁线上首日订单支付金额gmv
FROM    (
            SELECT  pay_gmv
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U018 连锁线上首日支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户首次支付当天的支付品项数

```sql
SELECT  d.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁线上首日支付品项数
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U019 连锁线上首日支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户首次支付当天的支付品项列表

```sql
SELECT  d.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁线上首日支付品项的list
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U020 连锁线上最近订单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户末次订单的支付日期

```sql
SELECT  DISTINCT a.user_id
        ,SUBSTR(a.pay_date,1,10) 连锁线上最近订单日期
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) a
WHERE   a.rn = 1
;
```

### U021 连锁线上最近一天日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户末次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 连锁线上最近一天日订单数量
FROM    (
            SELECT  main_order_id
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U022 连锁线上最近一天日订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户末次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 连锁线上最近一天日订单支付金额gmv
FROM    (
            SELECT  pay_gmv
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U023 连锁线上最近一天日支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户末次支付当天的支付品项数

```sql
SELECT  d.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁线上最近一天日支付品项数
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U024 连锁线上最近一天日支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户末次支付当天的支付品项列表

```sql
SELECT  d.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁线上最近一天日支付品项的list
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id <> 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U025 连锁线上累计订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户累计支付的订单量

```sql
SELECT  user_id
        ,COUNT(DISTINCT main_order_id) 连锁线上累计订单数量
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,0)
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     app_id <> 126
GROUP BY user_id
;
```

### U026 连锁线上累计订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户累计支付的支付金额gmv

```sql
SELECT  user_id
        ,SUM(pay_gmv) 连锁线上累计订单支付金额gmv
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,0)
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     app_id <> 126
GROUP BY user_id
;
```

### U027 连锁线上累计支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户累计支付的支付品项数

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁线上累计支付项目数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info c
ON      a.pid = c.product_id
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.dp = CURRENT_DATE() - 1
AND     c.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.app_id <> 126
GROUP BY a.user_id
;
```

### U028 连锁线上累计支付项目list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线上用户累计支付的支付品项列表

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁线上累计支付项目的list
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info c
ON      a.pid = c.product_id
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.dp = CURRENT_DATE() - 1
AND     c.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.app_id <> 126
GROUP BY a.user_id
;
```

### U029 连锁线下首单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户的首单支付日期

```sql
SELECT  DISTINCT a.user_id
        ,SUBSTR(a.pay_date,1,10) 连锁线下首单日期
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) a
WHERE   a.rn = 1
;
```

### U030 连锁线下首日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户首次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 连锁线下首日订单数量
FROM    (
            SELECT  main_order_id
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U031 连锁线下首日订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户首次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 连锁线下首日订单支付金额gmv
FROM    (
            SELECT  pay_gmv
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U032 连锁线下首日支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户首次支付当天的支付品项数

```sql
SELECT  d.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁线下首日支付品项数
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U033 连锁线下首日支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户首次支付当天的支付品项列表

```sql
SELECT  d.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁线下首日支付品项的list
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U034 连锁线下最近订单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户末次订单的支付日期

```sql
SELECT  DISTINCT a.user_id
        ,SUBSTR(a.pay_date,1,10) 连锁线下最近订单日期
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) a
WHERE   a.rn = 1
;
```

### U035 连锁线下最近一天日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户末次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 连锁线下最近一天日订单数量
FROM    (
            SELECT  main_order_id
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U036 连锁线下最近一天日订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户末次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 连锁线下最近一天日订单支付金额gmv
FROM    (
            SELECT  pay_gmv
                    ,user_id
                    ,pay_date
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS a
WHERE   rn = 1
GROUP BY user_id
;
```

### U037 连锁线下最近一天日支付spu数
- 用户板块 / 支付 · 用户级 · VARCHAR　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户末次支付当天的支付品项数

```sql
SELECT  d.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁线下最近一天日支付品项数
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U038 连锁线下最近一天日支付spu的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户末次支付当天的支付品项列表

```sql
SELECT  d.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁线下最近一天日支付品项的list
FROM    (
            SELECT  pay_date
                    ,user_id
                    ,pid
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     bus_type IN ('新氧优享','连锁')
            AND     pay_date != COALESCE(cash_back_date,0)
            AND     is_ass_hospital = 1
            AND     is_payed = 1
            AND     app_id = 126
        ) AS d
LEFT JOIN soyoung_dw.dim_product_info c
ON      c.product_id = d.pid
AND     c.dp = CURRENT_DATE() - 1
WHERE   d.rn = 1
GROUP BY d.user_id
;
```

### U039 连锁线下累计订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户累计支付的订单量

```sql
SELECT  user_id
        ,COUNT(DISTINCT main_order_id) 连锁线下累计订单数量
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,0)
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     app_id = 126
GROUP BY user_id
;
```

### U040 连锁线下累计订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户累计支付的支付金额gmv

```sql
SELECT  user_id
        ,SUM(pay_gmv) 连锁线下累计订单支付金额gmv
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,0)
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     app_id = 126
GROUP BY user_id
;
```

### U041 连锁线下累计支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户累计支付的支付品项数

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT c.standard_name) AS 连锁线下累计支付项目数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info c
ON      a.pid = c.product_id
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.dp = CURRENT_DATE() - 1
AND     c.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.app_id = 126
GROUP BY a.user_id
;
```

### U042 连锁线下累计支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：每个连锁线下用户累计支付的支付品项列表

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 连锁线下累计支付项目的list
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info c
ON      a.pid = c.product_id
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.dp = CURRENT_DATE() - 1
AND     c.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.app_id = 126
GROUP BY a.user_id
;
```

### U043 医美首单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域的首单支付日期

```sql
SELECT  DISTINCT a.user_id
        ,a.pay_date AS 医美首单日期
FROM    (
            SELECT  DISTINCT pay_date
                    ,pid
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
;
```

### U044 医美首日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域的首次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT main_order_id) AS 医美首日订单数量
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
;
```

### U045 医美首日订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域首次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(pay_gmv) AS 医美首日订单支付支付金额gmv
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U046 医美首日支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域首次支付当天的支付品项数

```sql
SELECT  a.user_id
        ,COUNT(b.standard_name) AS 医美首日支付项目数
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U047 医美首日支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域首次支付当天的支付品项列表

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT b.standard_name) AS 医美首日支付项目的list
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U048 医美最近一次订单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域末次订单的支付日期

```sql
SELECT  DISTINCT a.user_id
        ,a.pay_date AS 医美最近一次订单日期
FROM    (
            SELECT  DISTINCT pay_date
                    ,pid
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
;
```

### U049 医美最近一天日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域末次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT main_order_id) AS 医美最近一天日订单数量
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
;
```

### U050 医美最近一天日订单支付支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域末次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(pay_gmv) AS 医美最近一天日订单支付金额gmv
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U051 医美最近一天日支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域末次支付当天的支付品项数

```sql
SELECT  a.user_id
        ,COUNT(b.standard_name) AS 医美最近一天日支付项目数
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U052 医美最近一天日支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域末次支付当天的支付品项列表

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT b.standard_name) AS 医美最近一天日支付项目的list
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     (
                        b.track <> '好物'
                        OR      b.track IS NULL
            )
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U053 医美累计订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域累计支付的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 医美累计订单数量
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     (
            b.track <> '好物'
            OR      b.track IS NULL
)
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U054 医美累计订单支付支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域累计支付的订单金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 医美累计订单支付支付金额gmv
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     (
            b.track <> '好物'
            OR      b.track IS NULL
)
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U055 医美累计支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域累计支付的项目数

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT b.standard_name) AS 医美累计支付项目数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     (
            b.track <> '好物'
            OR      b.track IS NULL
)
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U056 医美累计支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在医美领域累计支付项目的list

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT b.standard_name) AS 医美累计支付项目的list
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     (
            b.track <> '好物'
            OR      b.track IS NULL
)
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U057 好物首单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域的首单支付日期

```sql
SELECT  DISTINCT a.user_id
        ,a.pay_date AS 好物首单日期
FROM    (
            SELECT  DISTINCT pay_date
                    ,pid
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
;
```

### U058 好物首日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域的首次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT main_order_id) AS 好物首日订单数量
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
;
```

### U059 好物首日订单支付支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域首次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(pay_gmv) AS 好物首日订单支付支付金额gmv
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U060 好物首日支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域首次支付当天的支付品项数

```sql
SELECT  a.user_id
        ,COUNT(b.standard_name) AS 好物首日支付项目数
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U061 好物首日支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域首次支付当天的支付品项列表

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT b.standard_name) AS 好物首日支付项目的list
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U062 好物最近一次订单日期
- 用户板块 / 支付 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域末次订单的支付日期

```sql
SELECT  DISTINCT a.user_id
        ,a.pay_date AS 好物最近一次订单日期
FROM    (
            SELECT  DISTINCT pay_date
                    ,pid
                    ,user_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
;
```

### U063 好物最近一天日订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域末次支付当天的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT main_order_id) AS 好物最近一天日订单数量
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
;
```

### U064 好物最近一天日订单支付支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域末次支付当天的支付金额gmv

```sql
SELECT  a.user_id
        ,SUM(pay_gmv) AS 好物最近一天日订单支付金额gmv
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U065 好物最近一天日支付spu数
- 用户板块 / 支付 · 用户级 · VARCHAR　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域末次支付当天的支付品项数

```sql
SELECT  a.user_id
        ,COUNT(b.standard_name) AS 好物最近一天日支付项目数
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U066 好物最近一天日支付spu的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域末次支付当天的支付品项列表

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT b.standard_name) AS 好物最近一天日支付项目的list
FROM    (
            SELECT  DISTINCT pay_date
                    ,user_id
                    ,pid
                    ,main_order_id
                    ,pay_gmv
                    ,b.standard_name
                    ,DENSE_RANK() OVER (PARTITION BY user_id ORDER BY pay_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
            LEFT JOIN    soyoung_dw.dim_product_info b
            ON      a.pid = b.product_id
            AND     b.dp = CURRENT_DATE() - 1
            AND     b.track = '好物'
            WHERE   a.dp = CURRENT_DATE() - 1
            AND     a.bus_type IN ('新氧优享','连锁')
            AND     a.pay_date != COALESCE(cash_back_date,0)
            AND     a.is_ass_hospital = 1
            AND     a.is_payed = 1
        ) a
WHERE   a.rn = 1
GROUP BY a.user_id
```

### U067 好物累计订单数量
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域累计支付的订单量

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT a.main_order_id) AS 好物累计订单数量
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     b.track = '好物'
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U068 好物累计订单支付金额gmv
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域累计支付的订单金额gmv

```sql
SELECT  a.user_id
        ,SUM(a.pay_gmv) AS 好物累计订单支付支付金额gmv
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     b.track = '好物'
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U069 好物累计支付项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域累计支付的项目数

```sql
SELECT  a.user_id
        ,COUNT(DISTINCT b.standard_name) AS 好物累计支付项目数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     b.track = '好物'
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U070 好物累计支付项目的list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：连锁用户在好物领域累计支付项目的list

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT b.standard_name) AS 好物累计支付项目的list
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info b
ON      a.pid = b.product_id
AND     b.track = '好物'
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.dp = CURRENT_DATE() - 1
AND     b.dp = CURRENT_DATE() - 1
GROUP BY a.user_id
;
```

### U071 实际支付GMV，剔除退款，换购，转增
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：剔除退款，换购，转增后，用户的实际支付gmv

```sql
SELECT  user_id
        ,SUM(pay_gmv) AS 实际支付GMV
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     cash_back_date IS NULL
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     transaction_type = 1
GROUP BY user_id
;
```

### U072 实际支付项目list剔除退款，换购，转增
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：剔除退款，换购，转增后，用户的实际支付项目list

```sql
SELECT  a.user_id
        ,COLLECT_SET(DISTINCT c.standard_name) AS 实际支付项目的list
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_product_info c
ON      a.pid = c.product_id
AND     c.dp = CURRENT_DATE() - 1
WHERE   a.bus_type IN ('新氧优享','连锁')
AND     a.dp = CURRENT_DATE() - 1
AND     cash_back_date IS NULL
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     a.transaction_type = 1
GROUP BY a.user_id
;
```

### U073 实际支付订单数，剔除剔除退款，换购，转增
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：剔除退款，换购，转增后，用户的实际支付订单数

```sql
SELECT  user_id
        ,COUNT(DISTINCT main_order_id) AS 实际支付订单数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     cash_back_date IS NULL
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     transaction_type = 1
GROUP BY user_id
;
```

### U074 待核销订单数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：用户购买后还未核销的订单数

```sql
SELECT  crm_customer_id
        ,COUNT(DISTINCT main_order_id) AS 待核销订单数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,'0')
AND     cash_back_date IS NULL
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     left_num > 0
GROUP BY crm_customer_id
;
```

### U075 待核销订单金额
- 用户板块 / 支付 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：用户购买后还未核销的订单金额gmv

```sql
SELECT  crm_customer_id
        ,SUM(pay_gmv) AS 待核销订单金额
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     bus_type IN ('新氧优享','连锁')
AND     pay_date != COALESCE(cash_back_date,'0')
AND     cash_back_date IS NULL
AND     is_ass_hospital = 1
AND     is_payed = 1
AND     left_num > 0
GROUP BY crm_customer_id
;
```

### U076 待核销项目数
- 用户板块 / 支付 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：用户购买后还未核销的项目数

```sql
SELECT  crm_customer_id
        ,COUNT(DISTINCT s.standard_commodity) 待核销项目数
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_qy_sku_market_temp_all s
ON      a.pid = s.sku_id
WHERE   a.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.cash_back_date IS NULL
AND     a.bus_type IN ('新氧优享','连锁')
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     left_num > 0
GROUP BY crm_customer_id
;
```

### U077 待核销项目list
- 用户板块 / 支付 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qzy_fact_all_d`
- 定义：用户购买后还未核销的项目列表

```sql
SELECT  crm_customer_id
        ,COLLECT_SET(s.standard_commodity) 待核销项目list
FROM    soyoung_dw.dwd_ord_order_qzy_fact_all_d a
LEFT JOIN soyoung_dw.dim_qy_sku_market_temp_all s
ON      a.pid = s.sku_id
WHERE   a.dp = CURRENT_DATE() - 1
AND     a.pay_date != COALESCE(a.cash_back_date,0)
AND     a.cash_back_date IS NULL
AND     a.bus_type IN ('新氧优享','连锁')
AND     a.is_ass_hospital = 1
AND     a.is_payed = 1
AND     left_num > 0
GROUP BY crm_customer_id
;
```

### U078 首次核销日期
- 用户板块 / 核销 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的首次核销日期

```sql
SELECT  DISTINCT a.executed_date 首次核销日期
        ,crm_customer_id
FROM    (
            SELECT  DISTINCT executed_date
                    ,crm_customer_id
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
;
```

### U079 首次核销gmv
- 用户板块 / 核销 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的首次核销金额gmv

```sql
SELECT  SUM(amount) 首次核销gmv
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,amount
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U080 首次核销收入（不含税gmv/1.06）
- 用户板块 / 核销 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的首次核销收入

```sql
SELECT  SUM(amount / 1.06) 首次核销收入
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,amount
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U081 首次核销服务点数
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的首次核销的服务点数

```sql
SELECT  COUNT(exe_cnt) 首次核销服务点数
        ,customer_id
FROM    (
            SELECT  exe_cnt
                    ,customer_id
                    ,DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY st_day ASC ) AS rn
            FROM    soyoung_dw.dws_opt_qy_core_summary_all_d a
            WHERE   dp = CURRENT_DATE() - 1
        ) a
WHERE   a.rn = 1
GROUP BY customer_id
;
```

### U082 首次核销项目数
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户首次核销的项目数

```sql
SELECT  COUNT(DISTINCT product_id) 首次核销项目数
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,product_id
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U083 首次核销项目数的list
- 用户板块 / 核销 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户首次核销的项目数的list

```sql
SELECT  COLLECT_SET(DISTINCT a.item_product_name) 首次核销项目list
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,item_product_name
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date ASC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U084 最近一次核销日期
- 用户板块 / 核销 · 用户级 · DATE　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的末次核销日期

```sql
SELECT  DISTINCT a.executed_date 最近一次核销日期
        ,crm_customer_id
FROM    (
            SELECT  DISTINCT executed_date
                    ,crm_customer_id
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
;
```

### U085 最近一次核销gmv
- 用户板块 / 核销 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的末次核销金额gmv

```sql
SELECT  SUM(amount) 最近一次核销gmv
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,amount
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U086 最近一次核销收入（不含税
- 用户板块 / 核销 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的末次核销收入

```sql
SELECT  SUM(amount / 1.06) 最近一次核销收入
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,amount
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U087 最近一次核销服务点数
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的末次核销的服务点数

```sql
SELECT  COUNT(exe_cnt) 最近一次核销服务点数
        ,customer_id
FROM    (
            SELECT  exe_cnt
                    ,customer_id
                    ,DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY st_day DESC ) AS rn
            FROM    soyoung_dw.dws_opt_qy_core_summary_all_d a
            WHERE   dp = CURRENT_DATE() - 1
        ) a
WHERE   a.rn = 1
GROUP BY customer_id
;
```

### U088 最近一次核销项目数
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户末次核销的项目数

```sql
SELECT  COUNT(DISTINCT product_id) 最近一次核销项目数
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,product_id
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U089 最近一次核销项目list
- 用户板块 / 核销 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户末次核销的项目数的list

```sql
SELECT  COLLECT_SET(DISTINCT a.item_product_name) 最近一次核销项目list
        ,crm_customer_id
FROM    (
            SELECT  crm_customer_id
                    ,item_product_name
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d a
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
        ) a
WHERE   a.rn = 1
GROUP BY crm_customer_id
;
```

### U090 累计核销gmv
- 用户板块 / 核销 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的累计核销金额gmv

```sql
SELECT  crm_customer_id
        ,SUM(amount) AS 累计核销gmv
FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     is_valid = 1
GROUP BY crm_customer_id
;
```

### U091 累计核销收入（不含税gmv/1.06）
- 用户板块 / 核销 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的累计核销收入

```sql
SELECT  crm_customer_id
        ,SUM(amount / 1.06) AS 累计核销收入
FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     is_valid = 1
GROUP BY crm_customer_id
;
```

### U092 累计核销服务点数
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的累计核销服务点数

```sql
SELECT  COUNT(exe_cnt) 累计核销服务点数
        ,customer_id
FROM    soyoung_dw.dws_opt_qy_core_summary_all_d
WHERE   dp = CURRENT_DATE() - 1
GROUP BY customer_id
;
```

### U093 累计核销项目数
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的累计核销项目数

```sql
SELECT  crm_customer_id
        ,COUNT(DISTINCT product_id) 累计核销项目数
FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     is_valid = 1
GROUP BY crm_customer_id
;
```

### U094 累计核销项目list
- 用户板块 / 核销 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的累计核销的项目list

```sql
SELECT  crm_customer_id
        ,COLLECT_SET(DISTINCT item_product_name) 累计核销品项list
FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     is_valid = 1
GROUP BY crm_customer_id
;
```

### U095 非本月末次核销时间
- 用户板块 / 核销 · 用户级 · VARCHAR　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户在当前月之前的末次核销日期

```sql
SELECT  a.executed_date AS 非本月末次核销日期
        ,crm_customer_id
FROM    (
            SELECT  DISTINCT executed_date
                    ,crm_customer_id
                    ,DENSE_RANK() OVER (PARTITION BY crm_customer_id ORDER BY executed_date DESC ) AS rn
            FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
            WHERE   dp = CURRENT_DATE() - 1
            AND     is_valid = 1
            AND     executed_date < SUBSTR(CURRENT_DATE(),1,7)
        ) a
WHERE   a.rn = 1
;
```

### U096 累计核销次数（按天去重）
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户的累计核销次数（同一天多次核销算一次）

```sql
SELECT  crm_customer_id
        ,COUNT(DISTINCT executed_date) AS 累计核销次数_按天去重
FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     is_valid = 1
GROUP BY crm_customer_id
;
```

### U097 非本月累计核销次数（按天去重）
- 用户板块 / 核销 · 用户级 · INT　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户非本月的累计核销次数（同一天多次核销算一次）

```sql
SELECT  crm_customer_id
        ,COUNT(DISTINCT executed_date) AS 非本月累计核销次数_按天去重
FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     is_valid = 1
AND     executed_date < SUBSTR(CURRENT_DATE(),1,7)
GROUP BY crm_customer_id
;
```

### U098 大师团核销gmv
- 用户板块 / 核销 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_ord_order_qy_execution_record_all_d`
- 定义：用户在大师团核销的gmv

```sql
SELECT  crm_customer_id
        ,SUM(CASE    WHEN customer_is_master = 1 THEN amount ELSE 0 END) AS 大师团核销gmv
FROM    soyoung_dw.dwd_ord_order_qy_execution_record_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     is_valid = 1
GROUP BY crm_customer_id
;
```

### U099 是否私域用户
- 用户板块 / 加c · 用户级 · BOOLEAN　源表：`soyoung_dw.dwd_inp_private_user_fact_all_d`
- 定义：是否私域用户

```sql
SELECT  d.unionid
        ,CASE   WHEN a.union_id IS NOT NULL THEN '是'
                ELSE '否'
        END 是否私域用户
FROM    soyoung_dw.dim_user_info d
LEFT JOIN   (
                SELECT  DISTINCT a.dp
                        ,union_id
                FROM    soyoung_dw.dwd_inp_private_user_fact_all_d a
                WHERE   a.dp = CURRENT_DATE() - 1
                AND     a.source IN (1,2)
                AND     a.data_type = 1
                AND     is_valid = 1
                AND     union_id <> ''
                AND     union_id IS NOT NULL
            ) a
ON      d.unionid = a.union_id
WHERE   d.dp = CURRENT_DATE() - 1
```

### U100 是否私域账号有效加c
- 用户板块 / 加c · 用户级 · BOOLEAN　源表：`soyoung_dw.dwd_inp_private_user_fact_all_d`
- 定义：是否私域账号有效加c

```sql
WITH siyu AS 
(
    SELECT  DISTINCT a.dp
            ,union_id
    FROM    soyoung_dw.dwd_inp_private_user_fact_all_d a
    JOIN    soyoung_dw.dim_inp_private_staff_info_all_d b 
    ON      a.qywx_user_id = b.qywx_user_id
    AND     b.source = 2
    AND     b.dp = CURRENT_DATE() - 1
    WHERE   a.dp = CURRENT_DATE() - 1
    AND     a.source = 2
    AND     a.data_type = 1
    AND     is_valid = 1
    AND     union_id <> ''
    AND     union_id IS NOT NULL
    AND     departments REGEXP '私域部|大师团'
)
SELECT  DISTINCT a.unionid
        ,CASE   WHEN t.union_id IS NOT NULL THEN '是'
                ELSE '否'
        END AS 是否私域C
FROM    soyoung_dw.dim_user_info a
LEFT JOIN siyu t
ON      a.unionid = t.union_id
WHERE   a.dp = CURRENT_DATE() - 1
```

### U101 是否网咨账号有效加c
- 用户板块 / 加c · 用户级 · BOOLEAN　源表：`soyoung_dw.dwd_inp_private_user_fact_all_d`
- 定义：是否网咨账号有效加c

```sql
WITH wangzi AS 
(
    SELECT  DISTINCT a.dp
            ,union_id
    FROM    soyoung_dw.dwd_inp_private_user_fact_all_d a
    LEFT JOIN soyoung_dw.dim_inp_private_staff_info_all_d b 
    ON      a.qywx_user_id = b.qywx_user_id
    AND     b.source = 2
    AND     b.dp = CURRENT_DATE() - 1
    WHERE   a.dp = CURRENT_DATE() - 1
    AND     a.source = 2
    AND     a.data_type = 1
    AND     is_valid = 1
    AND     departments REGEXP '总部网咨'
    AND     a.union_id <> ''
    AND     a.union_id IS NOT NULL
)
SELECT  DISTINCT a.unionid
        ,CASE   WHEN t.union_id IS NOT NULL THEN '是'
                ELSE '否'
        END AS 是否网咨C
FROM    soyoung_dw.dim_user_info a
LEFT JOIN wangzi t
ON      a.unionid = t.union_id
WHERE   a.dp = CURRENT_DATE() - 1
```

### U102 是否门店咨询账号有效加c
- 用户板块 / 加c · 用户级 · BOOLEAN　源表：`soyoung_dw.dwd_inp_private_user_fact_all_d`
- 定义：是否门店咨询账号有效加c

```sql
WITH mendian AS 
(
    SELECT  DISTINCT a.dp
            ,union_id
    FROM    soyoung_dw.dwd_inp_private_user_fact_all_d a
    LEFT JOIN soyoung_dw.dim_inp_private_staff_info_all_d b
    ON      a.qywx_user_id = b.qywx_user_id
    AND     b.source = 2
    AND     b.dp = CURRENT_DATE() - 1
    WHERE   a.dp = CURRENT_DATE() - 1
    AND     a.source = 2
    AND     a.data_type = 1
    AND     is_valid = 1
    AND     departments REGEXP '全国咨询师'
    AND     a.union_id <> ''
    AND     a.union_id IS NOT NULL
)
SELECT  DISTINCT a.unionid
        ,CASE   WHEN t.union_id IS NOT NULL THEN '是'
                ELSE '否'
        END AS 是否门店C
FROM    soyoung_dw.dim_user_info a
LEFT JOIN mendian t
ON      a.unionid = t.union_id
WHERE   a.dp = CURRENT_DATE() - 1
```

### U103 是否加群
- 用户板块 / 加c · 用户级 · BOOLEAN　源表：`soyoung_dw.dwd_inp_private_user_fact_all_d`
- 定义：是否加群

```sql
WITH qun AS  
(
    SELECT  DISTINCT a.dp
            ,union_id
    FROM    soyoung_dw.dwd_inp_private_user_fact_all_d a
    WHERE   a.dp = CURRENT_DATE() - 1
    AND     a.source = 2
    AND     a.data_type = 2
    AND     is_valid = 1
    AND     union_id <> ''
    AND     union_id IS NOT NULL
)
SELECT  DISTINCT a.unionid
        ,CASE   WHEN t.union_id IS NOT NULL THEN '是'
                ELSE '否'
        END AS 是否加群
FROM    soyoung_dw.dim_user_info a
LEFT JOIN qun t
ON      a.unionid = t.union_id
WHERE   a.dp = CURRENT_DATE() - 1
```

### U104 app首次登陆日期
- 用户板块 / 小程序 · 用户级 · DATE　源表：`soyoung_dw.dwd_md_xcx_all_log_d`
- 定义：用户首次登陆app的日期

```sql
SELECT  u.unionid
        ,MIN(a.dp) AS first_login_date
FROM    soyoung_dw.dwd_md_app_log_nocheat a
JOIN    soyoung_dw.dim_device_info d
ON      a.device_id = d.device_id
AND     d.dp = CURRENT_DATE() - 1
JOIN    soyoung_dw.dim_user_info u
ON      d.uid = u.uid
AND     u.dp = CURRENT_DATE() - 1
WHERE   a.dp >= CURRENT_DATE() - 90 --90天内
AND     a.app_id IN (131,132)
AND     a.from_action_id = 28454
AND     a.type = 1
AND     u.unionid IS NOT NULL
AND     u.unionid <> ''
GROUP BY u.unionid
;
```

### U105 app末次登陆日期
- 用户板块 / 小程序 · 用户级 · DATE　源表：`soyoung_dw.dwd_md_xcx_all_log_d`
- 定义：用户末次登陆app的日期

```sql
SELECT  u.unionid
        ,MAX(a.dp) AS last_login_date
FROM    soyoung_dw.dwd_md_app_log_nocheat a
JOIN    soyoung_dw.dim_device_info d
ON      a.device_id = d.device_id
AND     d.dp = CURRENT_DATE() - 1
JOIN    soyoung_dw.dim_user_info u
ON      d.uid = u.uid
AND     u.dp = CURRENT_DATE() - 1
WHERE   a.dp >= CURRENT_DATE() - 90 --90天内
AND     a.app_id IN (131,132)
AND     a.from_action_id = 28454
AND     a.type = 1
AND     u.unionid IS NOT NULL
AND     u.unionid <> ''
GROUP BY u.unionid
;
```

### U106 app近30天活跃天数
- 用户板块 / 小程序 · 用户级 · INT　源表：`soyoung_dw.dwd_md_xcx_all_log_d`
- 定义：用户近30天在app的活跃天数

```sql
SELECT  u.unionid
        ,COUNT(DISTINCT a.dp) AS active_days_last30
FROM    soyoung_dw.dwd_md_app_log_nocheat a
JOIN    soyoung_dw.dim_device_info d
ON      a.device_id = d.device_id
AND     d.dp = CURRENT_DATE() - 1
JOIN    soyoung_dw.dim_user_info u
ON      d.uid = u.uid
AND     u.dp = CURRENT_DATE() - 1
WHERE   a.dp >= CURRENT_DATE() - 30 -- 近30天 
AND     a.app_id IN (131,132)
AND     a.from_action_id = 28454
AND     a.type = 1
AND     u.unionid IS NOT NULL
AND     u.unionid <> ''
GROUP BY u.unionid
;
```

### U107 小程序首次登陆日期
- 用户板块 / 小程序 · 用户级 · DATE　源表：`soyoung_dw.dwd_md_xcx_all_log_d`
- 定义：用户首次登陆小程序的日期

```sql
SELECT  unionid
        ,MIN(dp) AS 小程序首次登陆日期
FROM    soyoung_dw.dwd_md_xcx_all_log_d a
WHERE   dp >= CURRENT_DATE() - 90 --90天内
AND     app_id IN (123) -- 连锁小程序
AND     from_action_id = 612 -- 小程序唤醒
AND     a.unionid IS NOT NULL
AND     a.unionid <> ''
AND     a.type = 1
GROUP BY unionid
;
```

### U108 小程序末次登陆日期
- 用户板块 / 小程序 · 用户级 · DATE　源表：`soyoung_dw.dwd_md_xcx_all_log_d`
- 定义：用户末次登陆小程序的日期

```sql
SELECT  unionid
        ,MAX(dp) AS 小程序末次登陆日期
FROM    soyoung_dw.dwd_md_xcx_all_log_d a
WHERE   dp >= CURRENT_DATE() - 90 --90天内
AND     app_id IN (123) -- 连锁小程序
AND     from_action_id = 612 -- 小程序唤醒
AND     a.unionid IS NOT NULL
AND     a.unionid <> ''
AND     a.type = 1
GROUP BY unionid
;
```

### U109 小程序近30天活跃天数
- 用户板块 / 小程序 · 用户级 · INT　源表：`soyoung_dw.dwd_md_xcx_all_log_d`
- 定义：用户近30天在小程序的活跃天数

```sql
SELECT  unionid
        ,COUNT(DISTINCT dp) AS 近30天活跃天数
FROM    soyoung_dw.dwd_md_xcx_all_log_d a
WHERE   dp >= CURRENT_DATE() - 30 -- 近30天   
AND     app_id IN (123) -- 连锁小程序
AND     from_action_id = 612 -- 小程序唤醒
AND     a.unionid IS NOT NULL
AND     a.unionid <> ''
AND     a.type = 1
GROUP BY unionid
;
```

### U110 最近有效预约日期
- 用户板块 / 预约 · 用户级 · DATE　源表：`soyoung_dw.dwd_opt_qy_reserve_all_d`
- 定义：用户最近的有效预约日期

```sql
SELECT  customer_id
        ,MIN(SUBSTR(reserve_date,1,10)) reserve_date
FROM    soyoung_dw.dwd_opt_qy_reserve_all_d
WHERE   dp = CURRENT_DATE() - 1
AND     reserve_status IN (1,2)
AND     SUBSTR(reserve_date,1,10) >= CURRENT_DATE()
GROUP BY customer_id
;
```

### U111 最近有效预约订单list
- 用户板块 / 预约 · 用户级 · STRING/ARRAY　源表：`soyoung_dw.dwd_opt_qy_reserve_all_d`
- 定义：用户最近的有效预约订单列表

```sql
SELECT  customer_id
        ,MIN(SUBSTR(reserve_date,1,10)) reserve_date
        ,COLLECT_SET(DISTINCT b.main_order_id) AS 最近有效预约订单list
FROM    soyoung_dw.dwd_opt_qy_reserve_all_d a
JOIN    soyoung_dw.dwd_ord_order_qzy_fact_all_d b
ON      a.order_id = b.sales_order_id
AND     b.dp = CURRENT_DATE() - 1
WHERE   a.dp = CURRENT_DATE() - 1
AND     SUBSTR(reserve_date,1,10) >= CURRENT_DATE()
AND     reserve_status IN (1,2)
GROUP BY customer_id 
;
```

### U112 最近有效预约gmv
- 用户板块 / 预约 · 用户级 · DECIMAL　源表：`soyoung_dw.dwd_opt_qy_reserve_all_d`
- 定义：用户最近的有效预约订单的订单金额gmv

```sql
SELECT  customer_id
        ,MIN(SUBSTR(reserve_date,1,10)) reserve_date
        ,SUM(b.pay_gmv) AS 最近有效预约gmv
FROM    soyoung_dw.dwd_opt_qy_reserve_all_d a
JOIN    soyoung_dw.dwd_ord_order_qzy_fact_all_d b
ON      a.order_id = b.sales_order_id
AND     b.dp = CURRENT_DATE() - 1
WHERE   a.dp = CURRENT_DATE() - 1
AND     SUBSTR(reserve_date,1,10) >= CURRENT_DATE()
AND     reserve_status IN (1,2)
GROUP BY customer_id
;
```
