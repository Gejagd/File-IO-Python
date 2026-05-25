import csv

file_name = "data_nilai.csv"

data_mahasiswa = [
    ["Nama", "Nilai"],  # Header
    ["Andi", 85],
    ["Budi", 90],
    ["Cindy", 78],
    ["Sheila", 88]
]

with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data_mahasiswa)

print("Data berhasil ditulis ke CSV.\n")

total = 0
jumlah_data = 0

print("=== Data Mahasiswa ===")
with open(file_name, mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        nama = row[0]
        nilai = int(row[1])

        print(f"{nama} : {nilai}")

        total += nilai
        jumlah_data += 1

rata_rata = total / jumlah_data
print("\nTotal Nilai:", total)
print("Rata-rata:", round(rata_rata, 2))

with open(file_name, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([])  # Blank line
    writer.writerow(["Total", total])
    writer.writerow(["Rata-rata", round(rata_rata, 2)])

print("\nHasil berhasil ditambahkan ke CSV.")