jam = int (input("masukin jam :"))
menit = int (input("masukin menit :"))
detik = int (input("masukin detik :"))

total_detik = (jam*3600) + (menit*60) + detik
print(jam+":"+menit+":"+detik+":"+"Sama dengan " + total_detik.format(jam,menit,detik)
