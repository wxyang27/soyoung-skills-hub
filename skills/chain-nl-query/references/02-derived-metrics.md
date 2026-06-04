# 衍生指标字典（132 个）

> 来源：指标字典 · 衍生指标字典 sheet。
> 衍生指标 = 原子指标 + 维度过滤。下表给出每个指标与其原子指标、维度切片、**关键追加过滤条件**；
> 复合/比率指标在末尾附完整 SQL。字段名以 SQL 为准（见 04-dimensions.md 的字段名差异表）。

## 全量索引（含关键过滤与所属看板）

| ID | 指标名称 | 原子指标 | 维度切片 | 类型 | 源表 | 所属看板 |
| --- | --- | --- | --- | --- | --- | --- |
| D001 | 新客核销gmv | 核销gmv | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D002 | 老客核销gmv | 核销gmv | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D003 | 大师团核销gmv | 核销gmv | 大师团 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D004 | 大单品核销gmv | 核销gmv | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D005 | 常规品核销gmv | 核销gmv | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D006 | 私域核销gmv | 核销gmv | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D007 | 公域核销gmv | 核销gmv | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D008 | 老带新核销gmv | 核销gmv | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D009 | BBL HERO核销gmv | 核销gmv | 品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D010 | 新客核销收入 | 核销收入 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 用户KPI看板, 用户整体看板 |
| D011 | 老客核销收入 | 核销收入 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 用户KPI看板 |
| D012 | 大师团核销收入 | 核销收入 | 大师团 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 连锁品项总览 |
| D013 | 大单品核销收入 | 核销收入 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 连锁品项分析, 连锁品项总览 |
| D014 | 常规品核销收入 | 核销收入 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 连锁品项总览 |
| D015 | 私域核销收入 | 核销收入 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D016 | 公域核销收入 | 核销收入 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D017 | 老带新核销收入 | 核销收入 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D018 | BBL HERO核销收入 | 核销收入 | 品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D019 | 新客核销服务点数 | 核销服务点数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D020 | 老客核销服务点数 | 核销服务点数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D021 | 大师团核销服务点数 | 核销服务点数 | 大师团 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D022 | 大单品核销服务点数 | 核销服务点数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D023 | 常规品核销服务点数 | 核销服务点数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D024 | 私域核销服务点数 | 核销服务点数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D025 | 公域核销服务点数 | 核销服务点数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D026 | 老带新核销服务点数 | 核销服务点数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D027 | BBL HERO核销服务点数 | 核销服务点数 | 品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D028 | 新客核销用户数 | 核销用户数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 信息流网咨看板 |
| D029 | 老客核销用户数 | 核销用户数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D030 | 大师团核销用户数 | 核销用户数 | 大师团 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D031 | 大单品核销用户数 | 核销用户数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D032 | 大单品品项核销用户数 | 核销用户数 | 大单品品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D033 | 常规品核销用户数 | 核销用户数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D034 | 私域核销用户数 | 核销用户数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D035 | 公域核销用户数 | 核销用户数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D036 | 老带新核销用户数 | 核销用户数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D037 | BBL HERO核销用户数 | 核销用户数 | 品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D038 | 新客核销人次 | 核销人次 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 用户整体看板 |
| D039 | 老客核销人次 | 核销人次 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 用户KPI看板 |
| D040 | 大师团核销人次 | 核销人次 | 大师团 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D041 | 大单品核销人次 | 核销人次 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 连锁品项分析 |
| D042 | 大单品品项核销人次 | 核销人次 | 大单品品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D043 | 常规品核销人次 | 核销人次 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D044 | 私域核销人次 | 核销人次 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D045 | 公域核销人次 | 核销人次 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D046 | 老带新核销人次 | 核销人次 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D047 | BBL HERO核销人次 | 核销人次 | 品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D048 | 新客核销订单数 | 核销订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D049 | 新客0元核销订单数 | 核销订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D050 | 老客核销订单数 | 核销订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D051 | 老客0元核销订单数 | 核销订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D052 | 大师团核销订单数 | 核销订单数 | 大师团 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D053 | 大师团0元核销订单数 | 核销订单数 | 大师团 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D054 | 大单品核销订单数 | 核销订单数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | 连锁品项分析 |
| D055 | 大单品品项核销订单数 | 核销订单数 | 大单品品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D056 | 大单品0元核销订单数 | 核销订单数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D057 | 常规品核销订单数 | 核销订单数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D058 | 常规品0元核销订单数 | 核销订单数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D059 | 私域核销订单数 | 核销订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D060 | 私域0元核销订单数 | 核销订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D061 | 公域核销订单数 | 核销订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D062 | 公域0元核销订单数 | 核销订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D063 | 老带新核销订单数 | 核销订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D064 | 老带新0元核销订单数 | 核销订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D065 | BBL HERO核销订单数 | 核销订单数 | 品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D066 | BBL HERO0元核销订单数 | 核销订单数 | 品项 | 衍生指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D067 | 新客核销客单价 | 核销客单价 | 新客/老客 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D068 | 老客核销客单价 | 核销客单价 | 新客/老客 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D069 | 大师团核销客单价 | 核销客单价 | 大师团 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D070 | 大单品核销客单价 | 核销客单价 | 大单品/常规品 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | 连锁品项分析 |
| D071 | 常规品核销客单价 | 核销客单价 | 大单品/常规品 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D072 | 私域核销客单价 | 核销客单价 | 获客渠道 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D073 | 公域核销客单价 | 核销客单价 | 获客渠道 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D074 | 老带新核销客单价 | 核销客单价 | 获客渠道 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D075 | BBL HERO核销客单价 | 核销客单价 | 品项 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D076 | 相控微针升单客单价 | 核销客单价 | 品项 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D077 | 新客支付订单数 | 支付订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D078 | 新客0元支付订单数 | 支付订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D079 | 老客支付订单数 | 支付订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D080 | 老客0元支付订单数 | 支付订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D081 | 大单品支付订单数 | 支付订单数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D082 | BBL HERO支付订单数 | 支付订单数 | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D083 | 新客支付gmv | 支付gmv | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D084 | 老客支付gmv | 支付gmv | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D085 | 大单品支付gmv | 支付gmv | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D086 | BBL HERO支付gmv | 支付gmv | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D087 | 新客支付人数 | 支付人数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D088 | 老客支付人数 | 支付人数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D089 | 大单品支付人数 | 支付人数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | 连锁品项分析 |
| D090 | BBL HERO支付人数 | 支付人数 | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D091 | 新客支付客单价 | 支付客单价 | 新客/老客 | 复合指标 | `dm_opt_qy_order_info_all_d` | — |
| D092 | 老客支付客单价 | 支付客单价 | 新客/老客 | 复合指标 | `dm_opt_qy_order_info_all_d` | — |
| D093 | 大单品支付客单价 | 支付客单价 | 大单品/常规品 | 复合指标 | `dm_opt_qy_order_info_all_d` | 连锁品项分析 |
| D094 | BBL HERO支付客单价 | 支付客单价 | 品项 | 复合指标 | `dm_opt_qy_order_info_all_d` | — |
| D095 | 新客待核销gmv | 待核销gmv | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D096 | 老客待核销gmv | 待核销gmv | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D097 | 大单品待核销gmv | 待核销gmv | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D098 | BBL HERO待核销gmv | 待核销gmv | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D099 | 新客待核销服务点 | 待核销服务点 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D100 | 老客待核销服务点 | 待核销服务点 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D101 | 大单品待核销服务点 | 待核销服务点 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | 连锁品项分析 |
| D102 | BBL HERO待核销服务点 | 待核销服务点 | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D103 | 新客升单人数 | 升单人数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D104 | 老客升单人数 | 升单人数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D105 | 大师团升单人数 | 升单人数 | 大师团 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D106 | 大单品升单人数 | 升单人数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D107 | 常规品升单人数 | 升单人数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D108 | 私域升单人数 | 升单人数 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D109 | 公域升单人数 | 升单人数 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D110 | 老带新升单人数 | 升单人数 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D111 | BBL HERO升单人数 | 升单人数 | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D112 | 新客升单订单数 | 升单订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D113 | 老客升单订单数 | 升单订单数 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D114 | 大师团升单订单数 | 升单订单数 | 大师团 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D115 | 大单品升单订单数 | 升单订单数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D116 | 常规品升单订单数 | 升单订单数 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D117 | 私域升单订单数 | 升单订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D118 | 公域升单订单数 | 升单订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D119 | 老带新升单订单数 | 升单订单数 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D120 | BBL HERO升单订单数 | 升单订单数 | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D121 | 新客升单人次 | 升单人次 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D122 | 老客升单人次 | 升单人次 | 新客/老客 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D123 | 大师团升单人次 | 升单人次 | 大师团 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D124 | 大单品升单人次 | 升单人次 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D125 | 常规品品升单人次 | 升单人次 | 大单品/常规品 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D126 | 私域升单人次 | 升单人次 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D127 | 公域升单人次 | 升单人次 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D128 | 老带新升单人次 | 升单人次 | 获客渠道 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D129 | BBL HERO升单人次 | 升单人次 | 品项 | 衍生指标 | `dm_opt_qy_order_info_all_d` | — |
| D130 | 相控微针升单率 | 核销人次 | 品项 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D131 | BBL HERO加购率 | 核销人次 | 品项 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |
| D132 | BBL HERO渗透率 | 核销用户数 | 品项 | 复合指标 | `dm_opt_qy_user_execution_record_all_d` | — |

## 复合 / 比率指标完整 SQL

以下指标不是简单的「原子 + 过滤」，需要按完整 SQL 取数：

### D067 新客核销客单价

- 维度切片：新客/老客　类型：复合指标
- 定义：统计周期内，新客核销收入/新客核销人次
- 公式：新客核销收入 / 新客核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT SUM(exe_income)/count(DISTINCT verify_date_id) 新客核销客单价
FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_new = 1
AND is_valid = 1
```

### D068 老客核销客单价

- 维度切片：新客/老客　类型：复合指标
- 定义：统计周期内，老客核销收入/老客核销人次
- 公式：老客核销收入 / 老客核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT SUM(exe_income)/count(DISTINCT verify_date_id) 老客核销客单价
FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_new = 0
AND is_valid = 1
```

### D069 大师团核销客单价

- 维度切片：大师团　类型：复合指标
- 定义：统计周期内，大师团核销收入/大师团核销人次
- 公式：大师团核销收入 / 大师团核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_income)/count(DISTINCT verify_date_id) 大师团核销客单价
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     revenue_category='大师团'
AND     is_valid = 1
```

### D070 大单品核销客单价

- 维度切片：大单品/常规品　类型：复合指标
- 定义：统计周期内，大单品的核销收入/收入类别为大单品的核销人次
- 公式：大单品核销收入 / 大单品核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_income)/count(DISTINCT verify_date_id) 大单品核销客单价
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     revenue_category='大单品'
AND     is_valid = 1
```

### D071 常规品核销客单价

- 维度切片：大单品/常规品　类型：复合指标
- 定义：统计周期内，常规品核销收入/常规品核销人次
- 公式：常规品核销收入 / 常规品核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_income)/count(DISTINCT verify_date_id) 常规品核销客单价
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     revenue_category='常规品'
AND     is_valid = 1
```

### D072 私域核销客单价

- 维度切片：获客渠道　类型：复合指标
- 定义：统计周期内，获客渠道为私域的所有用户核销收入之和/获客渠道为私域的所有用户核销人次
- 公式：私域核销收入 / 私域核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_income)/count(DISTINCT verify_date_id)  私域核销客单价
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     cx_first_channel = '私域'
AND     is_valid = 1
```

### D073 公域核销客单价

- 维度切片：获客渠道　类型：复合指标
- 定义：统计周期内，获客渠道为公域的所有用户核销收入/获客渠道为公域的所有用户核销人次
- 公式：公域核销收入 / 公域核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_income)/count(DISTINCT verify_date_id)  公域核销客单价
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     cx_first_channel = '公域'
AND     is_valid = 1
```

### D074 老带新核销客单价

- 维度切片：获客渠道　类型：复合指标
- 定义：统计周期内，获客渠道为老带新的所有用户核销收入之和/获客渠道为老带新的所有用户核销人次
- 公式：老带新核销收入 / 老带新核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT  SUM(exe_income)/count(DISTINCT verify_date_id)  老带新核销客单价
FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE   dp = DATE_SUB(CURRENT_DATE(),1)
AND     cx_first_channel = '老带新'
AND     is_valid = 1
```

### D075 BBL HERO核销客单价

- 维度切片：品项　类型：复合指标
- 定义：统计周期内，BBL HERO核销收入之和/BBL HERO核销人次
- 公式：BBL HERO核销收入 / BBL HERO核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT SUM(exe_income)/count(DISTINCT verify_date_id) BBL HERO核销客单价
FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND standard_name REGEXP 'BBL HERO'
AND is_valid = 1
```

### D076 相控微针升单客单价

- 维度切片：品项　类型：复合指标
- 定义：统计周期内，原单为相控微针且当日发生升单的核销收入之和/原单为相控微针且当日发生升单的核销人次
- 公式：相控微针升单客单价核销收入 / 相控微针升单客单价核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT a.standard_name ,
            sum(if(a.verify_date_id = b.verify_date_id,b.exe_income,0))/nullif(count(distinct if(b.verify_date_id is not null,a.verify_date_id,null)),0) 相控微针升单客单价
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
                         ,exe_income
                FROM    soyoung_dw.dm_opt_qy_user_execution_record_all_d 
                WHERE   dp = DATE_SUB(current_date(),1)
                AND     ord_up_type_name = '升单'
                AND     is_valid = 1
            ) b
ON     a.verify_date_id = b.verify_date_id
GROUP BY a.standard_name
;
```

### D091 新客支付客单价

- 维度切片：新客/老客　类型：复合指标
- 定义：统计周期内，新客支付总gmv/新客总支付人次
- 公式：新客支付GMV / 新客支付人次
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
select sum(pay_gmv)/count(distinct concat(uid,pay_date)) as 新客支付客单价
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_pay_new=1
AND is_paydate_cash = 0
;
```

### D092 老客支付客单价

- 维度切片：新客/老客　类型：复合指标
- 定义：统计周期内，老客支付总gmv/老客总支付人次
- 公式：老客支付GMV / 老客支付人次
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
select sum(pay_gmv)/count(distinct concat(uid,pay_date)) as 老客支付客单价
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_pay_new=0
AND is_paydate_cash = 0
;
```

### D093 大单品支付客单价

- 维度切片：大单品/常规品　类型：复合指标
- 定义：统计周期内，所有大单品品项支付总gmv/所有大单品品项总支付人次
- 公式：大单品支付GMV / 大单品支付人次
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
select sum(pay_gmv)/count(distinct concat(uid,pay_date)) as 大单品支付客单价
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND revenue_category = '大单品'
AND is_paydate_cash = 0
;
```

### D094 BBL HERO支付客单价

- 维度切片：品项　类型：复合指标
- 定义：统计周期内，BBL HERO支付总gmv/BBL HERO总支付人次
- 公式：BBL HERO支付GMV / BBL HERO支付人次
- 源表：`soyoung_dw.dm_opt_qy_order_info_all_d`

```sql
select sum(pay_gmv)/count(distinct concat(uid,pay_date)) as BBL HERO支付客单价
from soyoung_dw.dm_opt_qy_order_info_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND standard_name REGEXP 'BBL HERO'
AND is_paydate_cash = 0
;
```

### D130 相控微针升单率

- 维度切片：品项　类型：复合指标
- 定义：统计周期内，原单为相控微针且当日发生升单的核销人次/相控微针原单核销人次
- 公式：升单人次 / 原单核销人次
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

### D131 BBL HERO加购率

- 维度切片：品项　类型：复合指标
- 定义：统计周期内，品项的升单核销人次/总核销人次
- 公式：升单核销人次 / 总核销人次
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT 
COUNT(DISTINCT CASE WHEN standard_name regexp "BBL HERO" and is_up =1 then verify_date_id end)/
COUNT(DISTINCT verify_date_id) as 加购率
FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(),1)
AND is_valid = 1
;
```

### D132 BBL HERO渗透率

- 维度切片：品项　类型：复合指标
- 定义：90日内，核销过BBL HERO的用户数/总核销用户数量
- 公式：品项核销用户数 / 总核销用户数
- 源表：`soyoung_dw.dm_opt_qy_user_execution_record_all_d`

```sql
SELECT 
 ROUND(
 COUNT(DISTINCT case when product_name regexp "BBL HERO" then customer_id end) * 1.0 / 
 NULLIF(COUNT(DISTINCT customer_id), 0), 4 ) as 渗透率
FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d 
WHERE dp = DATE_SUB(CURRENT_DATE(), 1)
 AND executed_date BETWEEN DATE_SUB(DATE_SUB(CURRENT_DATE(), 1), 89) AND DATE_SUB(CURRENT_DATE(), 1) -- 截至昨天的滚动90天
 AND is_valid = 1;
```

## 衍生指标 SQL 模板（按原子指标分组）

简单衍生指标 = 对应原子指标 SQL + 下列「追加过滤」。把过滤 AND 进原子指标的 WHERE 即可。

### 原子指标：核销gmv

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客核销gmv | 新客/老客 | `is_new = 1` |
| 老客核销gmv | 新客/老客 | `is_new = 0` |
| 大师团核销gmv | 大师团 | `revenue_category = '大师团'` |
| 大单品核销gmv | 大单品/常规品 | `revenue_category = '大单品'` |
| 常规品核销gmv | 大单品/常规品 | `revenue_category ='常规品'` |
| 私域核销gmv | 获客渠道 | `cx_first_channel='私域'` |
| 公域核销gmv | 获客渠道 | `cx_first_channel='公域'` |
| 老带新核销gmv | 获客渠道 | `cx_first_channel='老带新'` |
| BBL HERO核销gmv | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：核销收入

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客核销收入 | 新客/老客 | `is_new = 1` |
| 老客核销收入 | 新客/老客 | `is_new = 0` |
| 大师团核销收入 | 大师团 | `revenue_category='大师团'` |
| 大单品核销收入 | 大单品/常规品 | `revenue_category='大单品'` |
| 常规品核销收入 | 大单品/常规品 | `revenue_category='常规品'` |
| 私域核销收入 | 获客渠道 | `cx_first_channel = '私域'` |
| 公域核销收入 | 获客渠道 | `cx_first_channel = '公域'` |
| 老带新核销收入 | 获客渠道 | `cx_first_channel = '老带新'` |
| BBL HERO核销收入 | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：核销服务点数

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客核销服务点数 | 新客/老客 | `is_new = 1` |
| 老客核销服务点数 | 新客/老客 | `is_new = 0` |
| 大师团核销服务点数 | 大师团 | `revenue_category='大师团'` |
| 大单品核销服务点数 | 大单品/常规品 | `revenue_category='大单品'` |
| 常规品核销服务点数 | 大单品/常规品 | `revenue_category='常规品'` |
| 私域核销服务点数 | 获客渠道 | `cx_first_channel = '私域'` |
| 公域核销服务点数 | 获客渠道 | `cx_first_channel = '公域'` |
| 老带新核销服务点数 | 获客渠道 | `cx_first_channel = '老带新'` |
| BBL HERO核销服务点数 | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：核销用户数

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客核销用户数 | 新客/老客 | `is_new = 1` |
| 老客核销用户数 | 新客/老客 | `is_new = 0` |
| 大师团核销用户数 | 大师团 | `revenue_category = '大师团'` |
| 大单品核销用户数 | 大单品/常规品 | `revenue_category = '大单品'` |
| 大单品品项核销用户数 | 大单品品项 | `standard_name REGEXP 'BBL HERO|奇迹童颜|新一代热玛吉|爱拉丝提'` |
| 常规品核销用户数 | 大单品/常规品 | `revenue_category = '常规品'` |
| 私域核销用户数 | 获客渠道 | `cx_first_channel='私域'` |
| 公域核销用户数 | 获客渠道 | `cx_first_channel='公域'` |
| 老带新核销用户数 | 获客渠道 | `cx_first_channel='老带新'` |
| BBL HERO核销用户数 | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：核销人次

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客核销人次 | 新客/老客 | `is_new = 1` |
| 老客核销人次 | 新客/老客 | `is_new = 0` |
| 大师团核销人次 | 大师团 | `revenue_category='大师团'` |
| 大单品核销人次 | 大单品/常规品 | `revenue_category='大单品'` |
| 大单品品项核销人次 | 大单品品项 | `standard_name REGEXP 'BBL HERO|奇迹童颜|新一代热玛吉|爱拉丝提'` |
| 常规品核销人次 | 大单品/常规品 | `revenue_category='常规品'` |
| 私域核销人次 | 获客渠道 | `cx_first_channel='私域'` |
| 公域核销人次 | 获客渠道 | `cx_first_channel='公域'` |
| 老带新核销人次 | 获客渠道 | `cx_first_channel='老带新'` |
| BBL HERO核销人次 | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：核销订单数

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客核销订单数 | 新客/老客 | `is_new = 1` |
| 新客0元核销订单数 | 新客/老客 | `is_new = 1 AND exe_income = 0` |
| 老客核销订单数 | 新客/老客 | `is_new = 0` |
| 老客0元核销订单数 | 新客/老客 | `is_new = 0 AND exe_income = 0` |
| 大师团核销订单数 | 大师团 | `revenue_category = '大师团'` |
| 大师团0元核销订单数 | 大师团 | `revenue_category = '大师团' AND exe_income = 0` |
| 大单品核销订单数 | 大单品/常规品 | `revenue_category = '大单品'` |
| 大单品品项核销订单数 | 大单品品项 | `standard_name REGEXP 'BBL HERO|奇迹童颜|新一代热玛吉|爱拉丝提'` |
| 大单品0元核销订单数 | 大单品/常规品 | `revenue_category = '大单品' AND exe_income = 0` |
| 常规品核销订单数 | 大单品/常规品 | `revenue_category = '常规品'` |
| 常规品0元核销订单数 | 大单品/常规品 | `revenue_category = '常规品' AND exe_income = 0` |
| 私域核销订单数 | 获客渠道 | `cx_first_channel = '私域'` |
| 私域0元核销订单数 | 获客渠道 | `cx_first_channel = '私域' AND exe_income = 0` |
| 公域核销订单数 | 获客渠道 | `cx_first_channel = '公域'` |
| 公域0元核销订单数 | 获客渠道 | `cx_first_channel = '公域' AND exe_income = 0` |
| 老带新核销订单数 | 获客渠道 | `cx_first_channel = '老带新'` |
| 老带新0元核销订单数 | 获客渠道 | `cx_first_channel = '老带新' AND exe_income = 0` |
| BBL HERO核销订单数 | 品项 | `standard_name REGEXP 'BBL HERO'` |
| BBL HERO0元核销订单数 | 品项 | `standard_name REGEXP 'BBL HERO' AND exe_income = 0` |

### 原子指标：支付订单数

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客支付订单数 | 新客/老客 | `is_pay_new=1` |
| 新客0元支付订单数 | 新客/老客 | `is_pay_new=1 AND pay_gmv = 0` |
| 老客支付订单数 | 新客/老客 | `is_pay_new=0` |
| 老客0元支付订单数 | 新客/老客 | `is_pay_new=0 AND pay_gmv = 0` |
| 大单品支付订单数 | 大单品/常规品 | `revenue_category = '大单品'` |
| BBL HERO支付订单数 | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：支付gmv

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客支付gmv | 新客/老客 | `is_pay_new=1` |
| 老客支付gmv | 新客/老客 | `is_pay_new=0` |
| 大单品支付gmv | 大单品/常规品 | `revenue_category = "大单品"` |
| BBL HERO支付gmv | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：支付人数

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客支付人数 | 新客/老客 | `is_pay_new=1` |
| 老客支付人数 | 新客/老客 | `is_pay_new=0` |
| 大单品支付人数 | 大单品/常规品 | `revenue_category  = '大单品'` |
| BBL HERO支付人数 | 品项 | `standard_name REGEXP 'BBL HERO'` |

### 原子指标：待核销gmv

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客待核销gmv | 新客/老客 | `is_pay_new=1 AND left_num > 0` |
| 老客待核销gmv | 新客/老客 | `is_pay_new=0 AND left_num > 0` |
| 大单品待核销gmv | 大单品/常规品 | `revenue_category = '大单品' AND left_num > 0` |
| BBL HERO待核销gmv | 品项 | `standard_name REGEXP 'BBL HERO' AND left_num > 0` |

### 原子指标：待核销服务点

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客待核销服务点 | 新客/老客 | `is_pay_new=1 AND left_num > 0` |
| 老客待核销服务点 | 新客/老客 | `is_pay_new=0 AND left_num > 0` |
| 大单品待核销服务点 | 大单品/常规品 | `revenue_category = '大单品' AND left_num > 0` |
| BBL HERO待核销服务点 | 品项 | `standard_name REGEXP 'BBL HERO' AND left_num > 0` |

### 原子指标：升单人数

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客升单人数 | 新客/老客 | `is_up = 1 AND is_new = 1` |
| 老客升单人数 | 新客/老客 | `is_up = 1 AND is_new = 0` |
| 大师团升单人数 | 大师团 | `is_up = 1 AND revenue_category = '大师团'` |
| 大单品升单人数 | 大单品/常规品 | `is_up = 1 AND revenue_category = '大单品'` |
| 常规品升单人数 | 大单品/常规品 | `is_up = 1 AND revenue_category = '常规品'` |
| 私域升单人数 | 获客渠道 | `is_up = 1 AND cx_first_channel = '私域'` |
| 公域升单人数 | 获客渠道 | `is_up = 1 AND cx_first_channel = '公域'` |
| 老带新升单人数 | 获客渠道 | `is_up = 1 AND cx_first_channel = '老带新'` |
| BBL HERO升单人数 | 品项 | `is_up = 1 AND standard_name REGEXP 'BBL HERO'` |

### 原子指标：升单订单数

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客升单订单数 | 新客/老客 | `is_up = 1 AND is_new = 1` |
| 老客升单订单数 | 新客/老客 | `is_up = 1 AND is_new = 0` |
| 大师团升单订单数 | 大师团 | `is_up = 1 AND revenue_category = '大师团'` |
| 大单品升单订单数 | 大单品/常规品 | `is_up = 1 AND revenue_category = '大单品'` |
| 常规品升单订单数 | 大单品/常规品 | `is_up = 1 AND revenue_category = '常规品'` |
| 私域升单订单数 | 获客渠道 | `is_up = 1 AND cx_first_channel = '私域'` |
| 公域升单订单数 | 获客渠道 | `is_up = 1 AND cx_first_channel = '公域'` |
| 老带新升单订单数 | 获客渠道 | `is_up = 1 AND cx_first_channel = '老带新'` |
| BBL HERO升单订单数 | 品项 | `is_up = 1 AND standard_name REGEXP 'BBL HERO'` |

### 原子指标：升单人次

| 衍生指标 | 维度切片 | 追加过滤条件 |
| --- | --- | --- |
| 新客升单人次 | 新客/老客 | `is_up = 1 AND is_new = 1` |
| 老客升单人次 | 新客/老客 | `is_up = 1 AND is_new = 0` |
| 大师团升单人次 | 大师团 | `is_up = 1 AND revenue_category = '大师团'` |
| 大单品升单人次 | 大单品/常规品 | `is_up = 1 AND revenue_category = '大单品'` |
| 常规品品升单人次 | 大单品/常规品 | `is_up = 1 AND revenue_category = '常规品'` |
| 私域升单人次 | 获客渠道 | `is_up = 1 AND cx_first_channel = '私域'` |
| 公域升单人次 | 获客渠道 | `is_up = 1 AND cx_first_channel = '公域'` |
| 老带新升单人次 | 获客渠道 | `is_up = 1 AND cx_first_channel = '老带新'` |
| BBL HERO升单人次 | 品项 | `is_up = 1 AND standard_name REGEXP 'BBL HERO'` |
