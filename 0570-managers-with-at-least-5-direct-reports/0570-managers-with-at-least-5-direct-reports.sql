# Write your MySQL query statement below
SELECT m.name
FROM Employee AS e
JOIN Employee AS m ON e.managerId = m.id
GROUP BY e.managerId
HAVING COUNT(*) >=5