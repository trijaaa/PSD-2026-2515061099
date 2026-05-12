Tugas Akhir Percobaan 3 : Searching

Judul Proyek : Sistem Pencari Kontak

Program ini dibuat untuk membantu pengguna dalam mengelola data kontak secara sederhana menggunakan bahasa pemrograman Python. Dalam kehidupan sehari-hari, sering kali seseorang membutuhkan tempat untuk menyimpan nomor telepon atau informasi kontak agar lebih mudah dicari dan diakses kembali. Oleh karena itu, dibuatlah sistem sederhana yang mampu melakukan penyimpanan, pencarian, penambahan, serta penghapusan kontak secara otomatis dan terstruktur.

Pada implementasinya, program ini memanfaatkan struktur data berupa dictionary untuk menyimpan data kontak yang terdiri dari nama dan nomor telepon. Program juga menggunakan metode searching untuk mencari data kontak berdasarkan nama yang dimasukkan pengguna. Proses pencarian dilakukan dengan perulangan dan perbandingan teks secara fleksibel menggunakan fungsi lower(), sehingga pencarian tetap dapat dilakukan meskipun terdapat perbedaan huruf besar dan kecil.

Selain fitur pencarian, program juga dilengkapi dengan menu interaktif yang memungkinkan pengguna melihat seluruh daftar kontak, menambahkan kontak baru, serta menghapus kontak yang sudah tidak diperlukan. Program turut menggunakan validasi pilihan menu agar input yang dimasukkan sesuai dengan opsi yang tersedia, sehingga dapat meminimalisir kesalahan saat program dijalankan.

Dengan adanya program ini, pengguna dapat lebih mudah dalam mengelola daftar kontak secara praktis dan terorganisir. Sistem ini diharapkan dapat membantu meningkatkan efisiensi pengguna dalam menyimpan serta mencari informasi kontak dengan lebih cepat dan sederhana.

Source Code:

<img width="1458" height="3240" alt="Source Code" src="https://github.com/user-attachments/assets/2614493d-da79-4a1d-9507-1bc63013e415" />

1 & 2. Mendefinisikan dictionary `kontak` sebagai tempat menyimpan data kontak.
3. (baris kosong)
4. Memulai perulangan program agar menu terus tampil sampai pengguna keluar.
5. Menampilkan judul program kontak.
6. Menampilkan menu “Lihat Kontak”.
7. Menampilkan menu “Cari Kontak”.
8. Menampilkan menu “Tambah Kontak”.
9. Menampilkan menu “Hapus Kontak”.
0. Menampilkan menu “Keluar”.
10. (baris kosong)
11. Menerima input pilihan menu dari pengguna.
12. (baris kosong)
13. Mengecek apakah pengguna memilih menu “1”.
14. Menampilkan teks daftar kontak.
15. (baris kosong)
16. Mengecek apakah dictionary kontak masih kosong.
17. Menampilkan pesan bahwa kontak kosong.
18. Jika kontak tidak kosong, program menjalankan blok else.
19. Melakukan perulangan untuk mengambil nama dan nomor dari dictionary kontak.
20. Menampilkan nama dan nomor kontak.
21. (baris kosong)
22. Mengecek apakah pengguna memilih menu “2”.
23. Meminta input nama kontak yang ingin dicari.
24. (baris kosong)
25. Membuat variabel `found` bernilai False sebagai penanda kontak belum ditemukan.
26. (baris kosong)
27. Melakukan perulangan untuk setiap nama di dictionary kontak.
28. Mengecek apakah nama yang dicari sama dengan nama kontak tanpa membedakan huruf besar kecil.
29. Menampilkan pesan bahwa kontak ditemukan.
30. Menampilkan nama kontak.
31. Menampilkan nomor kontak sesuai nama.
32. Mengubah nilai `found` menjadi True karena kontak ditemukan.
33. Menghentikan perulangan menggunakan `break`.
34. (baris kosong)
35. Mengecek apakah kontak tidak ditemukan setelah perulangan selesai.
36. Menampilkan pesan bahwa kontak tidak ditemukan.
37. (baris kosong)
38. Mengecek apakah pengguna memilih menu “3”.
39. Meminta input nama kontak baru.
40. Meminta input nomor kontak baru.
41. (baris kosong)
42. Menyimpan nama dan nomor baru ke dictionary kontak.
43. (baris kosong)
44. Menampilkan pesan bahwa kontak berhasil ditambahkan.
45. (baris kosong)
46. Mengecek apakah pengguna memilih menu “4”.
47. Meminta input nama kontak yang ingin dihapus.
48. (baris kosong)
49. Membuat variabel `found` bernilai False sebagai penanda kontak belum ditemukan.
50. (baris kosong)
51. Melakukan perulangan pada semua key dictionary kontak dalam bentuk list.
52. Mengecek apakah nama kontak sama dengan input hapus tanpa membedakan huruf besar kecil.
53. Menghapus kontak dari dictionary menggunakan `del`.
54. Menampilkan pesan bahwa kontak berhasil dihapus.
55. Mengubah nilai `found` menjadi True.
56. Menghentikan perulangan menggunakan `break`.
57. (baris kosong)
58. Mengecek apakah kontak yang ingin dihapus tidak ditemukan.
59. Menampilkan pesan bahwa kontak tidak ditemukan.
60. (baris kosong)
61. Mengecek apakah pengguna memilih menu “5”.
62. Menampilkan pesan bahwa program selesai.
63. Menghentikan perulangan utama menggunakan `break`.
64. (baris kosong)
65. Menjalankan blok `else` jika pilihan menu tidak sesuai.
66. Menampilkan pesan bahwa pilihan tidak valid.
