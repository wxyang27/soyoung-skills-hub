-- ============================================================
-- 【1.2 让利复盘 · 深层】各会员等级「0元单(赠品)」真实成本(手工费+耗材) · 1-5月
-- 成本口径 = 报告"成本型补贴":exe_amount=0 的核销项目的 手工费 + 耗材成本
-- 等级 = 当前/最新会员等级(dim_user.membership_level,与数仓/报告口径一致,每人只归一个等级,不重复计)
-- 对账:全等级「零元单成本」加总 应 ≈ 看板 sheet1【0元项目成本】886万
--        (= 灌券赠送509 + 门店开单赠送377)。重点看 L0(约97万,占其收入9.7%,是黑洞)
-- ============================================================
WITH base AS (
  SELECT
    COALESCE(u.membership_level, '未知') AS m_level,   -- 当前/最新等级(dim_user)
    t.execution_id, t.exe_amount, t.exe_cnt, t.exe_income,
    NVL(cm.手工费,0) + NVL(mt.耗材成本,0) AS 项目成本
  FROM soyoung_dw.dm_opt_qy_user_execution_record_all_d t
  LEFT JOIN soyoung_dw.dim_user_qy_crm_customer_info_all_d u
    ON u.dp = CURRENT_DATE()-1 AND u.id = t.customer_id
  LEFT JOIN (
    SELECT t1.code, SUM(t2.amount) AS 手工费
    FROM soyoung_dw.ods_db_store_crm_per_income_detail_all_d t1
    JOIN soyoung_dw.ods_db_store_crm_per_stats_all_d t2 ON t1.id=t2.detail_id AND t1.pt=t2.pt
    WHERE t1.pt=CURRENT_DATE()-1 AND t1.status=1 AND t2.type=2
    GROUP BY t1.code
  ) cm ON t.execution_id = cm.code
  LEFT JOIN (
    SELECT record_id, SUM(not_expand_exclude_tax_amount) AS 耗材成本
    FROM soyoung_dw.dwd_ord_order_qy_execution_record_cost_all_d
    WHERE dp=CURRENT_DATE()-1 AND status=1 AND consumable_type IN (1,3)
    GROUP BY record_id
  ) mt ON t.execution_id = mt.record_id
  WHERE t.dp = CURRENT_DATE()-1 AND t.is_valid=1
    AND t.executed_date BETWEEN '2026-01-01' AND '2026-05-31'
)
SELECT
  m_level,
  SUM(exe_cnt)                                              AS 总服务点数,
  SUM(CASE WHEN exe_amount=0 THEN exe_cnt ELSE 0 END)       AS 零元服务点数,
  ROUND(SUM(CASE WHEN exe_amount=0 THEN exe_cnt ELSE 0 END)/NULLIF(SUM(exe_cnt),0),4) AS 零元服务点占比,
  ROUND(SUM(CASE WHEN exe_amount=0 THEN 项目成本 ELSE 0 END),0) AS 零元单成本,
  ROUND(SUM(CASE WHEN exe_amount=0 THEN 项目成本 ELSE 0 END)/NULLIF(SUM(CASE WHEN exe_amount=0 THEN exe_cnt ELSE 0 END),0),1) AS 单个零元点成本,
  ROUND(SUM(exe_income),0)                                  AS 核销收入,
  ROUND(SUM(CASE WHEN exe_amount=0 THEN 项目成本 ELSE 0 END)/NULLIF(SUM(exe_income),0),4) AS 零元成本占收入比
FROM base
GROUP BY m_level
ORDER BY CASE WHEN m_level RLIKE '^[0-9]+$' THEN CAST(m_level AS BIGINT) ELSE 999 END ;
