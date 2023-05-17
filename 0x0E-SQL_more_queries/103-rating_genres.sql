-- list all genres by their rating
-- each record should display tv_genres.name - rating sum
-- results must be ordered in descending order by their rating
SELECT g.name, SUM(rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres gs
ON g.id = gs.genre_id
INNER JOIN tv_show_ratings r
ON gs.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
