def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j][1] > temp[1]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah tugas: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan data tugas:")

    for i in range(n):
        nama = input(f"Nama tugas ke-{i+1}: ")
        while True:
            try:
                deadline = int(input(f"Deadline (hari): "))
                arr.append((nama, deadline))
                break
            except ValueError:
                print("Masukkan angka yang valid!")

    print(f"\nData sebelum diurutkan: {arr}")

    insertion_sort(arr, n)

    print("\n=== PRIORITAS TUGAS ===")
    for i in range(n):
        print(f"{i+1}. {arr[i][0]} - {arr[i][1]} hari lagi")


if __name__ == "__main__":
    main()