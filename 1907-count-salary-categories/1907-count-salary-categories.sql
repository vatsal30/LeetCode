# Write your MySQL query statement below
WITH salary_category AS (
    SELECT 
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary' 
        END AS category
    FROM Accounts
), all_categories AS (
    SELECT
        'Low Salary' AS category
    UNION ALL SELECT 'Average Salary'
    UNION ALL SELECT 'High Salary'
)

SELECT 
    a.category,
    COUNT(s.category) AS accounts_count
FROM all_categories AS a
LEFT JOIN salary_category AS s
    ON s.category = a.category
GROUP BY a.category