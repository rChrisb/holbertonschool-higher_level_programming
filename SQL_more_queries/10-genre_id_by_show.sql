-- Genre ID by show
SELECT tv_shows.title, tv_show_genres.genre_id
 FROM tv_shows
 JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
 JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
 ORDER BY tv_shows.title, tv_show_genres.genre_id;