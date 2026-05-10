# Write your MySQL query statement below
DELETE FROM Person AS P
WHERE id NOT IN (
    SELECT 
        P1.min_id
    FROM
        (SELECT
            email,
            MIN(id) AS min_id
        FROM Person
        GROUP BY email
    ) AS P1
) 