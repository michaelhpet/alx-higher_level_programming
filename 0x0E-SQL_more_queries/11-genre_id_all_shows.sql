-- list all shows contained in the database hbtn_0d_tvshows
-- each record should display tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_show.title and tv_show_genres.genre_id
--  if a show doesn't have a genre, display null
SELECT t.title, g.genre_id
FROM tv_shows t
LEFT JOIN tv_show_genres g
ON t.id = g.show_id
ORDER BY t.title, g.genre_id;
