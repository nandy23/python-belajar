jam = int (input("masukin jam :"))
menit = int (input("masukin menit :"))
detik = int (input("masukin detik :"))

total_detik = (int(jam)*3600) + (int(menit)*60) + int(detik)
print(str(jam)+":"+str(menit)+":"+str(detik)+": "+"Sama dengan "+str(total_detik)+" detik")
