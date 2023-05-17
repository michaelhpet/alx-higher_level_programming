-- list all genres not linked to the show Dexter
-- the tv_shows table contains only one record where title = Dexter
-- each record should display tv_genres.name
-- results must be sorted in ascending order by genre name
SELECT DISTINCT g.name
FROM tv_genres g
INNER JOIN tv_show_genres gs
ON g.id = gs.genre_id
INNER JOIN tv_shows t
ON gs.show_id = t.id
WHERE g.name NOT IN (
	SELECT name
	FROM tv_genres g
	INNER JOIN tv_show_genres gs
	ON g.id = gs.genre_id
	INNER JOIN tv_shows t
	ON gs.show_id = t.id
	WHERE t.title = 'Dexter')
ORDER BY g.name;
