# Write your MySQL query statement below
WITH confirm_req_count AS (
    SELECT 
        s.user_id,
        COUNT(c.action) AS total_req, 
        SUM(CASE WHEN c.action='confirmed' THEN 1 ELSE 0 END) AS confirmed_req
    FROM Signups AS s
    LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
    GROUP BY s.user_id
)

SELECT user_id, COALESCE(ROUND(confirmed_req/total_req, 2), 0) AS confirmation_rate
FROM confirm_req_count
ORDER BY confirmation_rate;