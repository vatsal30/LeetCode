# Write your MySQL query statement below
SELECT 
    p.product_name,
    SUM(o.unit) AS unit
FROM Products AS p
JOIN Orders AS o
    ON p.product_id = o.product_id AND o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'
GROUP BY p.product_id
HAVING unit >= 100