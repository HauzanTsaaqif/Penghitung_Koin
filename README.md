# Penghitung Koin

Pada sektor perbankan dan industri vending machine, penghitungan koin menjadi sebuah tugas yang krusial namun seringkali melibatkan kesalahan dan memakan waktu. Metode penghitungan manual cenderung rentan terhadap kesalahan manusia, terutama dalam konteks jumlah yang besar. Oleh karena itu, hadirnya aplikasi Dekstop Penghitung Koin Berbasis Kecerdasan Buatan menjadi solusi inovatif untuk mengatasi tantangan ini. Dengan mengimplementasikan kecerdasan buatan, aplikasi ini dapat membedakan jenis koin berdasarkan karakteristik fisiknya, seperti ukuran, bentuk, dan warna, serta secara otomatis menghitung jumlah koin dan nilai berdasarkan denominasi yang telah ditentukan.

Aplikasi ini dikembangkan dengan alasan utama untuk meningkatkan efisiensi dan akurasi penghitungan koin dalam konteks pekerjaan perbankan. Penghitungan koin yang cepat dan akurat sangat penting untuk menghindari kesalahan manusia yang dapat muncul dalam metode manual, sekaligus meningkatkan efisiensi waktu dalam pekerjaan perbankan. Selain itu, kemampuan aplikasi untuk diintegrasikan dengan vending machine memberikan kemudahan dalam pengelolaan koin pada mesin tersebut. Dengan adanya integrasi, vending machine dapat secara otomatis menghitung dan melaporkan jumlah koin yang diterima, menyederhanakan proses pengelolaan inventaris dan akuntansi.

Aplikasi Dekstop Penghitung Koin Berbasis Kecerdasan Buatan membawa sejumlah manfaat yang diharapkan dapat mengoptimalkan proses penghitungan koin. Diantaranya adalah penghematan waktu, akurasi tinggi dalam identifikasi dan penghitungan koin, kemudahan integrasi dengan sistem perbankan dan vending machine, pengurangan risiko kesalahan manusia, serta peningkatan produktivitas dan efisiensi operasional di sektor-sektor terkait. Dengan kombinasi latar belakang yang kuat dan manfaat yang ditawarkan, aplikasi ini diharapkan dapat menjadi solusi efektif untuk menyederhanakan dan meningkatkan pengelolaan koin dalam berbagai konteks industri.

# Cara Instalasi

### 1. Pull atau download source code dari github.
### 2. Install requirement library yang dibutuhkan.
### 3. Buka main.py dan jalankan program.
### 4. Coba aplikasi dengan background berwarna hitam dan penerangan yang cukup.

# Proses Pembuatan
#### 1. Gathering data atau mengumpulkan data satu persatu
![Gambar Kumpulan data yang digunakan](hasil_pengukuran/img_1.png)
#### 2. Labeling Image atau memberikan label pada object yang ingin dideteksi
![Gambar Contoh Labeling Image](hasil_pengukuran/img_5.png)
#### 3. Setting model stuktur yang akan digunakan
#### 4. Proses training data menggunakan data yang telah disiapkan sebelumnya dan struktur model yang telah disetting
![Gambar Grafik Training Model](hasil_pengukuran/img_3.png)
#### 5. Konversi hasil training kedalam 1 file tensorflow lite
#### 6. Hitung presisi dari model yang telah didapatkan
![Gambar Hasil Pengukuran Model](hasil_pengukuran/img_2.png)
#### 7. Tambatkan model pada suatu aplikasi agar dapat menerima input dan menampilkan output
![Gambar Contoh Hasil Implementasi](example/example_2.png)
![Gambar Contoh Hasil Implementasi](example/example_1.png)
![Gambar Contoh Hasil Implementasi](example/example_3.png)
