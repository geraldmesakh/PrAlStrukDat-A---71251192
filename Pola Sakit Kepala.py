def Pola_Sakit_Kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)

    if panjang != lebar:
        print("Panjang dan lebar harus sama!!")

    if panjang % 2 == 0 or lebar % 2 == 0:
        print("Panjang dan lebar harus ganjil!!")

    n = panjang
    tengah = n // 2

    for i in range(n):
        for j in range(n):
            jarak = max(abs(i - tengah), abs(j - tengah)) + 1
            nilai = jarak % 10
            if j == n - 1:
                print(nilai, end="")
            else:
                print(nilai, end=" ")
        print()