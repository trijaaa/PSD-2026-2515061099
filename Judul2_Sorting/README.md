Tugas Akhir Percobaan 2 : Sorting

Judul Proyek : Sistem Pengurutan Prioritas Tugas Berdasarkan Deadline

Program ini dibuat untuk mengelola dan mengurutkan daftar tugas berdasarkan waktu deadline yang dimiliki. Dalam kehidupan sehari-hari, khususnya bagi pelajar atau mahasiswa, sering kali terdapat banyak tugas dengan batas waktu yang berbeda-beda. Oleh karena itu, diperlukan suatu sistem sederhana yang mampu membantu menyusun prioritas tugas secara otomatis agar pengguna dapat mengetahui tugas mana yang harus dikerjakan terlebih dahulu.

Pada implementasinya, program ini memanfaatkan struktur data berupa array (list) untuk menyimpan data tugas yang terdiri dari nama tugas dan deadline. Selanjutnya, digunakan algoritma Insertion Sort untuk mengurutkan data berdasarkan deadline secara ascending (dari yang paling dekat ke yang paling lama). Program juga dilengkapi dengan validasi input untuk memastikan data yang dimasukkan sesuai dengan yang diharapkan, sehingga dapat meminimalisir kesalahan selama proses berlangsung.

Dengan adanya program ini, pengguna dapat dengan mudah memasukkan daftar tugas, mengurutkannya berdasarkan tingkat prioritas, serta memperoleh hasil yang terstruktur dan mudah dipahami. Sistem ini diharapkan dapat membantu meningkatkan manajemen waktu dan efisiensi dalam menyelesaikan tugas.

Source Code:
<img width="1324" height="2184" alt="source code" src="https://github.com/user-attachments/assets/4b4627f6-c202-42f3-8508-9269b053ad05" />

1. Mendefinisikan fungsi insertion_sort dengan parameter arr dan n.
2. Melakukan perulangan dari indeks ke-1 sampai n-1.
3. Menyimpan elemen ke-i ke dalam variabel sementara temp.
4. Menentukan indeks sebelumnya dengan j = i - 1.
5. (baris kosong)
6. Melakukan perulangan selama j >= 0 dan deadline sebelumnya lebih besar dari deadline temp.
7. Menggeser elemen arr[j] ke posisi kanan (arr[j + 1]).
8. Mengurangi nilai j untuk lanjut membandingkan ke kiri.
9. (baris kosong)
10. Menempatkan temp ke posisi yang sesuai setelah pergeseran.
11. (baris kosong)
12. (baris kosong)
13. Mendefinisikan fungsi main sebagai fungsi utama.
14. Memulai blok try untuk menangani error input.
15. Mengambil input jumlah tugas dari user dan mengubahnya ke integer.
16. Menangkap error jika input bukan angka (ValueError).
17. Menampilkan pesan "Input tidak valid!".
18. Menghentikan fungsi dengan return.
19. (baris kosong)
20. Membuat list kosong arr untuk menyimpan data tugas.
21. Menampilkan pesan "Masukkan data tugas:".
22. (baris kosong)
23. Melakukan perulangan sebanyak jumlah tugas (n).
24. Mengambil input nama tugas ke-(i+1).
25. Memulai perulangan tak hingga (while True) untuk validasi input.
26. Memulai blok try untuk input deadline.
27. Mengambil input deadline dan mengubahnya ke integer.
28. Menambahkan tuple (nama, deadline) ke dalam list arr.
29. Menghentikan loop jika input valid.
30. Menangkap error jika input bukan angka.
31. Menampilkan pesan "Masukkan angka yang valid!".
32. (baris kosong)
33. Menampilkan data sebelum diurutkan.
34. (baris kosong)
35. Memanggil fungsi insertion_sort(arr, n) untuk mengurutkan data.
36. (baris kosong)
37. Menampilkan judul "=== PRIORITAS TUGAS ===".
38. Melakukan perulangan untuk menampilkan hasil.
39. Menampilkan nomor urutan, nama tugas, dan deadline.
40. (baris kosong)
41. (baris kosong)
42. Mengecek apakah file dijalankan sebagai program utama (__name__ == "__main__").
43. Memanggil fungsi main() jika kondisi terpenuhi.

Output:
Menampilkan proses input data tugas dari pengguna serta kondisi data sebelum dilakukan pengurutan.
<img width="1363" height="280" alt="image" src="https://github.com/user-attachments/assets/a7093e96-3295-459a-a4bd-7615fb777c29" />
Menampilkan hasil pengurutan tugas berdasarkan deadline dari yang paling mendesak menggunakan algoritma Insertion Sort.
<img width="527" height="121" alt="image" src="https://github.com/user-attachments/assets/c1673eb2-ba9d-4393-b99b-9a326ee7cff2" />
Link Youtube: https://www.youtube.com/watch?v=D2e77YmIygg
