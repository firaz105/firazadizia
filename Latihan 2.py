def hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas):
    total_kehadiran = kehadiran * 16
    total_tugas = sum(nilai_tugas)
    nilai_akhir = total_kehadiran + total_tugas + nilai_uts + nilai_uas
    return nilai_akhir

def tentukan_hasil_nilai(nilai_akhir):
    if nilai_akhir >= 90:
        return 'A'
    elif nilai_akhir >= 80:
        return 'B'
    elif nilai_akhir >= 70:
        return 'C'
    elif nilai_akhir >= 60:
        return 'D'
    else:
        return 'E'

# Input nilai dari pengguna
kehadiran = int(input("Masukkan jumlah kehadiran mahasiswa: "))
nilai_tugas = []
for i in range(8):
    nilai = float(input(f"Masukkan nilai tugas {i+1}: "))
    nilai_tugas.append(nilai)
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# Hitung nilai akhir dan tentukan hasil nilai kelulusan
nilai_akhir = hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas)
hasil_nilai = tentukan_hasil_nilai(nilai_akhir)

print(f"Nilai akhir mahasiswa: {nilai_akhir}")
print(f"Hasil nilai kelulusan: {hasil_nilai}")
