-- list all Comedy shows in the database
-- the tv_genres table contains only one record where name = Comedy
-- each record should display tv_shows.title
-- results must be sorted in ascending order by show title
SELECT t.title
FROM tv_shows t
JOIN tv_show_genres gs
ON t.id = gs.show_id
JOIN tv_genres g
ON gs.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY t.title;
