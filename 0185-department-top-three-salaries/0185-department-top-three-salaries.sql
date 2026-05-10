# Write your MySQL query statement below
WITH ranked_salaries AS (
    SELECT 
        name, salary, departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
        ) AS rnk
    FROM Employee
)

SELECT d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM ranked_salaries AS e
JOIN Department AS d
    ON e.departmentId = d.id
WHERE rnk BETWEEN 1 AND 3
