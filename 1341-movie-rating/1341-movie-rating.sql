# Write your MySQL query statement below
(SELECT u.name AS results FROM Users as u
JOIN MovieRating as r
    ON u.user_id = r.user_id
GROUP BY u.user_id
ORDER BY COUNT(movie_id) DESC, results ASC
LIMIT 1)
UNION ALL
(SELECT m.title AS results FROM Movies AS m
JOIN MovieRating AS r
    ON m.movie_id = r.movie_id
WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY m.movie_id
ORDER BY AVG(rating) DESC, results ASC
LIMIT 1)