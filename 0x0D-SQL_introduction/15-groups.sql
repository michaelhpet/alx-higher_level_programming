-- list the number of records with the same score in the table second_table
-- the results should display the score
-- the results should display the number of records for score with label number
-- the list should be sorted by the number of records (descending)
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
