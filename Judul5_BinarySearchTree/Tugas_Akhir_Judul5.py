class Node:
    def __init__(self, nilai):
        self.nilai = nilai
        self.left = None
        self.right = None


class BSTRanking:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nilai):
        if root is None:
            return Node(nilai)
        if nilai < root.nilai:
            root.left = self.insert_node(root.left, nilai)
        elif nilai > root.nilai:
            root.right = self.insert_node(root.right, nilai)
        return root

    def insert(self, nilai):
        if self.search(self.root, nilai):
            return False
        self.root = self.insert_node(self.root, nilai)
        return True

    def search(self, root, nilai):
        if root is None:
            return False
        if nilai == root.nilai:
            return True
        elif nilai < root.nilai:
            return self.search(root.left, nilai)
        else:
            return self.search(root.right, nilai)

    def find_min(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, nilai):
        if root is None:
            return None
        if nilai < root.nilai:
            root.left = self.delete_node(root.left, nilai)
        elif nilai > root.nilai:
            root.right = self.delete_node(root.right, nilai)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min(root.right)
                root.nilai = successor.nilai
                root.right = self.delete_node(
                    root.right,
                    successor.nilai
                )
        return root

    def delete(self, nilai):
        if not self.search(self.root, nilai):
            return False
        self.root = self.delete_node(self.root, nilai)
        return True

    def tampilkan_ranking(self, root):
        if root is not None:
            self.tampilkan_ranking(root.right)
            print(root.nilai)
            self.tampilkan_ranking(root.left)

    def height(self, root):
        if root is None:
            return -1
        kiri = self.height(root.left)
        kanan = self.height(root.right)
        return 1 + max(kiri, kanan)
    
    def is_empty(self):
        return self.root is None


def main():
    bst = BSTRanking()
    pilih = 0
    while pilih != 6:

        print("\n================================")
        print("      PROGRAM RANKING KELAS")
        print("================================")
        print("1. Tambah Nilai")
        print("2. Hapus Nilai")
        print("3. Tampilkan Ranking")
        print("4. Cari Nilai")
        print("5. Tinggi BST")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            try:
                nilai = int(input("Masukkan nilai siswa: "))
                berhasil = bst.insert(nilai)
                if berhasil:
                    print(f"Nilai {nilai} berhasil ditambahkan!")
                else:
                    print("Nilai sudah ada di ranking!")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                if bst.is_empty():
                    print("BST masih kosong!")
                else:
                    nilai = int(input(
                        "Masukkan nilai yang ingin dihapus: "
                    ))
                    berhasil = bst.delete(nilai)
                    if berhasil:
                        print(f"Nilai {nilai} berhasil dihapus!")
                    else:
                        print("Nilai tidak ditemukan!")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            if bst.is_empty():
                print("Ranking masih kosong!")
            else:
                print("\n=== RANKING KELAS ===")
                bst.tampilkan_ranking(bst.root)

        elif pilih == 4:
            try:
                if bst.is_empty():
                    print("BST masih kosong!")
                else:
                    nilai = int(input("Cari nilai: "))
                    ditemukan = bst.search(
                        bst.root,
                        nilai
                    )
                    if ditemukan:
                        print(
                            f"Nilai {nilai} ditemukan "
                            "dalam ranking!"
                        )
                    else:
                        print("Nilai tidak ditemukan!")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 5:
            if bst.is_empty():
                print("BST masih kosong!")
            else:
                print(
                    f"Tinggi BST: "
                    f"{bst.height(bst.root)}"
                )

        elif pilih == 6:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()