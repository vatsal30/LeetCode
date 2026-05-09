# Write your MySQL query statement below
WITH users_count AS (
    SELECT COUNT(*) AS total_users FROM Users
)

SELECT contest_id, ROUND(COUNT(user_id) * 100 / (SELECT total_users FROM users_count) , 2) AS percentage
FROM Register 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC