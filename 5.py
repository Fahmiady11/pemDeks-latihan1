def login(username,pwd):
    if username=="admin" and pwd=="fahmi37":
        print("anda berhasil masuk")
        return True
    else:
        print("maaf username dan password salah")
print("silahkan login")
d=0
for i in range(3):
    a=input("masukkan username:")
    b=input("masukkan password:")
    hasil=login(a,b)
    if hasil==True:
        break
    d+=1
if d==3:
    print("maaf tidak bisa lagi karena sudah 3 kali")
    
