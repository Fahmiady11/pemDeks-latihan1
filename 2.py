def persegipan(x,p,l):
    if x==1:
        result=p*l
        print(result)
    else:
        p=2*p
        l=2*l
        print(p+l)
    

print("1.luas persegi panjang \n2.keliling persegi panjang")
x=int(input("masukkan angka 1/2 untuk memilih:"))
p=int(input("masukkan panjang persegi:"))
l=int(input("masukkan luas persegi:"))
persegipan(x,p,l)

    
