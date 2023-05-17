-- list all cities contained in the database hbtn_0d_usa
-- each record should display cities.id - cities.name - states.name
--  results must be sorted in ascending order by cities.id
SELECT c.id, c.name, s.name
FROM cities c
RIGHT JOIN states s
ON c.state_id = s.id
ORDER BY c.id ASC;
