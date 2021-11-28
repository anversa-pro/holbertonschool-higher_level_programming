-- script that lists the number of records with the same value in a table second_table of the database in relative MySQL server.
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score ORDER BY number DESC;