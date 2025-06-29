# -*- coding: utf-8 -*-
"""SystemRecommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IDPT78k1X2HNl7lfj_lIwp_RgKhscBfY

# Proyek sistem rekomendasi film

- **Nama:** Naufal Dzakwan Zakianto
- **Email:** naufal.dzakwann28@gmail.com
- **ID Dicoding:** MC012D5Y2416

# Project overview

Saat ini industri film sudah berkembang sangat cepat, jika dahulu para penikmat film diharuskan untuk datang ke bioskop atau membeli vcd untuk dapat menikmati film, kini industri film sudah mengalami digitalisasi. Perusahaan besar yang menyediakan tempat atau platform untuk menikmati film mulai bermunculan, seperti Netflix, Youtube, maupun Amazon. Perkembangan yang pesat tentunya juga mengakibatkan bertambahnya produksi film secara masif setiap tahunnya, sehingga pengguna mengalami kesulitan dalam menemukan film yang sesuai dengan preferensi mereka. Untuk mengatasi permasalahan tersebut, banyak perusahaan menggunakan sistem rekomendasi agar mereka dapat melayani pengguna dengan lebih baik dan meningkatkan keuntungan mereka (Sunilkumar, 2020). Hal ini karena sistem rekomendasi dapat membantu menyaring ribuan opsi dan menyajikan film yang sesuai dengan selera pengguna. Sejalan dengan kebutuhan tersebut, proyek ini bertujuan untuk mengembangkan sistem rekomendasi menggunakan dua pendekatan utama, yaitu content-based filtering dan collaborative filtering.

# Business understanding

**Problem Statements**

1. Bagaimana cara memberikan rekomendasi film yang relevan kepada pengguna berdasarkan preferensi mereka?

2. Bagaimana memanfaatkan data rating pengguna dan data film untuk menghasilkan rekomendasi yang akurat?

**Goals**
1. Membangun sistem rekomendasi yang dapat memberikan daftar 10 film terbaik untuk pengguna.

2. Mengimplementasikan dua pendekatan berbeda: content-based filtering dan collaborative filtering.

**Solution Approach**
1. Content-Based Filtering: Menggunakan metadata film (genre) untuk merekomendasikan film yang mirip dengan yang disukai pengguna.

2. Collaborative Filtering: Menggunakan data rating dari pengguna lain untuk merekomendasikan film yang mungkin disukai oleh pengguna serupa.

# Import library
"""

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# Data Loading"""

path = kagglehub.dataset_download("nicoletacilibiu/movies-and-ratings-for-recommendation-system")
print("Path to dataset files:", path)

movies = pd.read_csv(path + "/movies.csv")
ratings = pd.read_csv(path + "/ratings.csv")

"""# Data understanding

Data yang digunakan adalah data movies and ratings, data ini berasal dari kaggle yang dapat di akses melalui: https://www.kaggle.com/datasets/nicoletacilibiu/movies-and-ratings-for-recommendation-system

Data tersebut memiliki 2 buah dataset yaitu movies.csv dan ratings.csv

movies.csv memiliki 9742 baris data dan 3 kolom dengan rincian sebagai berikut:

- movieid: id unique masing-masing film yang ada
- tittle: judul film
- genre: genre yang dimiliki oleh masing-masing film (satu film dapat memiliki lebih dari satu genre)

Sedangkan ratings.csv  memiliki 101000 baris data dan 4 kolom dengan rincian sebagai berikut:

- userid: id unique masing masing user yang ada
- movieid: id unique masing-masing film yang ada
- rating: nilai yang diberikan user terhadap suatu film
- timestamp: waktu dan tanggal pada saat user memberikan penilaian terhadap suatu film

# Exploratory data analysis

## Dataset movies.csv

Melihat bentuk dataset movies
"""

movies.shape

movies.head()

"""Memeriksa deskripsi variabel movies"""

movies.info()

movies.describe(include = 'all')

"""Melakukan cek null values dataset movies"""

movies.isnull().sum()

"""Melakukan cek duplikasi dataset movies"""

movies.duplicated().sum()

"""INSIGHT:

- Terdapat tahun rilis movie yang dapat dipisahkan menjadi kolom terpisah dengan tittle
- Tidak ditemukan missing value
- Tidak ditemukan duplikasi data
- Tidak ditemukan inaccurate value

## Dataset ratings

Melihat bentuk data ratings
"""

ratings.shape

ratings.head()

"""Memeriksa deskripsi variabel ratings"""

ratings.describe()

ratings.info()

"""Memeriksa missing value"""

ratings.isnull().sum()

"""Memeriksa duplikasi data"""

ratings.duplicated().sum()

"""INSIGHT:
- Tidak ditemukan missing value
- Tidak ditemukan duplikasi data
- Terdapat ketidaksesuaian tipe data pada kolom timestamp (int64) seharusnya bertipe datetime sebab merupakan waktu kapan rating diberikan.

### Melakukan cek distribusi rating
"""

plt.figure(figsize=(8, 4))
sns.countplot(x='rating', data=ratings)
plt.title("Distribusi Rating")
plt.xlabel("Rating")
plt.ylabel("Jumlah")
plt.show()

"""INSIGHT:
- Distribusi rating tidak berdistribusi normal, rating yang paling banyak diberikan adalah 4.0 dan yang paling sedikit diberikan adalah 0.5

### Analisis user

Memeriksa ada berapa jumlah user yang ada
"""

print("Jumlah user unik:", ratings['userId'].nunique())

"""Memeriksa user mana yang paling aktif"""

top_users = ratings['userId'].value_counts().head(10)
print("Top 10 pengguna paling aktif:\n", top_users)

"""Memeriksa distribusi jumlah film yang ditonton per user"""

user_activity = ratings['userId'].value_counts()
plt.figure(figsize=(8, 4))
sns.histplot(user_activity, bins=50, kde=True)
plt.title("Distribusi Jumlah Film yang Ditonton per User")
plt.xlabel("Jumlah Film")
plt.ylabel("Jumlah User")
plt.show()

"""INSIGHT:
- User yang ada berjumlah 610 user
- User yang paling aktif jika dilihat berdasarkan rating yang diberikan adalah user dengan userId 414
- Jumlah film yang ditonton tiap user cenderung dibawah 500 film, sangat sedikit user yang sudah menonton lebih dari 500 film

## Dataset movies dan ratings

### Analysis genre
"""

genres_expanded = movies['genres'].str.get_dummies(sep='|')
genre_counts = genres_expanded.sum().sort_values(ascending=False)


plt.figure(figsize=(10, 5))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.xticks(rotation=45)
plt.title("Distribusi Genre")
plt.xlabel("Genre")
plt.ylabel("Jumlah Film")
plt.show()


ratings_movies_genres = ratings.merge(movies, on='movieId')
ratings_movies_genres = ratings_movies_genres.join(genres_expanded)


genre_ratings = {}
for genre in genres_expanded.columns:
    genre_ratings[genre] = ratings_movies_genres[ratings_movies_genres[genre] == 1]['rating'].mean()

genre_ratings = pd.Series(genre_ratings).sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=genre_ratings.index, y=genre_ratings.values)
plt.xticks(rotation=45)
plt.title("Rata-rata Rating per Genre")
plt.xlabel("Genre")
plt.ylabel("Rata-rata Rating")
plt.show()

no_genre_movies = movies[movies['genres'] == '(no genres listed)']
print(no_genre_movies)

jumlah_tanpa_genre = (movies['genres'] == '(no genres listed)').sum()
print("Jumlah film tanpa genre:", jumlah_tanpa_genre)

persentase = 100 * jumlah_tanpa_genre / len(movies)
print(f"Persentase film tanpa genre: {persentase:.2f}%")

"""INSIGHT:

Ternyata setelah di cek, ada film yang tidak memiliki genre. dan berhubung film yang tidak memiliki genre hanyalah sedikit yaitu 0.35% maka dapat dihapus nantinya pada proses preprocessing data

Menghapus movie yang tidak memiliki genre
"""

moviesplot = movies[movies['genres'] != '(no genres listed)']

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



genres_expanded = moviesplot['genres'].str.get_dummies(sep='|')
genre_counts = genres_expanded.sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.xticks(rotation=45)
plt.title("Distribusi Genre Film")
plt.ylabel("Jumlah Film")
plt.xlabel("Genre")
plt.tight_layout()
plt.show()


ratings_movies = ratings.merge(moviesplot, on='movieId')
ratings_movies_genres = ratings_movies.join(genres_expanded)


genre_ratings = {}
for genre in genres_expanded.columns:
    avg = ratings_movies_genres[ratings_movies_genres[genre] == 1]['rating'].mean()
    genre_ratings[genre] = avg


genre_ratings = pd.Series(genre_ratings).sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=genre_ratings.index, y=genre_ratings.values)
plt.xticks(rotation=45)
plt.title("Rata-rata Rating per Genre")
plt.ylabel("Rata-rata Rating")
plt.xlabel("Genre")
plt.tight_layout()
plt.show()

"""INSIGHT:

Film yang ada didominasi oleh film dengan genre drama dan commedy, sedangkan film yang paling sedikit adalah film dengan genre film-noir. Dari segi rating, rata rata rating setiap genre yang terlihat tidak berbeda jauh, yakni sekitar 3.4 sampai 3.6, dengan film bergenre animation yang memiliki rata rata rating tertinggi.

### Melihat tren jumlah rating per tahun
"""

ratingsPlot = ratings
ratingsPlot['timestamp'] = pd.to_datetime(ratingsPlot['timestamp'], unit='s')
ratingsPlot['year'] = ratingsPlot['timestamp'].dt.year

ratings_per_year = ratingsPlot.groupby('year').size()

plt.figure(figsize=(10, 4))
ratings_per_year.plot()
plt.title("Jumlah Rating per Tahun")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Rating")
plt.grid()
plt.show()

"""INSIGHT:

Tahun 2000 adalah tahun dengan puncak pemberian rating paling tinggi jika didasarkan pada jumlah rating yang diberikan oleh user, hal ini juga berarti bahwa pada tahun inilah puncak terbanyak film yang ditonton oleh user. Meskpun trend sempat mengalami penurunan setelahnya pada tahun 2001 sampai dengan 2014, jumah rating yang diberikan kembali mengalami kenaikan meskipun tidak setinggi tahun 2000.

# Content based filtering

## data preprocessing & preparation

menyimpan data utama ke variabel baru khusus content based filtering
"""

cbf_df = movies

cbf_df.head()

cbf_df.shape

"""menghapus film yang tidak memiliki genre"""

cbf_df = cbf_df[cbf_df['genres'] != '(no genres listed)']

cbf_df.shape

"""## Modeling and Result

menerapkan TF-IDF Vectorizer
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data cuisine
tf.fit(cbf_df['genres'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(cbf_df['genres'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis genre
# Baris diisi dengan nama film

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=cbf_df.title
).sample(21, axis=1).sample(10, axis=0)

"""Menghitung derajat kesamaan dengan cosine similarity"""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa namafilm
cosine_sim_df = pd.DataFrame(cosine_sim, index=cbf_df['title'], columns=cbf_df['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap film
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""membuat fungsi movie recommendations"""

def movie_recommendations(judul_film, similarity_data=cosine_sim_df, items=cbf_df[['title', 'genres']], k=10):
    """
    Rekomendasi film berdasarkan kemiripan dataframe

    Parameter:
    ---
    judul_film : tipe data string (str)
            judul film (index kemiripan dataframe)

    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan film sebagai
                      indeks dan kolom

    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan

    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,judul_film].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(judul_film, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""mendapatkan rekomendasi"""

cbf_df[cbf_df.title.eq('Jumanji (1995)')]

movie_recommendations('Jumanji (1995)')

"""## Evaluation

Matrik evaluasi yang digunakan adalah precision. Precision bekerja dengan mengukur proporsi item yang direkomendasikan yang benar-benar relevan. Rumus precision adalah:

![image](https://github.com/user-attachments/assets/3fdf7a08-a69f-46e9-9b1c-1b3d123d3d91)

dengan mengikuti rumus tersebut, maka dapat menghitung precision dari content based filtering yang sudah berhasil dibangun. Yakni ada 10 item yang relevant dari 10 rekomendasi yang diberikan. Artinya nilai precision dari model tersebut adalah 100%.

# Collaborative filtering

## Data preprocessing & preparation

Menggabungkan dataset movies dan ratings menjadi satu
"""

all_df = movies.merge(ratings, on='movieId')

all_df.head()

all_df.shape

"""Menghapus movie yang tidak memiliki genre"""

all_df = all_df[all_df['genres'] != '(no genres listed)']

all_df.shape

"""Encoding userId"""

# Mengubah userID menjadi list tanpa nilai yang sama
user_ids = all_df['userId'].unique().tolist()
print('list userID: ', user_ids)

# Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userID : ', user_to_user_encoded)

# Melakukan proses encoding angka  ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userID: ', user_encoded_to_user)

"""Encoding movieId"""

# Mengubah movieID menjadi list tanpa nilai yang sama
movie_ids = all_df['movieId'].unique().tolist()
print('list movieID: ', movie_ids)

# Melakukan proses encoding movieUd
movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}
print('encoded movieID :' , movie_to_movie_encoded)

# Melakukan proses encoding angka ke movieID
movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}
print('encoded angka ke movieID ', movie_encoded_to_movie)

"""Mapping user id dan movie id ke dataframe yang berkaitan"""

# Mapping userID ke dataframe user
all_df['user'] = all_df['userId'].map(user_to_user_encoded)

# Mapping movieID ke dataframe movie
all_df['movie'] = all_df['movieId'].map(movie_to_movie_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah film
num_movie = len(movie_encoded_to_movie)
print(num_movie)

# Nilai minimum rating
min_rating = min(all_df['rating'])

# Nilai maksimal rating
max_rating = max(all_df['rating'])

print('Number of User: {}, Number of movie: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_movie, min_rating, max_rating
))

"""Membagi data training dan validasi"""

# Mengacak dataset
all_df = all_df.sample(frac=1, random_state=42)
all_df

# Membuat variabel x untuk mencocokkan data user dan movie menjadi satu value
x = all_df[['user', 'movie']].values

# Membuat variabel y untuk membuat rating dari hasil
y = all_df['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * all_df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""## Modeling and Result

membuat class RecommenderNet dengan keras Model class
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_movie, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_movie = num_movie
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1)
    self.movie_embedding = layers.Embedding(
        num_movie,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.movie_bias = layers.Embedding(num_movie, 1)

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    movie_vector = self.movie_embedding(inputs[:, 1]) # memanggil layer embedding 3
    movie_bias = self.movie_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_movie = tf.tensordot(user_vector, movie_vector, 2)

    x = dot_user_movie + user_bias + movie_bias

    return tf.nn.sigmoid(x) # activation sigmoid

"""compile model"""

model = RecommenderNet(num_users, num_movie, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Memulai training"""

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 10,
    validation_data = (x_val, y_val)
)

"""Mendapatkan rekomendasi film"""

import numpy as np

movie_df = movies

# Mengambil sample user
user_id = 325
movie_watch_by_user = all_df[all_df.userId == user_id]

movie_not_visited = movie_df[~movie_df['movieId'].isin(movie_watch_by_user.movieId.values)]['movieId']
movie_not_visited = list(
    set(movie_not_visited)
    .intersection(set(movie_to_movie_encoded.keys()))
)

movie_not_visited = [[movie_to_movie_encoded.get(x)] for x in movie_not_visited]
user_encoder = user_to_user_encoded.get(user_id)
user_movie_array = np.hstack(
    ([[user_encoder]] * len(movie_not_visited), movie_not_visited)
)

ratings = model.predict(user_movie_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movie_ids = [
    movie_encoded_to_movie.get(movie_not_visited[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Movie with high ratings from user')
print('----' * 8)

top_movie_user = (
    movie_watch_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .movieId.values
)

movie_df_rows = movie_df[movie_df['movieId'].isin(top_movie_user)]
for row in movie_df_rows.itertuples():
    print(row.title, ':', row.genres)

print('----' * 8)
print('Top 10 movie recommendation')
print('----' * 8)

recommended_movie = movie_df[movie_df['movieId'].isin(recommended_movie_ids)]
for row in recommended_movie.itertuples():
    print(row.title, ':', row.genres)

"""Berdasarkan rekomendasi film yang diberikan oleh model, dapat dilihat hasil rekomendasinya cukup baik dan sesuai dengan preferensi user id 325. Hal ini terbukti melalui genre movie yang direkomendasikan konsisten selalu memiliki keterkaitan dengan genre movie yang mendapatkan rating tinggi oleh user.

## Evaluasi

Visualisasi metrik
"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""berdasarkan visualisasi di atas, dapat diketahui bahwa proses training model cukup smooth dan model konvergen pada epochs sekitar 10. Dari proses ini, diperoleh nilai error akhir pada proses training sebesar sekitar 0.1822 dan error pada data validasi sebesar 0.1957. Nilai tersebut cukup bagus untuk sistem rekomendasi. Hal ini semakin diperkuat dengan bukti rekomendasi yang cukup relevan pada saat dilakukan uji coba mendapatkan rekomendasi film."""