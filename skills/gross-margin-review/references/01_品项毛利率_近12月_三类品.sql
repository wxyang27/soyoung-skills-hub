-- ============================================================
-- 【1.1 品项毛利率复盘】近12个月(2025-06 ~ 2026-05) × 三类品
-- 数据源:数仓预聚合表 dws_opt_qy_gross_margin_stats_all_d(毛利/耗材/手工费已算好)
-- 校验:本表算出的 2026-01 大盘毛利率 = 48.7%,与「补贴看板 sheet1」完全一致 → 口径可信
-- 三类品(strategy_group) 分类规则(已与现有 green_label 映射对齐):
--   ① revenue_category='大师团'      → 大师团  (优先)
--   ② 否则 item_name ∈ 绿标品清单(35个) → 绿标品  (green_label='是')
--   ③ 其余                           → 常规品
--   注:好物(益生菌/卸妆膏等22个自营零售品)本期核销营收=0,不进核销口径。
-- ============================================================
WITH base AS (
  SELECT
    SUBSTR(stat_date,1,7) AS month_id,
    COALESCE(revenue_category,'未分类') AS revenue_category,
    COALESCE(standard_name, product_name, '未命名') AS item_name,
    SUM(CAST(exe_income AS DOUBLE))      AS exe_income,
    SUM(CAST(gross_margin_amt AS DOUBLE))AS gross_margin_amt,
    SUM(CAST(exe_cnt AS DOUBLE))         AS exe_cnt,
    SUM(CAST(ware_cost AS DOUBLE))       AS ware_cost,
    SUM(CAST(manual_fee AS DOUBLE))      AS manual_fee
  FROM soyoung_dw.dws_opt_qy_gross_margin_stats_all_d
  WHERE dp = CURRENT_DATE()-1
    AND stat_date BETWEEN '2025-06-01' AND '2026-05-31'
  GROUP BY SUBSTR(stat_date,1,7),
           COALESCE(revenue_category,'未分类'),
           COALESCE(standard_name, product_name, '未命名')
),
tagged AS (
  SELECT
    month_id, exe_income, gross_margin_amt, exe_cnt, ware_cost, manual_fee,
    CASE
      WHEN revenue_category='大师团' THEN '大师团'
      WHEN item_name IN (
        'BBL HERO','Stelyne塑缇妍50','爱拉丝提无限','爱拉丝提自由','白雪公主光','白雪公主光2.0',
        '白雪公主水光','超声线雕','大师团-爱拉丝提无限','大师团-爱拉丝提自由','大师团-奇迹胶原',
        '大师团-薇旖美ColNet胶原网','光彩注射','胶原瀑布','净颜精英','紧肤超水光','极光美白','极光色修',
        '美人鱼水光','牛奶注白光','奇迹胶原','奇迹胶原-注射','奇迹热超','奇迹童颜','水滴提升',
        '薇旖美17型胶原','新漾致灵2号','新漾致灵5号','漾活光彩针','樱花水光2.0','艺人管理','元气超光子',
        '厚皮胶原','大师团-奇迹童颜Beauty','奇迹童颜Beauty'
      ) THEN '绿标品'
      ELSE '常规品'
    END AS strategy_group
  FROM base
)
-- A · 每月 × 三类品 明细(收入/毛利/毛利率/耗材/手工费/收入占比/服务点)
SELECT
  g.month_id,
  g.strategy_group AS 三类品,
  ROUND(g.exe_income/10000,1)                              AS 核销收入万,
  ROUND(g.gross_margin_amt/10000,1)                        AS 毛利额万,
  ROUND(g.gross_margin_amt/NULLIF(g.exe_income,0),4)       AS 毛利率,
  ROUND(g.exe_income/NULLIF(m.month_income,0),4)           AS 收入占比,
  CAST(g.exe_cnt AS BIGINT)                                AS 服务点,
  ROUND(g.exe_income/NULLIF(g.exe_cnt,0),0)                AS 点均收入,
  ROUND(g.ware_cost/10000,1)                               AS 耗材成本万,
  ROUND(g.manual_fee/10000,1)                              AS 手工费万,
  ROUND(g.ware_cost/NULLIF(g.exe_income,0),4)              AS 耗材率,
  ROUND(g.manual_fee/NULLIF(g.exe_income,0),4)             AS 手工费率
FROM (
  SELECT month_id, strategy_group,
         SUM(exe_income) AS exe_income, SUM(gross_margin_amt) AS gross_margin_amt,
         SUM(exe_cnt) AS exe_cnt, SUM(ware_cost) AS ware_cost, SUM(manual_fee) AS manual_fee
  FROM tagged GROUP BY month_id, strategy_group
) g
JOIN (SELECT month_id, SUM(exe_income) AS month_income FROM tagged GROUP BY month_id) m
  ON g.month_id = m.month_id
ORDER BY g.month_id,
         CASE g.strategy_group WHEN '大师团' THEN 1 WHEN '绿标品' THEN 2 ELSE 3 END ;


-- B · 每月 大盘合计(不分组) —— 总收入/总毛利率/耗材率/手工费率 12个月趋势(头部那条线)
SELECT
  month_id,
  ROUND(SUM(exe_income)/10000,1)                           AS 核销收入万,
  ROUND(SUM(gross_margin_amt)/10000,1)                     AS 毛利额万,
  ROUND(SUM(gross_margin_amt)/NULLIF(SUM(exe_income),0),4) AS 毛利率,
  ROUND(SUM(ware_cost)/NULLIF(SUM(exe_income),0),4)        AS 耗材率,
  ROUND(SUM(manual_fee)/NULLIF(SUM(exe_income),0),4)       AS 手工费率
FROM tagged
GROUP BY month_id
ORDER BY month_id ;


-- C · 三类品 12个月累计 汇总(结构总览)
SELECT
  strategy_group AS 三类品,
  ROUND(SUM(exe_income)/10000,0)                           AS 核销收入万,
  ROUND(SUM(exe_income)/(SELECT SUM(exe_income) FROM tagged),4) AS 收入占比,
  ROUND(SUM(gross_margin_amt)/10000,0)                     AS 毛利额万,
  ROUND(SUM(gross_margin_amt)/NULLIF(SUM(exe_income),0),4) AS 毛利率,
  CAST(SUM(exe_cnt) AS BIGINT)                             AS 服务点,
  ROUND(SUM(exe_income)/NULLIF(SUM(exe_cnt),0),0)          AS 点均收入,
  ROUND(SUM(ware_cost)/NULLIF(SUM(exe_income),0),4)        AS 耗材率,
  ROUND(SUM(manual_fee)/NULLIF(SUM(exe_income),0),4)       AS 手工费率
FROM tagged
GROUP BY strategy_group
ORDER BY CASE strategy_group WHEN '大师团' THEN 1 WHEN '绿标品' THEN 2 ELSE 3 END ;
