# Write your MySQL query statement below
WITH first_orders AS (
    SELECT 
        customer_id,
        MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT 
    ROUND(
        SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100/COUNT(*)
    , 2) AS immediate_percentage
FROM Delivery AS d
JOIN first_orders AS r
    ON d.customer_id = r.customer_id
        AND d.order_date = r.first_order_date