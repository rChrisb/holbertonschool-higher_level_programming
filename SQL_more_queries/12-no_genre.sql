-- No genre
SELECT tv_shows.title, tv_show_genres.genre_id
 FROM tv_shows
  LEFT JOIN tv_show_genres
   ON tv_show_genres.show_id = tv_shows.id
     LEFT JOIN tv_genres
	  ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.genre_id is null
 ORDER BY tv_shows.title, tv_show_genres.genre_id;