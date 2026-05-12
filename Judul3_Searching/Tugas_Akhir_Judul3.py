kontak = {
}

while True:
    print("\n=== PROGRAM KONTAK ===")
    print("1. Lihat Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\nDaftar Kontak:")
        
        if len(kontak) == 0:
            print("Kontak kosong.")
        else:
            for nama, nomor in kontak.items():
                print(f"{nama} : {nomor}")

    elif pilihan == "2":
        cari = input("\nMasukkan nama kontak: ")

        found = False

        for nama in kontak:
            if nama.lower() == cari.lower():
                print("\nKontak ditemukan!")
                print("Nama  :", nama)
                print("Nomor :", kontak[nama])
                found = True
                break

        if not found:
            print("\nKontak tidak ditemukan.")

    elif pilihan == "3":
        nama_baru = input("\nMasukkan nama kontak baru: ")
        nomor_baru = input("Masukkan nomor kontak: ")

        kontak[nama_baru] = nomor_baru

        print("Kontak berhasil ditambahkan!")

    elif pilihan == "4":
        hapus = input("\nMasukkan nama kontak yang ingin dihapus: ")

        found = False

        for nama in list(kontak.keys()):
            if nama.lower() == hapus.lower():
                del kontak[nama]
                print("Kontak berhasil dihapus!")
                found = True
                break

        if not found:
            print("Kontak tidak ditemukan.")

    elif pilihan == "5":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak valid.")