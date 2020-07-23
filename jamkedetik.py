print("Konversi jam ke detik")

jam = int(input("Masukan Jam : "))
menit = int(input("Masukan Menit : "))
detik = int(input("Masukan Detik : "))

total_detik = ((jam * 3600) + (menit * 60) + detik)

print(str(jam) + ":" + str(menit) + ":" + str(detik) + " Sama dengan " +
      str(total_detik) + " detik")
