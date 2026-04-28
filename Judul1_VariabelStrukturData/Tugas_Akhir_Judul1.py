def menu():
    print("\n=== MENU PLAYLIST ===")
    print("1. Tambah Lagu")
    print("2. Hapus Lagu")
    print("3. Tampilkan Playlist")
    print("4. Putar Lagu")
    print("5. Keluar")


def main():
    playlist = []
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            lagu = input("Masukkan judul lagu: ").strip()
            if lagu:
                playlist.append(lagu)
                print(f'Lagu "{lagu}" ditambahkan ke playlist.')
            else:
                print("Judul lagu tidak boleh kosong!")

        elif choice == 2:
            lagu = input("Masukkan judul lagu yang ingin dihapus: ").strip()
            if lagu in playlist:
                playlist.remove(lagu)
                print(f'Lagu "{lagu}" dihapus.')
            else:
                print("Lagu tidak ditemukan!")

        elif choice == 3:
            if len(playlist) == 0:
                print("Playlist kosong.")
            else:
                print("\nPlaylist:")
                for i, lagu in enumerate(playlist):
                    print(f"{i + 1}. {lagu}")

        elif choice == 4:
            try:
                index = int(input("Masukkan nomor lagu: "))
                print(f"Memutar lagu: {playlist[index - 1]}")
            except (ValueError, IndexError):
                print("Index tidak valid!")

        elif choice == 5:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()