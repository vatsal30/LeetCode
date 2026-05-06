# Write your MySQL query statement below
SELECT DISTINCT t1.id, 
    CASE 
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN t1.p_id IS NOT NULL and t2.id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree as t1
LEFT JOIN Tree as t2
ON t2.p_id = t1.id