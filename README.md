# Laporan Proyek Machine Learning - Naufal Dzakwan Zakianto

## Project Overview

Saat ini industri film sudah berkembang sangat cepat, jika dahulu para penikmat film diharuskan untuk datang ke bioskop atau membeli vcd untuk dapat menikmati film, kini industri film sudah mengalami digitalisasi. Perusahaan besar yang menyediakan tempat atau platform untuk menikmati film mulai bermunculan, seperti Netflix, Youtube, maupun Amazon. Perkembangan yang pesat tentunya juga mengakibatkan bertambahnya produksi film secara masif setiap tahunnya, sehingga pengguna mengalami kesulitan dalam menemukan film yang sesuai dengan preferensi mereka. Untuk mengatasi permasalahan tersebut, banyak perusahaan menggunakan sistem rekomendasi agar mereka dapat melayani pengguna dengan lebih baik dan meningkatkan keuntungan mereka (Sunilkumar, 2020). Hal ini karena sistem rekomendasi dapat membantu menyaring ribuan opsi dan menyajikan film yang sesuai dengan selera pengguna. Sejalan dengan kebutuhan tersebut, proyek ini bertujuan untuk mengembangkan sistem rekomendasi menggunakan dua pendekatan utama, yaitu content-based filtering dan collaborative filtering.

Referensi:

Sunilkumar, C. N. (2020). A review of movie recommendation system: Limitations, Survey and Challenges. ELCVIA Electronic Letters on Computer Vision and Image Analysis, 19(3), 18–37. https://doi.org/10.5565/rev/elcvia.1232


## Business Understanding
### Problem Statements

1. Berdasarkan data mengenai pengguna, bagaimana membuat sistem rekomendasi yang dipersonalisasi dengan teknik content-based filtering?
2. Dengan data rating yang dimiliki, bagaimana cara agar dapat merekomendasikan film lain yang mungkin disukai dan belum pernah ditonton oleh pengguna? 

### Goals

1. Menghasilkan sejumlah rekomendasi film yang dipersonalisasi untuk pengguna dengan teknik content-based filtering.
2. Menghasilkan sejumlah rekomendasi film yang sesuai dengan preferensi pengguna dan belum pernah ditonton sebelumnya dengan teknik collaborative filtering
   
### Solution approach

1. Content-Based Filtering: Menggunakan metadata film (genre) untuk merekomendasikan film yang mirip dengan yang disukai pengguna.
2. Collaborative Filtering: Menggunakan data rating dari pengguna lain untuk merekomendasikan film yang mungkin disukai oleh pengguna serupa.

## Data Understanding
Data yang digunakan adalah data movies and ratings, data ini berasal dari kaggle yang dapat di akses melalui: https://www.kaggle.com/datasets/nicoletacilibiu/movies-and-ratings-for-recommendation-system

Data tersebut memiliki 2 buah dataset yaitu movies.csv dan ratings.csv

movies.csv memiliki 9742 baris data dan 3 kolom dengan rincian sebagai berikut:
- movieid: id unique masing-masing film yang ada
- tittle: judul film
- genre: genre yang dimiliki oleh masing-masing film (satu film dapat memiliki lebih dari satu genre)
  
Sedangkan ratings.csv memiliki 101000 baris data dan 4 kolom dengan rincian sebagai berikut:

-  userid: id unique masing masing user yang ada
- movieid: id unique masing-masing film yang ada
- rating: nilai yang diberikan user terhadap suatu film
- timestamp: waktu dan tanggal pada saat user memberikan penilaian terhadap suatu film

**Exploratory Data Analysis movies.csv**:
1. Melihat bentuk data movies.csv
   
   ![image](https://github.com/user-attachments/assets/12aac807-2a6e-405f-b0c4-c92c234dd464)

2. Memeriksa deskripsi variabel movies.csv

   ![image](https://github.com/user-attachments/assets/002c58d8-d23b-4744-a8fc-0cb43700af79)
   
   ![image](https://github.com/user-attachments/assets/9777aef4-ecdc-434b-ac2a-197c9b38da5a)

3. Memeriksa null values movies.csv

   ![image](https://github.com/user-attachments/assets/1ec36d61-c035-4c56-928a-1246c7449728)

4. Memeriksa duplikasi movies.csv

   ![image](https://github.com/user-attachments/assets/6e31ca3c-40ed-47a9-a77d-dded8de45c89)

**INSIGHT:**
- Terdapat tahun rilis movie yang dapat dipisahkan menjadi kolom terpisah dengan tittle
- Tidak ditemukan missing value
- Tidak ditemukan duplikasi data
- Tidak ditemukan inaccurate value

**Exploratory Data Analysis ratings.csv**:

1. Melihat bentuk data ratings.csv
   
   ![image](https://github.com/user-attachments/assets/5d4d304d-3a6c-492b-a75d-7d896ba5e318)

2. Memeriksa deskripsi variabel ratings.csv

   ![image](https://github.com/user-attachments/assets/f166b934-ded4-436d-b132-2cdc138fb387)

3. Memeriksa missing value ratings.csv

   ![image](https://github.com/user-attachments/assets/b24c505c-afc3-4d9b-ba3a-936d14f4b375)

4. Memeriksa duplikasi data ratings.csv

   ![image](https://github.com/user-attachments/assets/8b6ebf69-0de6-445c-a270-54d675c26b11)

**INSIGHT:**
- Tidak ditemukan missing value
- Tidak ditemukan duplikasi data
- Terdapat ketidaksesuaian tipe data pada kolom timestamp (int64) seharusnya bertipe datetime sebab merupakan waktu kapan rating diberikan.

5. Melakukan cek distribusi rating

   ![image](https://github.com/user-attachments/assets/05dba023-0420-424a-b8c7-424607f85517)

**INSIGHT:**
  - Distribusi rating tidak berdistribusi normal, rating yang paling banyak diberikan adalah 4.0 dan yang paling sedikit diberikan adalah 0.5

6. Memeriksa ada berapa jumlah user yang ada

   ![image](https://github.com/user-attachments/assets/51f08d3b-1a4f-4444-8aa1-3207f56af934)

7. Memeriksa user mana yang paling aktif

   ![image](https://github.com/user-attachments/assets/4d9fde3a-40a1-40b4-b3b6-7dc5bb2bcc79)

8. Memeriksa distribusi jumlah film yang ditonton per user

   ![image](https://github.com/user-attachments/assets/a7421bd9-f5ad-4898-b5c0-fa40fdd58b6e)

**INSIGHT:**
- User yang ada berjumlah 610 user
- User yang paling aktif jika dilihat berdasarkan rating yang diberikan adalah user dengan userId 414
- Jumlah film yang ditonton tiap user cenderung dibawah 500 film, sangat sedikit user yang sudah menonton lebih dari 500 film

**Multivariate Data Analysis (movies.csv dan ratings.csv)**:
1. Analysis genre
   
   ![image](https://github.com/user-attachments/assets/6290ebd9-dab2-4051-aed6-fa6497ddc949)

   ![image](https://github.com/user-attachments/assets/57cc84d4-7169-4b26-9085-9574de31c5e8)

   ![image](https://github.com/user-attachments/assets/028a394b-793b-4d39-bd1f-37710dc16204)

   **INSIGHT:**
   
   Ternyata setelah di cek, ada film yang tidak memiliki genre. dan berhubung film yang tidak memiliki genre hanyalah sedikit yaitu 0.35% maka dapat dihapus
   nantinya pada proses preprocessing data

   **Distribusi genre dan rata rata rating genre setelah di filter hanya film yang memiliki genre saja**

   ![image](https://github.com/user-attachments/assets/8f006f1e-caf4-46c7-bca7-f4fa4d79295c)

   ![image](https://github.com/user-attachments/assets/641197ed-7b63-47fc-9338-97ec0153edc8)

   **INSIGHT:**

   Film yang ada didominasi oleh film dengan genre drama dan commedy, sedangkan film yang paling sedikit adalah film dengan genre film-noir. Dari segi rating,
   rata rata rating setiap genre yang terlihat tidak berbeda jauh, yakni sekitar 3.4 sampai 3.6, dengan film bergenre animation yang memiliki rata rata rating
   tertinggi.

2. Melihat tren jumlah rating per tahun

   ![image](https://github.com/user-attachments/assets/4b305d24-ac6b-4c47-903d-1736b6194144)

   **INSIGHT:**
   
   Tahun 2000 adalah tahun dengan puncak pemberian rating paling tinggi jika didasarkan pada jumlah rating yang diberikan oleh user, hal ini juga berarti bahwa
   pada tahun inilah puncak terbanyak film yang ditonton oleh user. Meskpun trend sempat mengalami penurunan setelahnya pada tahun 2001 sampai dengan 2014, jumah
   rating yang diberikan kembali mengalami kenaikan meskipun tidak setinggi tahun 2000.


## Content based filtering
### Data Pre-processing & Preparation

1. Menyimpan data utama ke variabel baru khusus content based filtering

Di tahap ini data utama dari movies.csv di copy ke variabel baru khusus untuk persiapan content based filtering, hal ini perlu dilakukan karena proses preprocessing maupun preparation data pada content based filtering berbeda dengan collaborative filtering, sehingga tahapan ini berfungsi agar data asli tidak terpengaruh oleh perubahan yang dilakukan pada proses pembangunan content based filtering dan data asli dapat digunakan kembali untuk membangun collaborative filtering.

2. Menghapus film yang tidak memiliki genre

Dilakukan penghapusan film yang  genrenya adalah 'no genre listed', dengan memfilter hanya film yang memiliki genre saja yang boleh disimpan ke dataframe. Hal ini dilakukan karena content based filtering akan memanfaatkan genre untuk memberikan rekomendasi film yang disukai oleh user berdasarkan preferensi mereka, apabila terdapat film yang tidak memiliki genre, maka tentunya hal ini akan menyulitkan dan tidak bisa digunakan dalam pembangunan content based filtering.

### Modeling

Content-based filtering adalah metode yang digunakan dalam sistem rekomendasi yang berfokus pada karakteristik atau konten dari item-item yang ingin direkomendasikan. Dalam proyek ini fitur item yang digunakan untuk menentukan kesamaan item yang ada dan preferensi pengguna adalah 'genre' film.

Kelebihan dari pendekatan ini adalah hanya membutuhkan informasi tentang item dan preferensi pengguna, sehingga tidak bergantung pada data dari pengguna lain dan content-based filtering dapat memberikan rekomendasi bahkan untuk pengguna baru yang belum memiliki banyak interaksi. Sedangkan kekurangannya ialah pengguna mungkin hanya mendapatkan rekomendasi yang mirip dengan item yang sudah mereka sukai, sehingga mengurangi kemungkinan menemukan item baru yang berbeda.

proses model development content based filtering dilakukan dengan tahapan berikut:


1. Menerapkan TF-IDF vectorizer

   TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer adalah teknik yang digunakan dalam pemrosesan bahasa alami (NLP) untuk mengubah teks menjadi representasi numerik. Hal ini perlu dilakukan karena
   TF-IDF membantu mengidentifikasi kata-kata yang lebih relevan dalam data, sehingga sistem rekomendasi dapat lebih akurat dalam memahami konten yang disukai pengguna, selain itu TF-IDF juga dapat memungkinkan
   sistem untuk bekerja dengan representasi numerik yang lebih efisien, sehingga mempermudah perhitungan kesamaan antar data, dalam hal ini adalah judul film dengan genre film.

2. Menghitung derajat kesamaan dengan cosine similarity

   Setelah matrix tfidf sudah terbentuk selanjutnya dapat dihitung derajat kesamaan antar matrixnya dengan memanfaatkan cosine
   similarity, hasil akhirnya akan menjadi array 2 dimensi seperti berikut:

   ![image](https://github.com/user-attachments/assets/cd4b66b0-03d7-437c-b5ae-3d5e06a9a198)

   untuk lebih memahami penggunaan dan intepretasinya, hasil tersebut dapat di plot ke dataframe dengan baris dan kolom berupa nama
   film seperti berikut:

   ![image](https://github.com/user-attachments/assets/cb416ed9-1d56-4a83-a510-76f9b3630b60)

   dari gambar di atas, dapat diketahui derajat kesamaan antar film yang ada. Contohnya jika ada user yang menyukai film Everything Is Illuminated (2005) maka kemungkinan sistem akan merekomendasikan film One-Way Ticket to Mombasa (Menolippu Mombasaan) (2002), karena nilai derajat kesamaan kedua film tersebut adalah 1.

3. Membuat fungsi movie recommendations

   fungsi recommendations yang digunakan dalam proyek ini memiliki struktur sebagai berikut:   

   def movie_recommendations(judul_film, similarity_data=cosine_sim_df, items=cbf_df[['title', 'genres']], k=10):

   fungsi ini memiliki peran untuk memberikan rekomendasi film berdasarkan kemiripan dataframe yang didasarkan pada nilai cosine
   similarity terbesar.

   parameter dari fungsi tersebut adalah:

   - judul_film : tipe data string (str), merupakan judul film berdasarkan (index kemiripan dataframe)

   - similarity_data : tipe data pd.DataFrame (object), Kesamaan dataframe, simetrik, dengan film sebagai indeks dan kolom

   - items : tipe data pd.DataFrame (object), Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
     (tittle dan genre)

   - k : tipe data integer (int), banyaknya jumlah rekomendasi yang diberikan

4. Mendapatkan rekomendasi
   
   Untuk mendapatkan rekomendasi, hal pertama yang perlu dilakukan adalah menentukan judul film yang ingin menjadi acuan dalam
   memberikan rekomendasi, misalnya disini akan digunakan film Jumanji (1995)

   ![image](https://github.com/user-attachments/assets/f0b01b70-99bd-441f-bc8a-7bb2ce1f754b)

   maka setelah itu, dapat langsung gunakan fungsi yang sudah di definisikan sebelumnya. Sehingga sistem akan mengeluarkan 10
   rekomendasi film sesuai dengan film acuan yang sudah ditentukan.

   ![image](https://github.com/user-attachments/assets/c48ef345-2783-4884-9901-af810b2bd949)

   Melalui gambar di atas, dapat dilihat bahwa sistem berhasil memberikan 10 rekomendasi film yang karakteristik genrenya sama seperti
   film Jumanji (1995) yakni 	Adventure, Children dan Fantasy.

### Evaluation
Matrik evaluasi yang digunakan adalah precision. Precision bekerja dengan mengukur proporsi item yang direkomendasikan yang benar-benar relevan. Rumus precision adalah:

![image](https://github.com/user-attachments/assets/3fdf7a08-a69f-46e9-9b1c-1b3d123d3d91)

dengan mengikuti rumus tersebut, maka dapat menghitung precision dari content based filtering yang sudah berhasil dibangun. Yakni ada 10 item yang relevant dari 10 rekomendasi yang diberikan. Artinya nilai precision dari model tersebut adalah 100%.

## Collaborative Filtering

### Data Pre-processing & Preparation
1. Menggabungkan dataset movies dan ratings menjadi satu
   
   ![image](https://github.com/user-attachments/assets/94008b15-fc29-471b-be11-7f55e8287991)

   Karena dataset film dan ratings pada priyek ini masih terpisah, maka perlu dilakukan penggabungan menjadi satu kesatuan dataframe.
   Penggabungan dataset memungkinkan sistem untuk menghubungkan informasi tentang film (judul dan genre) dengan rating yang
   diberikan oleh pengguna. Ini penting untuk memahami preferensi pengguna terhadap berbagai film.

2. Encoding user id
   
   Encoding user ID adalah proses mengubah identifikasi pengguna menjadi format numerik atau kategori yang dapat diproses oleh
   algoritma. Hal ini perlu dilakukan karena Algoritma collaborative filtering, membutuhkan data dalam
   format numerik untuk melakukan perhitungan kesamaan dan prediksi.

   ![image](https://github.com/user-attachments/assets/baa23bf4-fd92-4d52-87e5-f32e4e1b1560)

   
4. Encoding movie Id

   Encoding movie ID adalah proses mengubah identifikasi film menjadi format numerik atau kategori yang dapat diproses oleh
   algoritma. Hal ini perlu dilakukan karena Algoritma collaborative filtering, membutuhkan data dalam
   format numerik untuk melakukan perhitungan kesamaan dan prediksi. Selain itu Encoding movie ID juga memastikan bahwa setiap film
   memiliki representasi yang konsisten di seluruh dataset.

5. Mapping user id dan movie id ke dataframe yang berkaitan

   Proses ini adalah melakukan mapping hasil encode yang sudah dilakukan sebelumnya ke dalam dataset. Proses ini perlu dilakukan agar
   sistem daoat mengakses dan menganalisis data secara bersamaan. Memastikan bahwa setiap pengguna dan film memiliki representasi yang
   konsisten di seluruh dataset.

6. Membagi data training dan validasi

   Proses ini adalah membagi dataset menjadi dua bagian, 80% data training dan 20% data validasi. Data training digunakan untuk melatih
   model. Model belajar dari data ini untuk memahami pola dan hubungan antara pengguna dan item. Sedangkan data validasi digunakan
   untuk mengevaluasi performa model selama proses pelatihan. Proses ini perlu dilakukan untuk memastikan model tidak overfitting dan
   dapat menggeneralisasi dengan baik pada data yang belum pernah dilihat sebelumnya.
   
### Modelling and Result

Collaborative filtering adalah teknik yang digunakan dalam sistem rekomendasi untuk memprediksi preferensi pengguna berdasarkan kesamaan dengan pengguna lain. Kelebihan dari teknik ini adalah dapat menemukan item yang tidak terduga tetapi sesuai dengan selera pengguna. Namun kekurangannya adalah kesulitan memberikan rekomendasi untuk pengguna baru yang belum memiliki riwayat preferensi serta memerlukan komputasi yang besar untuk data pengguna yang banyak.

1. Membuat class RecommenderNet dengan keras Model class
   
   Pada tahap ini, model menghitung skor kecocokan antara pengguna dan resto dengan teknik embedding. Pertama, dilakukan proses
   embedding terhadap data user dan movie. Selanjutnya, dilakukan operasi perkalian dot product antara embedding user dan movie. Selain
   itu, ditambahkan bias untuk setiap user dan movie. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid.

3. Compile model

   Model ini menggunakan Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer, dan
   root mean squared error (RMSE) sebagai metrics evaluation.
   
4. Memulai training model

   ![image](https://github.com/user-attachments/assets/d7229125-9942-41b9-99ba-6ec616fde78e)

5. Mendapatkan rekomendasi
   Setelah proses pelatihan selesai, model dapat memberikan 10 rekomendasi yang sesuai dengan preferensi pengguna. Untuk menguji hasil
   rekomendasinya, digunakan percobaan terhadap user dengan id 325.

   ![image](https://github.com/user-attachments/assets/a1c0c87a-7d36-40b9-ae56-d85859080607)

   Berdasarkan gambar di atas, dapat dilihat hasil rekomendasinya cukup baik dan sesuai dengan preferensi user dengan id 325.

### Evaluation

Metrik yang digunakan untuk evaluasi pada proyek ini adalah Root Mean Square Error (RMSE). Metrik tersebut adalah metrik yang digunakan untuk mengukur seberapa baik model prediktif mendekati nilai aktual. RMSE memberikan ukuran rata-rata kesalahan kuadrat dari prediksi model, memberikan bobot lebih besar pada kesalahan yang lebih besar. 

Formula dari RMSE adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/3a3516b2-17ec-41f4-9c38-713fbba9b9cc)

Di mana:
- n adlaah jumlah sample dalam data
- yi adalah nilai aktual
- yi^ adalah nilai prediksi

Hasil proyek berdasarkan metrik evaluasi dapat dilihat melalui visualisasi berikut:

![image](https://github.com/user-attachments/assets/f13c4a81-ff67-49d2-96dd-be0c1863f347)

berdasarkan visualisasi di atas, dapat diketahui bahwa proses training model cukup smooth dan model konvergen pada epochs sekitar 8. Dari proses ini, diperoleh nilai error akhir sebesar sekitar 0.1806 dan error pada data validasi sebesar 0.1953. Nilai tersebut cukup bagus untuk sistem rekomendasi. Hal ini semakin diperkuat dengan bukti rekomendasi yang cukup relevan pada saat dilakukan uji coba mendapatkan rekomendasi film.




   





