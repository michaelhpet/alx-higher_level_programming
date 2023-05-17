-- list all shows by their rating
-- each record should display rv_shows.title - rating sum
-- results must be sorted in descending order by their rating
SELECT t.title, SUM(rate) AS rating
FROM tv_shows t
INNER JOIN tv_show_ratings r
ON t.id = r.show_id
GROUP BY t.title
ORDER BY rating DESC;
