-- ============================================================
-- 【1.2 让利复盘 · 深层】分「用券时等级」的 用户运营券 用券→核销→收入→让利→补贴率
-- 用券时等级 = executed_membership_level(核销/用券当日会员等级,冻结在每条核销记录上)
-- 看板不分会员等级,这是 L0 黑洞那层的唯一数据来源。窗口 = 1-5月,与看板对齐。
-- 对账:A 段「用户运营让利额」全等级加总 应 ≈ 看板 sheet1【On】用户运营价格优惠 4,297万
--        (= Sheet2 四类: 促销补贴2,947 + 老带新1,206 + 用户运营142 + 促核销3)
-- ============================================================
WITH cp AS (
  SELECT
    COALESCE(executed_membership_level,'未知') AS lvl,
    customer_id, verify_date_id, main_order_id, exe_cnt, exe_income,
    IF(exclusive_coupon_business_type IS NOT NULL, NVL(split_new_coupon_deposit,0)*exe_cnt, 0)
    + IF(red_packet_business_type IS NOT NULL AND red_packet_business_type NOT IN ('其他-仅品项使用','其他-仅禾叶使用'),
         GREATEST(NVL(base_price,0)*exe_cnt - NVL(split_new_coupon_deposit,0)*exe_cnt - NVL(exe_amount,0),0), 0) AS 让利
  FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d
  WHERE dp = CURRENT_DATE()-1 AND is_valid = 1
    AND executed_date BETWEEN '2026-01-01' AND '2026-05-31'
    AND ( exclusive_coupon_business_type IS NOT NULL
       OR (red_packet_business_type IS NOT NULL AND red_packet_business_type NOT IN ('其他-仅品项使用','其他-仅禾叶使用')) )
)
-- A · 核心:分用券时等级 用券人数/核销/收入/让利/补贴率/倒挂
SELECT
  lvl AS 用券时等级,
  COUNT(DISTINCT customer_id)    AS 用券人数,
  COUNT(DISTINCT verify_date_id) AS 核销人次,
  COUNT(DISTINCT main_order_id)  AS 核销订单数,
  SUM(exe_cnt)                   AS 核销服务点,
  ROUND(SUM(exe_income),0)       AS 核销收入,
  ROUND(SUM(让利),0)             AS 用户运营让利额,
  ROUND(SUM(让利)/NULLIF(SUM(exe_income),0),4) AS 补贴率,
  CASE WHEN SUM(让利) > SUM(exe_income) THEN '倒挂' ELSE '' END AS 让利倒挂
FROM cp
GROUP BY lvl
ORDER BY CASE WHEN lvl RLIKE '^[0-9]+$' THEN CAST(lvl AS BIGINT) ELSE 999 END ;


-- B · 支付GMV 分用券时等级(每核销主单归一个等级,去重 pay_gmv)
WITH cp AS (
  SELECT COALESCE(executed_membership_level,'未知') AS lvl, main_order_id
  FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d
  WHERE dp = CURRENT_DATE()-1 AND is_valid = 1
    AND executed_date BETWEEN '2026-01-01' AND '2026-05-31'
    AND ( exclusive_coupon_business_type IS NOT NULL
       OR (red_packet_business_type IS NOT NULL AND red_packet_business_type NOT IN ('其他-仅品项使用','其他-仅禾叶使用')) )
),
ord_lvl AS (SELECT main_order_id, MAX(lvl) AS lvl FROM cp GROUP BY main_order_id),
ogmv AS (SELECT order_id, MAX(pay_gmv) AS pay_gmv FROM soyoung_dw.dm_opt_qy_order_info_all_d
         WHERE dp = CURRENT_DATE()-1 GROUP BY order_id)
SELECT o.lvl AS 用券时等级,
       COUNT(DISTINCT o.main_order_id) AS 核销主单数,
       ROUND(SUM(g.pay_gmv),0)         AS 支付GMV
FROM ord_lvl o LEFT JOIN ogmv g ON g.order_id = o.main_order_id
GROUP BY o.lvl
ORDER BY CASE WHEN o.lvl RLIKE '^[0-9]+$' THEN CAST(o.lvl AS BIGINT) ELSE 999 END ;
