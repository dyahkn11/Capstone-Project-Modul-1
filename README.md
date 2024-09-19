**Capstone Project: Aplikasi CRUD Data Pelanggan Toko**

**Overview**
- Proyek ini adalah aplikasi CRUD (Create, Read, Update, Delete) sederhana untuk mengelola data pelanggan toko. Data pelanggan yang dikelola meliputi Nama, Jenis Kelamin, Nomor Telepon, Lokasi Kota, dan Tanggal Lahir. Aplikasi ini dibuat menggunakan Python dan menyimpan data pelanggan dalam format JSON.

**Main Function**
1. read_customers(): Fungsi ini membaca data pelanggan dari file data.json. Jika file belum ada atau kosong, maka akan dibuat data awal dengan format kosong.
2. update_customers(): Menyimpan perubahan data pelanggan (misalnya setelah penambahan atau pengeditan) ke dalam file data.json.

**Main Features**
1. Create: Menambahkan pelanggan baru ke daftar. Setiap pelanggan diberi ID unik secara otomatis, dan pengguna memasukkan data lainnya seperti nama, jenis kelamin, nomor telepon, kota, dan tanggal lahir.
2. Read: Membaca dan menampilkan semua data pelanggan yang tersimpan di file JSON dengan menggunakan fungsi pprint untuk memformat tampilan data.
3. Update: Mengedit data pelanggan berdasarkan ID yang diberikan. Jika pelanggan ditemukan, program meminta pengguna memasukkan data baru untuk menggantikan yang lama.
4. Delete: Menghapus pelanggan dari daftar berdasarkan ID yang diberikan. Setelah ditemukan, pelanggan akan dihapus dari file JSON.
5. Exit: Menyimpan data ke file JSON dan keluar dari aplikasi.

**Program Flow**
1. Memulai Program: Saat program dijalankan, aplikasi akan membaca data dari file data.json jika sudah ada, atau membuat file baru jika belum ada.
2. Menu Pilihan: Program menampilkan menu untuk pengguna memilih opsi:
   - Membuat pelanggan baru
   - Membaca data pelanggan
   - Memperbarui data pelanggan
   - Menghapus pelanggan
   - Keluar dari aplikasi
3. Proses CRUD: Setiap kali pengguna memilih salah satu opsi, program akan mengeksekusi fungsi yang sesuai:
   - _Create new customer_: Pilih opsi 1 dari opsi yang tersedia: 1-5. Ikuti instruksi di aplikasi untuk memasukkan data pelanggan baru (Nama, Jenis Kelamin, Nomor Telepon, Kota, dan Tanggal Lahir).
   - _Read customer data_: Pilih opsi 2 untuk menampilkan semua data pelanggan yang tersimpan.
   - _Update customer data_: Pilih opsi 3 untuk memperbaharui data pelanggan. Pilih pelanggan yang ingin diperbarui berdasarkan customer ID, lalu ikuti instruksi untuk memperbarui informasinya.
   - _Delete existing customer_: Pilih opsi 4 dan masukkaan customer ID dari data pelanggan terkait yang ingin dihapus.
   -_ Exit application_: Pilih opsi 5 untuk menyimpan data dan keluar dari aplikasi.
     
![image](https://github.com/user-attachments/assets/ac158ab2-105b-4893-b560-d89e650418f6)

**Technologies Used**
- Programming Language: Python
- Database: JSON (untuk penyimpanan data lokal)
- Virtual Environment: Python venv
  
**Installation**
1. Clone Repositori: Clone repositori ini ke direktori lokal.
2. Buat dan Aktifkan Virtual Environment: Buat virtual environment untuk mengelola dependensi dan aktifkan virtual environment.
3. Install Dependensi: Install semua dependensi yang diperlukan dari file requirements.txt.
4. Jalankan Aplikasi: Setelah semua siap, jalankan aplikasi.

**Customer Data Structure**
- Data pelanggan disimpan dalam file JSON dengan struktur sebagai berikut:
![image](https://github.com/user-attachments/assets/676da219-0e49-4804-9fa1-92e595fb99f2)
