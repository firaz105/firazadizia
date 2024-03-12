def hitung_gaji():
    nama_karyawan = input("Nama karyawan: ")
    gaji_pokok = float(input("Gaji pokok: "))
    jam_kerja_per_hari = 8

    print("Nama karyawan:", nama_karyawan)
    print("Gaji pokok:", gaji_pokok)
    print("Jam kerja per hari:", jam_kerja_per_hari)

    pilihan = input("Pilih Rician Gaji (1 untuk mingguan, 2 untuk harian): ")

    if pilihan == '1':
        gaji_mingguan = gaji_pokok / 48
        print("Gaji mingguan:", gaji_mingguan)
    elif pilihan == '2':
        gaji_harian = gaji_pokok / 8
        print("Gaji harian:", gaji_harian)
    else:
        print("Pilihan tidak valid!")

hitung_gaji() 
