-- list all shows and all genres linked to shows
-- if a show doesn't have a genre display null in the genre column
-- each record should display tv_shows.title - tv_genres.name
-- results must be sorted in ascending order by the show title and genre name
SELECT t.title, g.name
FROM tv_shows t
LEFT JOIN tv_show_genres gs
ON t.id = gs.show_id
LEFT JOIN tv_genres g
ON gs.genre_id = g.id
ORDER BY t.title, g.name;
