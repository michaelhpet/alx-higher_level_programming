-- use the hbtn_0d_tvshows database to list all genres of the show Dexter
-- the tv_shows table contains only one record where title = Dexter
-- each record should display tv_genres.name
SELECT g.name
FROM tv_genres g
JOIN tv_show_genres gs
ON gs.genre_id = g.id
JOIN tv_shows t
ON gs.show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY g.name;
