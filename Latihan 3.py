# Data mahasiswa (username dan password)
data_mahasiswa = {
    'firaz': 'firaz123',
    'mahasiswainformatika': '1234',
    # Tambahkan data mahasiswa lainnya di sini
}

# Data mata kuliah dan dosen pengampuh
data_matkul = {
    'Daspro': 'Dosen1',
    'Logika Matematika': 'Dosen2',
    # Tambahkan data mata kuliah dan dosen pengampuh lainnya di sini
}

# Fungsi untuk autentikasi login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    return username, password

# Autentikasi login
while True:
    username, password = login()
    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")

# Input mata kuliah dan dosen pengampuh
while True:
    print("\nDaftar Mata Kuliah:")
    for mata_kuliah, dosen in data_matkul.items():
        print(f"{mata_kuliah}: {dosen}")
    
    mata_kuliah_input = input("\nMasukkan nama mata kuliah: ")
    
    if mata_kuliah_input in data_matkul:
        print(f"Dosen pengampuh untuk {mata_kuliah_input}: {data_matkul[mata_kuliah_input]}")
    else:
        print("Mata kuliah tidak ditemukan.")

    ulangi = input("\nApakah Anda ingin melihat mata kuliah lainnya? (ya/tidak): ")
    if ulangi.lower() != 'ya':
        break
