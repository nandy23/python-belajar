print("Menentukan Nilai Maksimum Dari 3 Bilangan")

a = int(input("Masukan Bilangan Ke-1 : "))
b = int(input("Masukan Bilangan Ke-2 : "))
c = int(input("Masukan Bilangan Ke-3 : "))
# cara I
# if (a > b):
#     if(a > c):
#         mask = a
# else:
#     if (b > c):
#         maks = b
#     else:
#         mask = c

# cara II
if(a > b and a > c):
    maks = a
else:
    if (b > a and b > c):
        maks = b
    else:
        maks = c

print("Nilai Maksimum Adalah {}".format(maks))
