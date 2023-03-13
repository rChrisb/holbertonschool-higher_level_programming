-- Number of shows by genre

SELECT tv_genres.name AS genre, COUNT(tv_shows.title) AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;