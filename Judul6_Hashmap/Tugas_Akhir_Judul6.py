class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)

        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\n===== DAFTAR MENU KOPI =====")

        for i in range(self.SIZE):
            if self.table[i] is not None:  # hanya slot yang berisi data
                print(f"Slot {i}: ", end="")

                current = self.table[i]

                while current is not None:
                    print(
                        f"[ID:{current.key}, "
                        f"{current.value['nama']}, "
                        f"Rp{current.value['harga']:,}]".replace(",","."),
                        end=""
                    )
                    current = current.next

                print()


def main():
    hashmap = HashMapSeparateChaining()

    while True:
        print("\n===== SISTEM MANAJEMEN MENU KOPI =====")
        print("1. Tambah Menu Kopi")
        print("2. Cari Menu Kopi")
        print("3. Hapus Menu Kopi")
        print("4. Tampilkan Semua Menu")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_kopi = int(input("Masukkan ID Kopi : "))
            nama = input("Masukkan Nama Kopi : ")
            harga = int(input("Masukkan Harga Kopi : "))

            data_kopi = {
                "nama": nama,
                "harga": harga
            }

            hashmap.insert(id_kopi, data_kopi)

            print("Menu kopi berhasil ditambahkan!")

        elif pilihan == "2":
            id_kopi = int(input("Masukkan ID Kopi yang dicari : "))

            hasil = hashmap.search(id_kopi)

            if hasil is not None:
                print("\n=== MENU DITEMUKAN ===")
                print(f"ID Kopi    : {hasil.key}")
                print(f"Nama Kopi  : {hasil.value['nama']}")
                print(
                    f"Harga Kopi : Rp{hasil.value['harga']:,}".replace(",", ".")
                )
            else:
                print("Menu kopi tidak ditemukan.")

        elif pilihan == "3":
            id_kopi = int(input("Masukkan ID Kopi yang akan dihapus : "))

            if hashmap.remove_key(id_kopi):
                print("Menu kopi berhasil dihapus.")
            else:
                print("Menu kopi tidak ditemukan.")

        elif pilihan == "4":
            hashmap.display()

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()