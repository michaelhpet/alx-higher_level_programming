-- list all shows contained in hbtn_0d_shows without a genre linked
-- each record should display  tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT t.title, g.genre_id
FROM tv_shows t
LEFT JOIN tv_show_genres g
ON t.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY t.title, g.genre_id;
