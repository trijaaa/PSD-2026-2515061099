**Tugas Akhir Percobaan 6 : Hashing (Separate Chaining)**
**Judul Proyek : Sistem Manajemen Menu Kopi**

Program ini dibuat untuk membantu pengguna dalam menyimpan dan mengelola data menu kopi secara sederhana menggunakan bahasa pemrograman Python. Dalam sebuah kedai kopi, data menu seperti ID kopi, nama kopi, dan harga perlu dikelola dengan baik agar proses pencarian, penambahan, maupun penghapusan data dapat dilakukan dengan cepat dan terorganisir. Oleh karena itu, dibuatlah sistem sederhana yang mampu menyimpan dan mengelola data menu kopi secara efisien.

Pada implementasinya, program ini memanfaatkan struktur data **Hash Map** dengan metode **Separate Chaining** untuk menyimpan data menu kopi. Struktur Hash Map digunakan karena mampu melakukan proses penyimpanan dan pencarian data dengan cepat melalui fungsi hash. Setiap data akan ditempatkan pada slot tertentu berdasarkan hasil perhitungan hash key. Apabila terjadi collision atau tabrakan data pada slot yang sama, program akan menyimpan data tersebut menggunakan struktur **Linked List** pada slot yang bersangkutan.

Program ini memiliki beberapa fitur utama seperti menambahkan menu kopi baru, mencari menu kopi berdasarkan ID, menghapus menu kopi, serta menampilkan seluruh data menu kopi yang tersimpan di dalam hash table. Selain itu, program juga dilengkapi dengan menu interaktif sehingga pengguna dapat menjalankan setiap fitur dengan lebih mudah dan terstruktur.

Dalam proses penyimpanan data, setiap menu kopi memiliki ID sebagai key dan informasi menu berupa nama kopi serta harga sebagai value. Ketika pengguna melakukan pencarian atau penghapusan data, program akan menggunakan fungsi hash untuk menemukan slot yang sesuai, kemudian melakukan pencarian pada linked list apabila terdapat lebih dari satu data pada slot tersebut.

Dengan adanya program ini, pengguna dapat lebih mudah dalam mengelola data menu kopi secara praktis dan terorganisir. Sistem ini juga membantu pengguna memahami penerapan struktur data **Hash Map dengan metode Separate Chaining** pada pemrograman Python, khususnya dalam menangani collision menggunakan linked list serta meningkatkan efisiensi penyimpanan dan pencarian data.

Source Code:

<img width="1672" height="6716" alt="Source Code" src="https://github.com/user-attachments/assets/86bb3194-d11a-4a94-9367-40ce900d3718" />

1. Mendefinisikan class Node sebagai node pada linked list.
2. Mendefinisikan constructor **init** pada class Node.
3. Menyimpan key ke atribut key.
4. Menyimpan value ke atribut value.
5. Mengatur pointer next menjadi None.
6. (baris kosong)
7. (baris kosong)
8. Mendefinisikan class HashMapSeparateChaining sebagai class utama hash map.
9. Mendefinisikan constructor **init** pada class HashMapSeparateChaining.
10. Menyimpan ukuran hash table ke variabel SIZE.
11. Membuat hash table berupa list berisi None sebanyak SIZE.
12. (baris kosong)
13. Mendefinisikan fungsi hash_function().
14. Menghitung indeks hash menggunakan operasi modulo.
15. (baris kosong)
16. Mendefinisikan fungsi insert() untuk menambah data.
17. Menentukan indeks penyimpanan berdasarkan hash key.
18. (baris kosong)
19. Mengambil node pertama pada slot yang dituju.
20. (baris kosong)
21. Melakukan traversal linked list selama node masih ada.
22. Mengecek apakah key sudah ada.
23. Mengubah value jika key sudah ada.
24. Mengakhiri fungsi insert().
25. Berpindah ke node berikutnya.
26. (baris kosong)
27. Membuat node baru.
28. Menghubungkan node baru ke node pertama pada slot tersebut.
29. Menjadikan node baru sebagai head linked list.
30. (baris kosong)
31. Mendefinisikan fungsi search() untuk mencari data.
32. Menentukan indeks berdasarkan hash key.
33. (baris kosong)
34. Mengambil node pertama pada slot yang dicari.
35. (baris kosong)
36. Melakukan traversal linked list.
37. Mengecek apakah key ditemukan.
38. Mengembalikan node jika key ditemukan.
39. Berpindah ke node berikutnya.
40. (baris kosong)
41. Mengembalikan None jika data tidak ditemukan.
42. (baris kosong)
43. Mendefinisikan fungsi remove_key() untuk menghapus data.
44. Menentukan indeks berdasarkan hash key.
45. (baris kosong)
46. Mengambil node pertama pada slot yang dituju.
47. Membuat variabel prev untuk menyimpan node sebelumnya.
48. (baris kosong)
49. Melakukan traversal linked list.
50. Mengecek apakah key ditemukan.
51. Mengecek apakah node yang dihapus berada di awal linked list.
52. Menggeser head ke node berikutnya.
53. Jika bukan node pertama maka masuk ke blok else.
54. Menghubungkan node sebelumnya ke node setelah node yang dihapus.
55. (baris kosong)
56. Mengembalikan True karena data berhasil dihapus.
57. (baris kosong)
58. Memindahkan prev ke node saat ini.
59. Berpindah ke node berikutnya.
60. (baris kosong)
61. Mengembalikan False jika data tidak ditemukan.
62. (baris kosong)
63. Mendefinisikan fungsi display() untuk menampilkan data.
64. Menampilkan judul daftar menu kopi.
65. (baris kosong)
66. Melakukan perulangan untuk seluruh slot hash table.
67. Mengecek apakah slot berisi data.
68. Menampilkan nomor slot.
69. (baris kosong)
70. Mengambil node pertama pada slot tersebut.
71. (baris kosong)
72. Melakukan traversal linked list pada slot tersebut.
73. Menampilkan data menu kopi.
74. Melanjutkan string output ID kopi.
75. Melanjutkan string output nama kopi.
76. Melanjutkan string output harga kopi.
77. Mengganti tanda koma menjadi titik pada output harga.
78. Menentukan agar output tetap pada baris yang sama.
79. Menutup fungsi print().
80. Berpindah ke node berikutnya.
81. (baris kosong)
82. Mencetak baris baru setelah seluruh node pada slot ditampilkan.
83. (baris kosong)
84. (baris kosong)
85. Mendefinisikan fungsi main().
86. Membuat objek HashMapSeparateChaining.
87. (baris kosong)
88. Membuat perulangan utama program.
89. Menampilkan judul menu program.
90. Menampilkan pilihan tambah menu kopi.
91. Menampilkan pilihan cari menu kopi.
92. Menampilkan pilihan hapus menu kopi.
93. Menampilkan pilihan tampilkan semua menu.
94. Menampilkan pilihan keluar.
95. (baris kosong)
96. Meminta input pilihan menu dari pengguna.
97. (baris kosong)
98. Mengecek apakah pengguna memilih menu 1.
99. Meminta input ID kopi.
100. Meminta input nama kopi.
101. Meminta input harga kopi.
102. (baris kosong)
103. Membuat dictionary data_kopi.
104. Menyimpan nama kopi ke dictionary.
105. Menyimpan harga kopi ke dictionary.
106. Menutup dictionary.
107. (baris kosong)
108. Memasukkan data ke hash map.
109. (baris kosong)
110. Menampilkan pesan berhasil tambah data.
111. (baris kosong)
112. Mengecek apakah pengguna memilih menu 2.
113. Meminta ID kopi yang akan dicari.
114. (baris kosong)
115. Mencari data berdasarkan ID kopi.
116. (baris kosong)
117. Mengecek apakah data ditemukan.
118. Menampilkan judul hasil pencarian.
119. Menampilkan ID kopi.
120. Menampilkan nama kopi.
121. Menampilkan output harga kopi.
122. Memformat harga dengan pemisah ribuan.
123. Menutup fungsi print().
124. Jika data tidak ditemukan masuk ke blok else.
125. Menampilkan pesan data tidak ditemukan.
126. (baris kosong)
127. Mengecek apakah pengguna memilih menu 3.
128. Meminta ID kopi yang akan dihapus.
129. (baris kosong)
130. Memanggil fungsi remove_key().
131. Menampilkan pesan berhasil dihapus.
132. Jika data tidak ditemukan masuk ke blok else.
133. Menampilkan pesan data tidak ditemukan.
134. (baris kosong)
135. Mengecek apakah pengguna memilih menu 4.
136. Menampilkan seluruh data pada hash map.
137. (baris kosong)
138. Mengecek apakah pengguna memilih menu 5.
139. Menampilkan pesan penutup program.
140. Menghentikan perulangan menggunakan break.
141. (baris kosong)
142. Menangani pilihan menu yang tidak valid.
143. Menampilkan pesan pilihan tidak valid.
144. (baris kosong)
145. (baris kosong)
146. Mengecek apakah file dijalankan sebagai program utama.
147. Memanggil fungsi main().

Output:

Menambahkan menu kopi:

<img width="555" height="637" alt="image" src="https://github.com/user-attachments/assets/4409b4b4-7752-4968-8c6f-ee633789fdc4" />
<img width="501" height="320" alt="image" src="https://github.com/user-attachments/assets/346b9859-5243-4da2-9808-f699c45069c7" />

======

Menampilkan seluruh menu kopi:

<img width="511" height="341" alt="image" src="https://github.com/user-attachments/assets/5afd22c6-9bda-4c51-ba68-847fffab0d6f" />

======

Mencari menu kopi berdasarkan ID nya:

<img width="513" height="369" alt="image" src="https://github.com/user-attachments/assets/9a2d043e-e466-4247-b0a6-2a0eb854b6ca" />

======

Menghapus menu kopi menggunakan ID:

<img width="536" height="269" alt="image" src="https://github.com/user-attachments/assets/287d5285-dc0f-4cd5-a461-7c19d47869ec" />
<img width="516" height="317" alt="image" src="https://github.com/user-attachments/assets/65e507a0-0641-46c1-9d56-23f3a35868b7" />

======

Link YT: https://www.youtube.com/watch?v=34vjHpaxGhw
