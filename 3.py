def BMI(t,b):
    t=t/100
    h=t*t
    nilai=b/h
    if nilai<18.5:
        print("berat badan kurang")
    elif nilai<22.9:
        print("Berat badan normal")
    elif nilai<29.9:
        print("Berat badan berlebih")
    else:
        print("obesitas")
print("pengukuran BMI")
t=int(input("masukkan tinggi badan"))
b=int(input("masukkan berat badan"))
BMI(t,b)

