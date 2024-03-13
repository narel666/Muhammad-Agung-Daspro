# Data dictionary jadwal daspro IF2
jadwal_if2 = {
    'Senin': '08.00','kamis': '10.50','jumat':'08.00'
}

# Data dictionary jadwal daspro IF3
jadwal_if3 = {
    'Selasa': '08.00','Rabu': '10.50','Rabu':'15.00'
}

# Menggabungkan dua data dictionary
jadwal_combined = jadwal_if3.copy()
jadwal_combined.update(jadwal_if2)

# Menampilkan hasil gabungan
print("Jadwal gabungan IF3 dan IF2:")
print(jadwal_combined)
