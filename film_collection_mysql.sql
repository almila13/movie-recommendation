SELECT DISTINCT M2.title, M2.genre
FROM User_Watchlist W
JOIN Movies M1 ON W.movie_id = M1.id
JOIN Movies M2 ON M1.genre = M2.genre
WHERE W.user_id = 1
  AND W.rating >= 8
  AND M2.id != M1.id;
