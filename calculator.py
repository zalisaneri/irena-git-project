print("selamat datang dikalkulator")
print("pilih /n")
print("1. pertambahan /n")
print("2. perkalian /n")
print("3. pengurangan/n ")
print("4. pembagian/n")
user = input("pilih angka: ")
x = int(input("masukkan angka yang ingin di hitung: "))
y = int(input("masukkan angka yang ingin dihitung: "))
if user == "1":
    hasil_1 = x + y 
    print(f"hasil : {hasil_1}")
elif user == "2" :
    hasil_2 = x * y 
    print(f"hasil : {hasil_2}")
elif user == "3" :
    hasil_3 = x - y 
    print(f"hasil : {hasil_3}")
elif user == "4" :
    hasil_4 = x / y 
    print(f"hasil : {hasil_4}")
else:
    print("input salah ")
print("terimakasih")
