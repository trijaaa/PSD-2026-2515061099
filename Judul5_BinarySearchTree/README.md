Tugas Akhir Percobaan 5 : Binary Search Tree (BST)
Judul Proyek : Sistem Ranking Kelas

Program ini dibuat untuk membantu pengguna dalam menyimpan dan mengelola data ranking kelas secara sederhana menggunakan bahasa pemrograman Python. Dalam lingkungan sekolah, data nilai siswa sering digunakan untuk menentukan urutan ranking berdasarkan nilai tertinggi hingga terendah. Oleh karena itu, dibuatlah sistem sederhana yang mampu menyimpan, mencari, menampilkan, dan menghapus data nilai siswa secara terstruktur dan efisien.

Pada implementasinya, program ini memanfaatkan struktur data Binary Search Tree (BST) untuk menyimpan data nilai siswa. Struktur BST digunakan karena memiliki kemampuan dalam melakukan proses pencarian, penyisipan, dan penghapusan data dengan lebih cepat dibandingkan penyimpanan data biasa. Pada BST, setiap node memiliki maksimal dua anak, yaitu left child dan right child. Nilai yang lebih kecil akan ditempatkan di sebelah kiri node, sedangkan nilai yang lebih besar ditempatkan di sebelah kanan node sehingga data dapat tersusun secara otomatis.

Program ini memiliki beberapa fitur utama seperti menambahkan nilai siswa ke dalam ranking, menghapus nilai tertentu, mencari nilai siswa, menampilkan seluruh ranking kelas secara terurut, serta menghitung tinggi pohon BST. Selain itu, program juga dilengkapi dengan menu interaktif dan validasi input agar pengguna dapat menjalankan program dengan lebih mudah dan meminimalisir kesalahan saat memasukkan pilihan menu.

Dalam proses penampilan ranking, program menggunakan metode traversal reverse inorder sehingga data nilai dapat ditampilkan mulai dari nilai terbesar hingga terkecil. Dengan cara tersebut, pengguna dapat melihat urutan ranking kelas secara otomatis tanpa perlu melakukan proses sorting tambahan.

Dengan adanya program ini, pengguna dapat lebih mudah dalam mengelola data ranking kelas secara praktis dan terorganisir. Sistem ini diharapkan dapat membantu pengguna dalam memahami penerapan struktur data Binary Search Tree (BST) pada pemrograman Python, sekaligus memberikan pengalaman penggunaan program yang sederhana namun fungsional.

Source Code:

<img width="1420" height="8168" alt="Source code" src="https://github.com/user-attachments/assets/a614a9bd-0586-43e5-bacf-c428f47de63a" />

1. Mendefinisikan class `Node` sebagai node BST.
2. Mendefinisikan constructor `__init__` pada class `Node`.
3. Menyimpan data nilai ke variabel `nilai`.
4. Mengatur child kiri (`left`) menjadi `None`.
5. Mengatur child kanan (`right`) menjadi `None`.
6. (baris kosong)
7. (baris kosong)
8. Mendefinisikan class `BSTRanking` sebagai class utama BST.
9. Mendefinisikan constructor `__init__` pada class `BSTRanking`.
10. Mengatur `root` BST menjadi `None`.
11. (baris kosong)
12. Mendefinisikan fungsi `insert_node()` untuk menambahkan node baru.
13. Mengecek apakah root kosong.
14. Mengembalikan node baru jika root kosong.
15. Mengecek apakah nilai lebih kecil dari root.
16. Menambahkan node ke subtree kiri secara rekursif.
17. Mengecek apakah nilai lebih besar dari root.
18. Menambahkan node ke subtree kanan secara rekursif.
19. Mengembalikan root BST setelah proses insert selesai.
20. (baris kosong)
21. Mendefinisikan fungsi `insert()` untuk insert data baru.
22. Mengecek apakah nilai sudah ada di BST.
23. Mengembalikan `False` jika data sudah ada.
24. Menambahkan node baru ke BST.
25. Mengembalikan `True` jika insert berhasil.
26. (baris kosong)
27. Mendefinisikan fungsi `search()` untuk mencari data BST.
28. Mengecek apakah root kosong.
29. Mengembalikan `False` jika data tidak ditemukan.
30. Mengecek apakah nilai sama dengan root.
31. Mengembalikan `True` jika data ditemukan.
32. Mengecek apakah nilai lebih kecil dari root.
33. Menjalankan pencarian pada subtree kiri.
34. Menjalankan kondisi selain `elif`.
35. Menjalankan pencarian pada subtree kanan.
36. (baris kosong)
37. Mendefinisikan fungsi `find_min()` untuk mencari nilai minimum.
38. Menyimpan root ke variabel `current`.
39. Melakukan perulangan selama child kiri masih ada.
40. Memindahkan pointer ke node kiri.
41. Mengembalikan node dengan nilai terkecil.
42. (baris kosong)
43. Mendefinisikan fungsi `delete_node()` untuk menghapus node BST.
44. Mengecek apakah root kosong.
45. Mengembalikan `None` jika BST kosong.
46. Mengecek apakah nilai lebih kecil dari root.
47. Menjalankan delete pada subtree kiri.
48. Mengecek apakah nilai lebih besar dari root.
49. Menjalankan delete pada subtree kanan.
50. Menjalankan kondisi jika node ditemukan.
51. Mengecek apakah node tidak memiliki child kiri dan kanan.
52. Menghapus node dengan mengembalikan `None`.
53. Mengecek apakah child kiri kosong.
54. Mengembalikan child kanan.
55. Mengecek apakah child kanan kosong.
56. Mengembalikan child kiri.
57. Menjalankan kondisi jika node memiliki dua child.
58. Mencari successor menggunakan fungsi `find_min()`.
59. Mengganti nilai root dengan nilai successor.
60. Menjalankan delete pada successor.
61. Mengirim subtree kanan BST.
62. Mengirim nilai successor sebagai target delete.
63. Menutup pemanggilan fungsi `delete_node()`.
64. Mengembalikan root BST.
65. (baris kosong)
66. Mendefinisikan fungsi `delete()` untuk menghapus data BST.
67. Mengecek apakah nilai ada di BST.
68. Mengembalikan `False` jika nilai tidak ditemukan.
69. Menjalankan delete node pada BST.
70. Mengembalikan `True` jika delete berhasil.
71. (baris kosong)
72. Mendefinisikan fungsi `tampilkan_ranking()` untuk menampilkan ranking.
73. Mengecek apakah root tidak kosong.
74. Menampilkan subtree kanan terlebih dahulu.
75. Menampilkan nilai node saat ini.
76. Menampilkan subtree kiri.
77. (baris kosong)
78. Mendefinisikan fungsi `height()` untuk menghitung tinggi BST.
79. Mengecek apakah root kosong.
80. Mengembalikan `-1` jika BST kosong.
81. Menghitung tinggi subtree kiri.
82. Menghitung tinggi subtree kanan.
83. Mengembalikan tinggi terbesar BST.
84. (baris kosong)
85. Mendefinisikan fungsi `is_empty()` untuk mengecek BST kosong.
86. Mengembalikan `True` jika root bernilai `None`.
87. (baris kosong)
88. (baris kosong)
89. Mendefinisikan fungsi `main()` sebagai program utama.
90. Membuat objek BST baru bernama `bst`.
91. Membuat variabel `pilih` untuk menyimpan pilihan menu.
92. Membuat perulangan menu selama pilihan tidak sama dengan 6.
93. (baris kosong)
94. Menampilkan garis menu program.
95. Menampilkan judul program ranking kelas.
96. Menampilkan garis menu program.
97. Menampilkan menu tambah nilai.
98. Menampilkan menu hapus nilai.
99. Menampilkan menu tampil ranking.
100. Menampilkan menu cari nilai.
101. Menampilkan menu tinggi BST.
102. Menampilkan menu keluar.
103. (baris kosong)
104. Menjalankan blok `try`.
105. Meminta input pilihan menu dari user.
106. Menjalankan blok `except` jika input salah.
107. Menampilkan pesan error input.
108. Melanjutkan perulangan program.
109. (baris kosong)
110. Mengecek apakah user memilih menu 1.
111. Menjalankan blok `try`.
112. Meminta input nilai siswa.
113. Menyimpan hasil insert ke variabel `berhasil`.
114. Mengecek apakah insert berhasil dilakukan.
115. Menampilkan pesan bahwa nilai berhasil ditambahkan.
116. Menjalankan kondisi selain `if`.
117. Menampilkan pesan bahwa nilai sudah ada.
118. Menjalankan blok `except` jika input salah.
119. Menampilkan pesan error input.
120. (baris kosong)
121. Mengecek apakah user memilih menu 2.
122. Menjalankan blok `try`.
123. Mengecek apakah BST kosong.
124. Menampilkan pesan bahwa BST kosong.
125. Menjalankan kondisi selain `if`.
126. Memulai input multiline nilai delete.
127. Menampilkan input nilai yang ingin dihapus.
128. Menutup input multiline.
129. Menyimpan hasil delete ke variabel `berhasil`.
130. Mengecek apakah delete berhasil dilakukan.
131. Menampilkan pesan bahwa nilai berhasil dihapus.
132. Menjalankan kondisi selain `if`.
133. Menampilkan pesan bahwa nilai tidak ditemukan.
134. Menjalankan blok `except` jika input salah.
135. Menampilkan pesan error input.
136. (baris kosong)
137. Mengecek apakah user memilih menu 3.
138. Mengecek apakah BST kosong.
139. Menampilkan pesan bahwa ranking kosong.
140. Menjalankan kondisi selain `if`.
141. Menampilkan judul ranking kelas.
142. Menampilkan ranking BST menggunakan traversal.
143. (baris kosong)
144. Mengecek apakah user memilih menu 4.
145. Menjalankan blok `try`.
146. Mengecek apakah BST kosong.
147. Menampilkan pesan bahwa BST kosong.
148. Menjalankan kondisi selain `if`.
149. Meminta input nilai yang ingin dicari.
150. Menjalankan fungsi `search()`.
151. Mengirim root BST sebagai parameter.
152. Mengirim nilai target pencarian.
153. Menutup pemanggilan fungsi `search()`.
154. Mengecek apakah data ditemukan.
155. Menampilkan pesan bahwa nilai ditemukan.
156. Menampilkan teks lanjutan print multiline.
157. Menutup fungsi `print()`.
158. Menjalankan kondisi selain `if`.
159. Menampilkan pesan bahwa nilai tidak ditemukan.
160. Menjalankan blok `except` jika input salah.
161. Menampilkan pesan error input.
162. (baris kosong)
163. Mengecek apakah user memilih menu 5.
164. Mengecek apakah BST kosong.
165. Menampilkan pesan bahwa BST kosong.
166. Menjalankan kondisi selain `if`.
167. Menampilkan teks tinggi BST.
168. Menampilkan hasil fungsi `height()`.
169. Menutup fungsi `print()`.
170. (baris kosong)
171. Mengecek apakah user memilih menu 6.
172. Menampilkan pesan program selesai.
173. Menjalankan kondisi selain semua pilihan menu.
174. Menampilkan pesan pilihan tidak valid.
175. (baris kosong)
176. Mengecek apakah file dijalankan langsung.
177. Menjalankan fungsi `main()`.
178. (akhir program)
179. (file selesai dieksekusi)

Output:

Menampilkan menu:

<img width="434" height="296" alt="image" src="https://github.com/user-attachments/assets/c1aac8c3-2dc3-458a-ae81-eddf87d54e7d" />

Pilihan 1, menambahkan nilai:

<img width="479" height="708" alt="image" src="https://github.com/user-attachments/assets/dffc840d-37da-4ba2-b726-d137940dc03b" />
<img width="462" height="703" alt="image" src="https://github.com/user-attachments/assets/37018548-e7d4-4fb3-85d8-b3fa5638a4bd" />
