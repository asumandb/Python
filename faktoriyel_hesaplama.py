def Faktoriyel(n):
    if n < 0:
        return "negatif sayı girdiniz"

    elif n == 0 and n == 1:
       return 1

    else:
        sonuc = 1
        for i in range(2, n+1):
         sonuc *= i
    return sonuc

sayi = int(input("sayı girin"))
factorielsonuc = Faktoriyel(sayi)
print(f"{sayi}! = {factorielsonuc}" )
