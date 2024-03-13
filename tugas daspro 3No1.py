# Data dictionary berisi username dan password mahasiswa
mahasiswa = {
    'Nabil': {'password': '123456'},
    'putra': {'password': '123456'},
    'Ilham': {'password': '123456'},
    'Safril': {'password': '123456'},
    'Arridoh': {'password': '123456'},
    'Ozan': {'password': '123456'},
    'Desstito': {'password': '123456'},
    'Sagri': {'password': '123456'},
    'Gatsu': {'password': '123456'},
    'Rafaell': {'password': '123456'}
}

# Meminta pengguna memasukkan username dan password
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# Memeriksa apakah kombinasi tersebut ada dalam dictionary mahasiswa
if username in mahasiswa and mahasiswa[username]['password'] == password:
    print("Login berhasil. Selamat datang, ", username)
else:
    print("Login gagal. Username atau password salah.")
