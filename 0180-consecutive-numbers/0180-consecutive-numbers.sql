# Write your MySQL query statement below
WITH nums_cte AS (
    SELECT num, LEAD(num, 1) OVER(ORDER BY id) AS num1, LEAD(num, 2) OVER(ORDER BY id) AS num2 FROM Logs
)

SELECT DISTINCT num AS ConsecutiveNums FROM nums_cte WHERE num = num1 AND num1 = num2