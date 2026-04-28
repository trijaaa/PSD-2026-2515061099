Tugas Akhir Percobaan 1

Judul Program: Sistem Playlist Lagu

Program ini berfungsi sebagai sistem manajemen playlist yang dirancang untuk memudahkan pengguna dalam menyimpan, mengatur, dan memutar daftar lagu secara terstruktur. Dengan menyediakan fitur utama seperti penambahan lagu, penghapusan lagu, penampilan daftar playlist, serta pemutaran lagu berdasarkan nomor urut, program ini membantu pengguna dalam mengelola koleksi lagu secara efisien. Algoritma dan struktur data yang diterapkan dalam program ini adalah Vector (list), yaitu struktur data dinamis yang memungkinkan penambahan dan penghapusan elemen secara fleksibel. Setiap elemen dalam list merepresentasikan satu judul lagu yang tersimpan secara berurutan. Implementasi ini menggunakan perulangan untuk mengakses dan menampilkan data, serta dilengkapi dengan mekanisme error handling (try-except) untuk menangani kesalahan input pengguna, seperti input non-angka atau index yang tidak valid, sehingga program tetap berjalan dengan stabil. Selain itu, penggunaan teknik string formatting digunakan untuk menyajikan output secara rapi dan mudah dipahami oleh pengguna.

Source Code:
<img width="1592" height="3020" alt="source code" src="https://github.com/user-attachments/assets/50eeadfb-0d97-4b21-bd9e-22d394d768f0" />

1. Mendefinisikan fungsi menu() untuk menampilkan daftar pilihan program.
2. Menampilkan judul menu playlist kepada pengguna.
3. Menampilkan opsi untuk menambah lagu ke dalam playlist.
4. Menampilkan opsi untuk menghapus lagu dari playlist.
5. Menampilkan opsi untuk melihat isi playlist.
6. Menampilkan opsi untuk memutar lagu berdasarkan nomor.
7. Menampilkan opsi untuk keluar dari program.
8. 
9. 
10. Mendefinisikan fungsi main() sebagai fungsi utama program.
11. Membuat vector (list) kosong bernama playlist untuk menyimpan lagu.
12. Mengatur variabel running bernilai True agar program berjalan dalam loop.
13. 
14. Membuat perulangan while agar program terus berjalan selama running bernilai True.
15. Memanggil fungsi menu() untuk menampilkan pilihan ke pengguna.
16. Menggunakan try untuk mengantisipasi error saat input pilihan.
17. Mengambil input pilihan dari pengguna dan mengubahnya menjadi tipe integer.
18. Menangkap error jika input bukan angka menggunakan except ValueError.
19. Menampilkan pesan kesalahan jika input tidak valid.
20. Menggunakan continue untuk mengulang loop ke awal.
21. 
22. Mengecek apakah pengguna memilih opsi tambah lagu (choice == 1).
23. Mengambil input judul lagu dan menghapus spasi berlebih dengan strip().
24. Mengecek apakah input lagu tidak kosong.
25. Menambahkan lagu ke dalam vector menggunakan append().
26. Menampilkan pesan bahwa lagu berhasil ditambahkan.
27. Jika input lagu kosong akan ditampilkan pesan error.
28. Menampilkan pesan error jika input lagu kosong.
29. 
30. Mengecek apakah pengguna memilih opsi hapus lagu (choice == 2).
31. Mengambil input judul lagu yang ingin dihapus.
32. Mengecek apakah lagu terdapat dalam playlist.
33. Menghapus lagu dari vector menggunakan remove().
34. Menampilkan pesan bahwa lagu berhasil dihapus.
35. Jika lagu tidak ditemukan dalam playlist.
36. Menampilkan pesan jika lagu tidak ditemukan.
37. 
38. Mengecek apakah pengguna memilih opsi tampilkan playlist (choice == 3).
39. Mengecek apakah playlist kosong dengan len().
40. Menampilkan pesan jika playlist kosong.
41. Jika playlist tidak kosong.
42. Menampilkan judul playlist jika tidak kosong.
43. Melakukan perulangan pada setiap lagu menggunakan enumerate().
44. Menampilkan nomor urut dan nama lagu.
45. 
46. Mengecek apakah pengguna memilih opsi putar lagu (choice == 4).
47. Menggunakan try untuk menangani kemungkinan error input.
48. Mengambil input nomor lagu dari pengguna.
49. Menampilkan lagu berdasarkan nomor yang dipilih.
50. Menangkap error jika input bukan angka atau index tidak valid.
51. Menampilkan pesan error jika index salah.
52. 
53. Mengecek apakah pengguna memilih keluar (choice == 5).
54. Mengubah nilai running menjadi False untuk menghentikan loop.
55. Menampilkan pesan bahwa program selesai.
56. 
57. Menangani kondisi jika pilihan tidak sesuai dengan menu.
58. Menampilkan pesan bahwa pilihan tidak valid.
59. 
60. 
61. Baris standar Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi langsung.
62. Memanggil fungsi main() untuk menjalankan program.

Output Program:
- Daftar Pilihan yang ada dalam Program
<img width="313" height="217" alt="image" src="https://github.com/user-attachments/assets/a1278b82-cba3-4992-8e32-841455affb27" />

- Pilihan 1 (Menambahkan lagu kedalam playlist)
<img width="580" height="93" alt="image" src="https://github.com/user-attachments/assets/55bc3712-3418-476d-83a4-335a2583f69f" />

- Pilihan 2 (Menghapus lagu dari playlist)
<img width="681" height="86" alt="image" src="https://github.com/user-attachments/assets/d9add18c-7de0-4829-bbab-0d1c09d01a5a" />

- Pilihan 3 (Menampilkan playlist)
<img width="452" height="143" alt="image" src="https://github.com/user-attachments/assets/be3ee806-98ab-4f49-a916-d05dbe6174e5" />

- Pilihan 4 (Putar lagu)
<img width="579" height="96" alt="image" src="https://github.com/user-attachments/assets/306aa518-f943-4f0d-80ff-189212702184" />

- Pilihan 5 (Keluar program)
<img width="222" height="59" alt="image" src="https://github.com/user-attachments/assets/2f7a2f05-aac7-40b8-a749-b13372df40e4" />

Link Youtube: 
