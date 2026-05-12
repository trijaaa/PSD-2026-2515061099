Tugas Akhir Percobaan 3 : Searching

Judul Proyek : Sistem Pencari Kontak

Program ini dibuat untuk membantu pengguna dalam mengelola data kontak secara sederhana menggunakan bahasa pemrograman Python. Dalam kehidupan sehari-hari, sering kali seseorang membutuhkan tempat untuk menyimpan nomor telepon atau informasi kontak agar lebih mudah dicari dan diakses kembali. Oleh karena itu, dibuatlah sistem sederhana yang mampu melakukan penyimpanan, pencarian, penambahan, serta penghapusan kontak secara otomatis dan terstruktur.

Pada implementasinya, program ini memanfaatkan struktur data berupa dictionary untuk menyimpan data kontak yang terdiri dari nama dan nomor telepon. Program juga menggunakan metode searching untuk mencari data kontak berdasarkan nama yang dimasukkan pengguna. Proses pencarian dilakukan dengan perulangan dan perbandingan teks secara fleksibel menggunakan fungsi lower(), sehingga pencarian tetap dapat dilakukan meskipun terdapat perbedaan huruf besar dan kecil.

Selain fitur pencarian, program juga dilengkapi dengan menu interaktif yang memungkinkan pengguna melihat seluruh daftar kontak, menambahkan kontak baru, serta menghapus kontak yang sudah tidak diperlukan. Program turut menggunakan validasi pilihan menu agar input yang dimasukkan sesuai dengan opsi yang tersedia, sehingga dapat meminimalisir kesalahan saat program dijalankan.

Dengan adanya program ini, pengguna dapat lebih mudah dalam mengelola daftar kontak secara praktis dan terorganisir. Sistem ini diharapkan dapat membantu meningkatkan efisiensi pengguna dalam menyimpan serta mencari informasi kontak dengan lebih cepat dan sederhana.

Source Code:

<img width="1458" height="3240" alt="Source Code" src="https://github.com/user-attachments/assets/2614493d-da79-4a1d-9507-1bc63013e415" />

1 & 2. Mendefinisikan dictionary kontak sebagai tempat menyimpan data kontak.
3. (baris kosong)
4. Memulai perulangan program agar menu terus tampil sampai pengguna keluar.
5. Menampilkan judul program kontak.
6. Menampilkan menu “Lihat Kontak”.
7. Menampilkan menu “Cari Kontak”.
8. Menampilkan menu “Tambah Kontak”.
9. Menampilkan menu “Hapus Kontak”.
10. Menampilkan menu “Keluar”.
(baris kosong)
Menerima input pilihan menu dari pengguna.
(baris kosong)
Mengecek apakah pengguna memilih menu “1”.
Menampilkan teks daftar kontak.
(baris kosong)
Mengecek apakah dictionary kontak masih kosong.
Menampilkan pesan bahwa kontak kosong.
Jika kontak tidak kosong, program menjalankan blok else.
Melakukan perulangan untuk mengambil nama dan nomor dari dictionary kontak.
Menampilkan nama dan nomor kontak.
(baris kosong)
Mengecek apakah pengguna memilih menu “2”.
Meminta input nama kontak yang ingin dicari.
(baris kosong)
Membuat variabel found bernilai False sebagai penanda kontak belum ditemukan.
(baris kosong)
Melakukan perulangan untuk setiap nama di dictionary kontak.
Mengecek apakah nama yang dicari sama dengan nama kontak tanpa membedakan huruf besar kecil.
Menampilkan pesan bahwa kontak ditemukan.
Menampilkan nama kontak.
Menampilkan nomor kontak sesuai nama.
Mengubah nilai found menjadi True karena kontak ditemukan.
Menghentikan perulangan menggunakan break.
(baris kosong)
Mengecek apakah kontak tidak ditemukan setelah perulangan selesai.
Menampilkan pesan bahwa kontak tidak ditemukan.
(baris kosong)
Mengecek apakah pengguna memilih menu “3”.
Meminta input nama kontak baru.
Meminta input nomor kontak baru.
(baris kosong)
Menyimpan nama dan nomor baru ke dictionary kontak.
(baris kosong)
Menampilkan pesan bahwa kontak berhasil ditambahkan.
(baris kosong)
Mengecek apakah pengguna memilih menu “4”.
Meminta input nama kontak yang ingin dihapus.
(baris kosong)
Membuat variabel found bernilai False sebagai penanda kontak belum ditemukan.
(baris kosong)
Melakukan perulangan pada semua key dictionary kontak dalam bentuk list.
Mengecek apakah nama kontak sama dengan input hapus tanpa membedakan huruf besar kecil.
Menghapus kontak dari dictionary menggunakan del.
Menampilkan pesan bahwa kontak berhasil dihapus.
Mengubah nilai found menjadi True.
Menghentikan perulangan menggunakan break.
(baris kosong)
Mengecek apakah kontak yang ingin dihapus tidak ditemukan.
Menampilkan pesan bahwa kontak tidak ditemukan.
(baris kosong)
Mengecek apakah pengguna memilih menu “5”.
Menampilkan pesan bahwa program selesai.
Menghentikan perulangan utama menggunakan break.
(baris kosong)
Menjalankan blok else jika pilihan menu tidak sesuai.
Menampilkan pesan bahwa pilihan tidak valid.
