import mysql.connector
import matplotlib.pyplot as plt

# MySQL bağlantısı
conn = mysql.connector.connect(
    host='localhost',
    user='root',           # kendi kullanıcı adın
    password='istinye1234',   # kendi şifren
    database='film_collection'
)
cursor = conn.cursor()

# Önerilen filmleri çekme sorgusu
query = """
SELECT M2.genre, COUNT(*) as count
FROM Movies M2
JOIN Movies M1 ON M2.genre = M1.genre
WHERE M1.id IN (
  SELECT movie_id FROM User_Watchlist WHERE user_id = 1 AND rating >= 8
)
AND M2.id NOT IN (
  SELECT movie_id FROM User_Watchlist WHERE user_id = 1
)
GROUP BY M2.genre;
"""

cursor.execute(query)
results = cursor.fetchall()
print(results) 

genres = [row[0] for row in results]
counts = [row[1] for row in results]

# Grafik çizimi
plt.bar(genres, counts, color='skyblue')
plt.title('User 1 Recommended Movie Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Recommended Movies')
plt.show()

cursor.close()
conn.close()
