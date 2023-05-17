-- list all the cities of California that can be found in the database hbtn_0d_usa
-- the states table contains only one record where name = California
-- but the di can be different
-- results must be sorted in ascending order by cities.id
SELECT * FROM cities c
WHERE c.state_id IN (
	SELECT id FROM states s
	WHERE s.name = 'California')
ORDER BY c.id ASC;

