# Write your MySQL query statement below
SELECT 
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status = 'completed' THEN 0 ELSE 1 END) / COUNT(*), 
    2) AS 'Cancellation Rate'
FROM Trips AS t 
JOIN Users AS u ON t.client_id=u.users_id AND u.role='client'
JOIN Users AS d ON t.driver_id=d.users_id AND d.role='driver'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND u.banned != 'Yes' AND d.banned != 'Yes'
GROUP BY t.request_at