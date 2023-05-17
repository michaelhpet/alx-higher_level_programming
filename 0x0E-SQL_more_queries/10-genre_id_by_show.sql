-- list all shows contained in hbtn_0d_tvshows that have atlease one genre linked
-- each record should display tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT t.`title`, g.`genre_id`
FROM `hbtn_0d_tvshows`.`tv_shows` t
INNER JOIN `hbtn_0d_tvshows`.`tv_show_genres` g
ON t.`id` = g.`show_id`
ORDER BY t.`title`, g.`genre_id`;
