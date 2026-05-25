import csv

"""
Variable of the name file.
"""
file_name = "data_nilai.csv"

"""
Data dummy
"""
data_mahasiswa = [
    ["Nama", "Nilai"],  # Header
    ["Andi", 85],
    ["Budi", 90],
    ["Cindy", 78],
    ["Sheila", 88]
]

"""
Creating CSV file

Pre-Condition:
- File name picked from variable and created
Post-Condition:
- File succesfuly created and output message in CLI
"""
with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data_mahasiswa)

print("Data berhasil ditulis ke CSV.\n")

"""
Variable for summary and total

Pre-Condition:
- CSV file is available and filled with prepared data
Post-Condition:
- Successfully reading the data through the file
"""
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

"""
Summary variable

Pre-Condition:
- Total of the grade and total data acquired
Post-Condition:
- Succesfully Subtracted
- Output of the Sum variable in CLI
"""
rata_rata = total / jumlah_data
print("\nTotal Nilai:", total)
print("Rata-rata:", round(rata_rata, 2))

"""
Adding Summary and Total back to the CSV

Pre-Condition:
- Summary variable acquired
Post-Condition:
- Output of the variable succesfully inserted into CSV
"""
with open(file_name, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([])  # Blank line
    writer.writerow(["Total", total])
    writer.writerow(["Rata-rata", round(rata_rata, 2)])

print("\nHasil berhasil ditambahkan ke CSV.")