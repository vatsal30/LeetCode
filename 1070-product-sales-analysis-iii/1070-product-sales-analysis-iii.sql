# Write your MySQL query statement below
WITH first_sale_cte AS (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales AS s
JOIN first_sale_cte as fs
 ON s.product_id = fs.product_id AND s.year=fs.first_year
ORDER BY product_id


