# Write your MySQL query statement below
SELECT 
    CASE WHEN id = total_seat AND id % 2 != 0 THEN id
        WHEN id % 2 = 0 THEN id - 1
    ELSE id + 1
    END AS id,
    student
FROM Seat
CROSS JOIN (SELECT COUNT(*) AS total_seat FROM Seat) t
ORDER BY id;