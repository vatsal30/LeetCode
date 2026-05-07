# Write your MySQL query statement below
WITH days_with_100 AS (
    SELECT *, 
    ROW_NUMBER() OVER (
        ORDER BY id
    ) AS row_id
    FROM Stadium
    WHERE people >= 100
), row_groups AS (
    SELECT *,
    id - row_id AS group_id
    FROM days_with_100
), qualifying AS (
    SELECT group_id
    FROM row_groups
    GROUP BY group_id
    HAVING COUNT(group_id) >= 3
)

SELECT r.id, r.visit_date, r.people
FROM row_groups as r
WHERE r.group_id IN (
    SELECT group_id FROM qualifying
)
ORDER BY r.visit_date