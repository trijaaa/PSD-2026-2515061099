class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top_ptr = None

    def is_empty(self):
        return self.top_ptr is None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_ptr
        self.top_ptr = new_node
        print(f"Aktivitas '{x}' berhasil ditambahkan.")

    def pop(self):
        if self.is_empty():
            print("Riwayat aktivitas kosong.")
            return

        temp = self.top_ptr
        print(f"Aktivitas terakhir '{temp.data}' berhasil dihapus.")
        self.top_ptr = self.top_ptr.next

    def peek(self):
        if self.is_empty():
            print("Riwayat aktivitas kosong.")
            return

        print(f"Aktivitas terakhir: {self.top_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Riwayat aktivitas kosong.")
            return

        print("\n=== RIWAYAT AKTIVITAS ===")
        current = self.top_ptr
        nomor = 1

        while current is not None:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1

    def hitung_aktivitas(self):
        count = 0
        current = self.top_ptr

        while current is not None:
            count += 1
            current = current.next

        print(f"Total aktivitas: {count}")


def main():
    stack = StackLinkedList()
    pilih = 0

    while pilih != 6:
        print("\n=== STACK LINKED LIST ===")
        print("1. Tambah Aktivitas")
        print("2. Hapus Aktivitas Terakhir")
        print("3. Lihat Aktivitas Terakhir")
        print("4. Tampilkan Semua Aktivitas")
        print("5. Hitung Total Aktivitas")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            aktivitas = input("Masukkan aktivitas: ")
            stack.push(aktivitas)

        elif pilih == 2:
            stack.pop()

        elif pilih == 3:
            stack.peek()

        elif pilih == 4:
            stack.display()

        elif pilih == 5:
            stack.hitung_aktivitas()

        elif pilih == 6:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()