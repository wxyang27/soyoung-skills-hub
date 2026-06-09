-- ============================================================
-- 【1.2 · L0 灌券薅羊毛证据 v2】分「发券时等级」漏斗 + 纯薅 + 0元单成本
-- 探针已确认 dim_user 保留历史分区(2026-01-02 有 46.9万行)→ 发券时等级=真·发券日等级。
-- v1 问题:核销/纯薅全为0 —— 因 coupon.order_id ≠ 核销.order_id(命名空间不同)。
-- v2 修复:核销侧改 uid 级关联(用户的用户运营券核销),不再走 order_id。
-- 口径:发券时等级 = 用户「最早发券日」会员等级(每人只归一个等级,避免升级用户跨级重复)。
--      ⚠️ 因此发券人数会比 v1 略有变化(v1按券、会跨级重复),但分布/结论一致。
-- ============================================================

-- A · 分发券时等级:发券→用券→核销→核销收入→纯薅
WITH issue AS (
  SELECT CAST(uid AS STRING) AS uid, create_date,
         CASE WHEN use_yn=1 OR order_id>0 THEN 1 ELSE 0 END AS is_used
  FROM soyoung_dw.ods_db_coupon_user_order_discount_code_all_d
  WHERE pt = CURRENT_DATE()-1
    AND create_date BETWEEN '2026-01-01 00:00:00' AND '2026-05-31 23:59:59'
),
u_first AS ( SELECT uid, SUBSTR(MIN(create_date),1,10) AS first_dt FROM issue GROUP BY uid ),
u_lvl AS (   -- 发券时等级 = 最早发券日快照(兜底当前)
  SELECT f.uid, COALESCE(us.membership_level, uc.membership_level, '未知') AS issue_level
  FROM u_first f
  LEFT JOIN soyoung_dw.dim_user_qy_crm_customer_info_all_d us
         ON us.dp = f.first_dt           AND CAST(us.uid AS STRING)=f.uid
  LEFT JOIN soyoung_dw.dim_user_qy_crm_customer_info_all_d uc
         ON uc.dp = CURRENT_DATE()-1     AND CAST(uc.uid AS STRING)=f.uid
),
u_issue AS ( SELECT uid, COUNT(*) AS issued, SUM(is_used) AS used, MAX(is_used) AS used_flag FROM issue GROUP BY uid ),
u_verify AS (   -- 用户的「用户运营券」核销(uid 级)
  SELECT CAST(uid AS STRING) AS uid,
         SUM(exe_income)                              AS v_income,
         MAX(CASE WHEN exe_income>0 THEN 1 ELSE 0 END) AS has_paid
  FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d
  WHERE dp = CURRENT_DATE()-1 AND is_valid=1
    AND executed_date BETWEEN '2026-01-01' AND '2026-05-31'
    AND ( exclusive_coupon_business_type IS NOT NULL
       OR (red_packet_business_type IS NOT NULL AND red_packet_business_type NOT IN ('其他-仅品项使用','其他-仅禾叶使用')) )
  GROUP BY uid
)
SELECT
  l.issue_level AS 发券时等级,
  COUNT(DISTINCT l.uid)                                          AS 发券人数,
  SUM(i.issued)                                                  AS 发券张数,
  COUNT(DISTINCT CASE WHEN i.used_flag=1 THEN l.uid END)         AS 用券人数,
  SUM(i.used)                                                    AS 用券张数,
  COUNT(DISTINCT CASE WHEN v.uid IS NOT NULL THEN l.uid END)     AS 核销人数,
  ROUND(SUM(v.v_income),0)                                       AS 核销收入,
  COUNT(DISTINCT CASE WHEN v.uid IS NOT NULL AND NVL(v.has_paid,0)=0 THEN l.uid END) AS 纯薅人数_核销0付费,
  COUNT(DISTINCT CASE WHEN NVL(v.has_paid,0)=1 THEN l.uid END)   AS 付费核销人数,
  ROUND(COUNT(DISTINCT CASE WHEN i.used_flag=1 THEN l.uid END)/NULLIF(COUNT(DISTINCT l.uid),0),4) AS 发到用券人率,
  ROUND(COUNT(DISTINCT CASE WHEN v.uid IS NOT NULL AND NVL(v.has_paid,0)=0 THEN l.uid END)
        /NULLIF(COUNT(DISTINCT CASE WHEN v.uid IS NOT NULL THEN l.uid END),0),4)               AS 纯薅率_占核销人
FROM u_lvl l
JOIN u_issue i ON i.uid = l.uid
LEFT JOIN u_verify v ON v.uid = l.uid
GROUP BY l.issue_level
ORDER BY CASE WHEN l.issue_level RLIKE '^[0-9]+$' THEN CAST(l.issue_level AS BIGINT) ELSE 999 END ;


-- B · 分发券时等级:这些用户的「0元单」真实成本(手工费+耗材)
--     回答"给某发券时等级灌的券,后续0元核销吃了多少成本"。等级口径同 A(最早发券日)。
WITH issue AS (
  SELECT CAST(uid AS STRING) AS uid, create_date
  FROM soyoung_dw.ods_db_coupon_user_order_discount_code_all_d
  WHERE pt = CURRENT_DATE()-1
    AND create_date BETWEEN '2026-01-01 00:00:00' AND '2026-05-31 23:59:59'
),
u_first AS ( SELECT uid, SUBSTR(MIN(create_date),1,10) AS first_dt FROM issue GROUP BY uid ),
u_lvl AS (
  SELECT f.uid, COALESCE(us.membership_level, uc.membership_level, '未知') AS issue_level
  FROM u_first f
  LEFT JOIN soyoung_dw.dim_user_qy_crm_customer_info_all_d us ON us.dp=f.first_dt        AND CAST(us.uid AS STRING)=f.uid
  LEFT JOIN soyoung_dw.dim_user_qy_crm_customer_info_all_d uc ON uc.dp=CURRENT_DATE()-1  AND CAST(uc.uid AS STRING)=f.uid
),
u_zero AS (   -- 用户级:0元单成本 + 核销收入
  SELECT CAST(t.uid AS STRING) AS uid,
    SUM(CASE WHEN t.exe_amount=0 THEN NVL(cm.手工费,0)+NVL(mt.耗材,0) ELSE 0 END) AS zero_cost,
    SUM(CASE WHEN t.exe_amount=0 THEN t.exe_cnt ELSE 0 END)                     AS zero_cnt,
    SUM(t.exe_cnt)                                                              AS exe_cnt,
    SUM(t.exe_income)                                                           AS v_income
  FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d t
  LEFT JOIN ( SELECT t1.code, SUM(t2.amount) AS 手工费
              FROM soyoung_dw.ods_db_store_crm_per_income_detail_all_d t1
              JOIN soyoung_dw.ods_db_store_crm_per_stats_all_d t2 ON t1.id=t2.detail_id AND t1.pt=t2.pt
              WHERE t1.pt=CURRENT_DATE()-1 AND t1.status=1 AND t2.type=2 GROUP BY t1.code) cm ON t.execution_id=cm.code
  LEFT JOIN ( SELECT record_id, SUM(not_expand_exclude_tax_amount) AS 耗材
              FROM soyoung_dw.dwd_ord_order_qy_execution_record_cost_all_d
              WHERE dp=CURRENT_DATE()-1 AND status=1 AND consumable_type IN (1,3) GROUP BY record_id) mt ON t.execution_id=mt.record_id
  WHERE t.dp=CURRENT_DATE()-1 AND t.is_valid=1
    AND t.executed_date BETWEEN '2026-01-01' AND '2026-05-31'
  GROUP BY CAST(t.uid AS STRING)
)
SELECT
  l.issue_level AS 发券时等级,
  COUNT(DISTINCT l.uid)                       AS 发券人数,
  ROUND(SUM(z.zero_cost),0)                   AS 零元单成本,
  SUM(z.zero_cnt)                             AS 零元服务点,
  ROUND(SUM(z.zero_cnt)/NULLIF(SUM(z.exe_cnt),0),4) AS 零元点占比,
  ROUND(SUM(z.zero_cost)/NULLIF(SUM(z.zero_cnt),0),1) AS 单个零元点成本,
  ROUND(SUM(z.v_income),0)                    AS 核销收入,
  ROUND(SUM(z.zero_cost)/NULLIF(SUM(z.v_income),0),4) AS 零元成本占收入比
FROM u_lvl l
JOIN u_zero z ON z.uid = l.uid
GROUP BY l.issue_level
ORDER BY CASE WHEN l.issue_level RLIKE '^[0-9]+$' THEN CAST(l.issue_level AS BIGINT) ELSE 999 END ;
