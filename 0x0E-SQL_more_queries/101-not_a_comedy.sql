-- list all shows without the genre Comedy
-- the tv_genres table contains only one record where name = Comedy
-- each record should display tv_shows.title
-- results should be sorted in ascending order by the show title
SELECT t.title
FROM tv_shows t
LEFT JOIN tv_show_genres gs
ON t.id = gs.show_id
LEFT JOIN tv_genres g
ON gs.genre_id = g.id
WHERE t.title NOT IN (
	SELECT t.title
	FROM tv_shows t
	INNER JOIN tv_show_genres gs
	ON t.id = gs.show_id
	INNER JOIN tv_genres g
	ON gs.genre_id = g.id
	WHERE g.name = 'Comedy')
ORDER BY t.title;
