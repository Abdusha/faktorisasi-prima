import time

n = input("Masukan angka = ") #input angka
input = int(n) #konversi str ke int
batas = input + 1 #batasan
prima = [] #array bilangan prima
faktor = [] #array faktorisasi prima
x = 0
hasil = input

start = time.time()
print("Nilai =",input)
for i in range(2,batas):
    hitung = 0
    for j in range(1,i+1):
        div = i % j
        if(div == 0):
            hitung = hitung+1
    if(hitung == 2):
        prima.append(i)
        x = x + 1

print("Faktor prima =",prima)
print("Sebanyak =",x)

index = 0
while(hasil != 1):
    for k in range(x):
        if(hasil % prima[k] == 0):
            faktor.append(prima[k])
            old = hasil
            hasil = hasil/prima[k]
            index = index + 1
            if(hasil == 0):
                break
            print("faktorisasi ke-",index,":",old,"dengan",prima[k],"adalah",hasil)

end = time.time()
print("Faktorisasi =",faktor)
print("\nLama running =",(end - start),"detik")

