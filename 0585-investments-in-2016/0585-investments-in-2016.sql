# Write your MySQL query statement below
SELECT ROUND(SUM(t1.tiv_2016), 2) AS tiv_2016 
FROM Insurance AS t1
WHERE 
    EXISTS (
        SELECT 1 FROM Insurance AS t2 WHERE t1.pid != t2.pid AND t1.tiv_2015 = t2.tiv_2015 
    )
    AND 
    NOT EXISTS (
        SELECT 1 FROM Insurance AS t3 WHERE t1.pid != t3.pid AND t1.lat = t3.lat AND t1.lon = t3.lon)