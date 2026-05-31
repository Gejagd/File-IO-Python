import csv

"""
Variable of the name file.
"""
file_name = "data_nilai.csv"

"""
Data dummy
"""
data_mahasiswa = [
    ["Nama", "Nilai"],
    ["Andi", 85],
    ["Budi", 90],
    ["Cindy", 78],
    ["Sheila", 88]
]

total = 0
jumlah_data = 0

try:
    """
    Creating and writing to CSV file
    
    Pre-Condition:
    - File name picked from variable and created
    Post-Condition:
    - File successfully created and output message in CLI
    """
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data_mahasiswa)
    print("Data berhasil ditulis ke CSV.\n")

    """
    Reading and processing CSV file
    
    Pre-Condition:
    - CSV file is available and filled with prepared data
    Post-Condition:
    - Successfully reading the data through the file
    """
    print("=== Data Mahasiswa ===")
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            nama = row[0]
            nilai = int(row[1])  # Bisa raise ValueError jika nilai bukan integer
            print(f"{nama} : {nilai}")
            total += nilai
            jumlah_data += 1

    """
    Calculating Summary
    
    Pre-Condition:
    - Total of the grade and total data acquired
    Post-Condition:
    - Successfully calculated the average
    """
    rata_rata = total / jumlah_data  # Bisa raise ZeroDivisionError jika jumlah_data = 0
    print("\nTotal Nilai:", total)
    print("Rata-rata:", round(rata_rata, 2))

    """
    Adding Summary and Total back to the CSV
    
    Pre-Condition:
    - Summary variable acquired
    Post-Condition:
    - Output of the variable successfully inserted into CSV
    """
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([])  # Blank line
        writer.writerow(["Total", total])
        writer.writerow(["Rata-rata", round(rata_rata, 2)])

except FileNotFoundError:
    print(f"Error: File '{file_name}' tidak ditemukan.")
except ZeroDivisionError:
    print("Error: Tidak ada data mahasiswa yang terbaca (pembagian dengan nol).")
except ValueError:
    print("Error: Terjadi kesalahan format data saat membaca nilai (nilai harus berupa angka).")
except IOError as e:
    print(f"Error I/O: Terjadi kesalahan saat mengakses file: {e}")
except Exception as e:
    print(f"Terjadi kesalahan yang tidak terduga: {e}")
else:
    print("\nHasil berhasil ditambahkan ke CSV.")
    print("[ELSE] Seluruh operasi I/O dan perhitungan selesai dengan sukses!")
finally:
    print("[FINALLY] Program selesai dijalankan. Sesi ditutup.")