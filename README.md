# Laporan Proyek Machine Learning - Naufal Dzakwan Zakianto

## Project Overview

Saat ini industri film sudah berkembang sangat cepat, jika dahulu para penikmat film diharuskan untuk datang ke bioskop atau membeli vcd untuk dapat menikmati film, kini industri film sudah mengalami digitalisasi. Perusahaan besar yang menyediakan tempat atau platform untuk menikmati film mulai bermunculan, seperti Netflix, Youtube, maupun Amazon. Perkembangan yang pesat tentunya juga mengakibatkan bertambahnya produksi film secara masif setiap tahunnya, sehingga pengguna mengalami kesulitan dalam menemukan film yang sesuai dengan preferensi mereka. Untuk mengatasi permasalahan tersebut, banyak perusahaan menggunakan sistem rekomendasi agar mereka dapat melayani pengguna dengan lebih baik dan meningkatkan keuntungan mereka (Sunilkumar, 2020). Hal ini karena sistem rekomendasi dapat membantu menyaring ribuan opsi dan menyajikan film yang sesuai dengan selera pengguna. Sejalan dengan kebutuhan tersebut, proyek ini bertujuan untuk mengembangkan sistem rekomendasi menggunakan dua pendekatan utama, yaitu content-based filtering dan collaborative filtering.

Referensi:

Sunilkumar, C. N. (2020). A review of movie recommendation system: Limitations, Survey and Challenges. ELCVIA Electronic Letters on Computer Vision and Image Analysis, 19(3), 18–37. https://doi.org/10.5565/rev/elcvia.1232


## Business Understanding
### Problem Statements

1. Bagaimana cara memberikan rekomendasi film yang relevan kepada pengguna berdasarkan preferensi mereka?

2. Bagaimana memanfaatkan data rating pengguna dan data film untuk menghasilkan rekomendasi yang akurat?

### Goals

1. Membangun sistem rekomendasi yang dapat memberikan daftar 10 film terbaik untuk pengguna.

2. Mengimplementasikan dua pendekatan berbeda: content-based filtering dan collaborative filtering.

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

   **Distribusi genre dan rata rata rating genre setelah di filter hanya film yang memiliki genre saja

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
### Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
