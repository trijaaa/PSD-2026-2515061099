Tugas Akhir Percobaan 4 : Stack Linked List

Judul Proyek : Sistem Riwayat Aktivitas

Program ini dibuat untuk membantu pengguna dalam menyimpan dan mengelola riwayat aktivitas secara sederhana menggunakan bahasa pemrograman Python. Dalam kehidupan sehari-hari, seseorang sering melakukan berbagai aktivitas seperti membuka aplikasi, mengedit file, atau menjalankan tugas tertentu yang terkadang perlu dilihat kembali riwayatnya. Oleh karena itu, dibuatlah sistem sederhana yang mampu mencatat, menampilkan, serta menghapus aktivitas terakhir secara otomatis dan terstruktur.

Pada implementasinya, program ini memanfaatkan struktur data Stack yang dikombinasikan dengan Linked List untuk menyimpan data aktivitas. Struktur Stack digunakan karena menerapkan konsep LIFO (Last In First Out), yaitu data yang terakhir dimasukkan akan menjadi data pertama yang diambil atau dihapus. Sementara itu, Linked List digunakan untuk menghubungkan setiap data aktivitas melalui node yang saling terhubung secara dinamis.

Program ini memiliki beberapa fitur utama seperti menambahkan aktivitas baru (push), menghapus aktivitas terakhir (pop), melihat aktivitas terakhir (peek), menampilkan seluruh riwayat aktivitas, serta menghitung jumlah aktivitas yang tersimpan. Selain itu, program juga dilengkapi dengan menu interaktif dan validasi input agar pengguna dapat menjalankan program dengan lebih mudah dan meminimalisir kesalahan saat memasukkan pilihan menu.

Dengan adanya program ini, pengguna dapat lebih mudah dalam mengelola riwayat aktivitas secara praktis dan terorganisir. Sistem ini diharapkan dapat membantu pengguna dalam memahami penerapan struktur data Stack dan Linked List pada pemrograman Python, sekaligus memberikan pengalaman penggunaan program yang sederhana namun fungsional.

Source Code:

<img width="1472" height="4868" alt="Source Code" src="https://github.com/user-attachments/assets/4d3f46f5-dac0-4542-8827-ae1cb2498248" />

1 : Mendefinisikan class Node sebagai node untuk Linked List.
2 : Mendefinisikan constructor __init__ pada class Node.
3 : Menyimpan data aktivitas ke dalam variabel data.
4 : Mengatur pointer next menjadi None.
5 : (baris kosong)
6 : (baris kosong)
7 : Mendefinisikan class StackLinkedList.
8 : Mendefinisikan constructor __init__ pada class StackLinkedList.
9 : Mengatur pointer top_ptr sebagai penunjuk stack teratas dan bernilai None.
10 : (baris kosong)
11 : Mendefinisikan fungsi is_empty() untuk mengecek apakah stack kosong.
12 : Mengembalikan nilai True jika stack kosong.
13 : (baris kosong)
14 : Mendefinisikan fungsi push() untuk menambahkan aktivitas baru.
15 : Membuat node baru berdasarkan input pengguna.
16 : Menghubungkan node baru ke node sebelumnya.
17 : Memindahkan top_ptr ke node baru.
18 : Menampilkan pesan bahwa aktivitas berhasil ditambahkan.
19 : (baris kosong)
20 : Mendefinisikan fungsi pop() untuk menghapus aktivitas terakhir.
21 : Mengecek apakah stack kosong.
22 : Menampilkan pesan bahwa riwayat aktivitas kosong.
23 : Menghentikan fungsi menggunakan return.
24 : (baris kosong)
25 : Menyimpan node teratas ke variabel sementara temp.
26 : Menampilkan aktivitas terakhir yang berhasil dihapus.
27 : Memindahkan top_ptr ke node berikutnya.
28 : (baris kosong)
29 : Mendefinisikan fungsi peek() untuk melihat aktivitas terakhir.
30 : Mengecek apakah stack kosong.
31 : Menampilkan pesan bahwa riwayat aktivitas kosong.
32 : Menghentikan fungsi menggunakan return.
33 : (baris kosong)
34 : Menampilkan aktivitas terakhir pada stack.
35 : (baris kosong)
36 : Mendefinisikan fungsi display() untuk menampilkan semua aktivitas.
37 : Mengecek apakah stack kosong.
38 : Menampilkan pesan bahwa riwayat aktivitas kosong.
39 : Menghentikan fungsi menggunakan return.
40 : (baris kosong)
41 : Menampilkan judul riwayat aktivitas.
42 : Menyimpan node teratas ke variabel current.
43 : Membuat variabel nomor dengan nilai awal 1.
44 : (baris kosong)
45 : Memulai perulangan selama node masih ada.
46 : Menampilkan nomor dan data aktivitas.
47 : Memindahkan current ke node berikutnya.
48 : Menambahkan nomor urut aktivitas.
49 : (baris kosong)
50 : Mendefinisikan fungsi hitung_aktivitas() untuk menghitung total aktivitas.
51 : Membuat variabel count dengan nilai awal 0.
52 : Menyimpan node teratas ke variabel current.
53 : (baris kosong)
54 : Memulai perulangan selama node masih ada.
55 : Menambahkan jumlah aktivitas sebanyak 1.
56 : Memindahkan current ke node berikutnya.
57 : (baris kosong)
58 : Menampilkan total aktivitas yang tersimpan.
59 : (baris kosong)
60 : (baris kosong)
61 : Mendefinisikan fungsi utama main().
62 : Membuat objek stack dari class StackLinkedList.
63 : Membuat variabel pilih dengan nilai awal 0.
64 : (baris kosong)
65 : Memulai perulangan program selama pengguna belum memilih keluar.
66 : Menampilkan judul program stack linked list.
67 : Menampilkan menu “Tambah Aktivitas”.
68 : Menampilkan menu “Hapus Aktivitas Terakhir”.
69 : Menampilkan menu “Lihat Aktivitas Terakhir”.
70 : Menampilkan menu “Tampilkan Semua Aktivitas”.
71 : Menampilkan menu “Hitung Total Aktivitas”.
72 : Menampilkan menu “Keluar”.
73 : (baris kosong)
74 : Memulai blok try untuk validasi input.
75 : Menerima input pilihan menu dari pengguna.
76 : Menangkap error jika input bukan angka.
77 : Menampilkan pesan input tidak valid.
78 : Mengulangi menu menggunakan continue.
79 : (baris kosong)
80 : Mengecek apakah pengguna memilih menu “1”.
81 : Menerima input aktivitas dari pengguna.
82 : Menambahkan aktivitas ke stack menggunakan fungsi push().
83 : (baris kosong)
84 : Mengecek apakah pengguna memilih menu “2”.
85 : Menghapus aktivitas terakhir menggunakan fungsi pop().
86 : (baris kosong)
87 : Mengecek apakah pengguna memilih menu “3”.
88 : Menampilkan aktivitas terakhir menggunakan fungsi peek().
89 : (baris kosong)
90 : Mengecek apakah pengguna memilih menu “4”.
91 : Menampilkan seluruh aktivitas menggunakan fungsi display().
92 : (baris kosong)
93 : Mengecek apakah pengguna memilih menu “5”.
94 : Menghitung total aktivitas menggunakan fungsi hitung_aktivitas().
95 : (baris kosong)
96 : Mengecek apakah pengguna memilih menu “6”.
97 : Menampilkan pesan program selesai.
98 : (baris kosong)
99 : Mengecek jika pilihan menu tidak tersedia.
100 : Menampilkan pesan pilihan tidak valid.
101 : (baris kosong)
102 : (baris kosong)
103 : Mengecek apakah file dijalankan sebagai program utama.
104 : Menjalankan fungsi main().
