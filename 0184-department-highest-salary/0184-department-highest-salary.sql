# Write your MySQL query statement below
WITH employe_salary_rank AS (
    SELECT
        e.name AS Employee,
        d.name AS Department,
        e.salary AS Salary,
        Rank() OVER (
            PARTITION BY d.name
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM Employee AS e 
    JOIN Department as d ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM employe_salary_rank
WHERE salary_rank = 1
ORDER BY Salary DESC

