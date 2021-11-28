-- script that lists not empty column records of a table of the database in relative MySQL server.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
