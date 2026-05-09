# Write your MySQL query statement below
WITH player_registered AS (
    SELECT player_id, MIN(event_date) AS first_logged_in FROM Activity GROUP BY player_id
)

SELECT ROUND(COUNT(DISTINCT p.player_id)/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM Activity AS a
LEFT JOIN player_registered AS p 
    ON a.player_id = p.player_id AND a.event_date = DATE_ADD(p.first_logged_in, INTERVAL 1 DAY) 