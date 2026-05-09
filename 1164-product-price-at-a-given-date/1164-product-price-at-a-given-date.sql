# Write your MySQL query statement below
WITH changed_prices AS (
    SELECT 
        product_id,
        MAX(change_date) AS recent_changed_date 
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)


SELECT p.product_id,
    p.new_price AS price
FROM Products AS p
JOIN changed_prices AS c
    ON c.product_id=p.product_id AND p.change_date = c.recent_changed_date
UNION ALL
SELECT product_id,
    10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'

