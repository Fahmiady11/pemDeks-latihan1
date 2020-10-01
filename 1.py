def rata(nilai):
    hasil2=0
    for i in nilai:
        i=int(i)
        hasil2+=i
    hasil2=hasil2/5
    print(hasil2)
hasil=[]
for i in range(5):
    nilai=input("masukkan angka:")
    hasil.append(nilai)
rata(hasil)
