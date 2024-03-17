def konversi_bilangan(nilai):
    print("Desimal:", nilai)
    print("Biner:", bin(nilai))
    print("Oktal:", oct(nilai))
    print("Heksadesimal:", hex(nilai))

while True:
    try:
        nilai = int(input("Masukkan nilai desimal (ketik 'exit' untuk keluar): "))
        konversi_bilangan(nilai)
    except ValueError:
        if input.lower() == 'exit':
            break
        else:
            print("Masukkan hanya bilangan desimal atau ketik 'exit' untuk keluar.")
