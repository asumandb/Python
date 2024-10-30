import random

def tahmin_oyunu():
    sayi = random.randint(1,100)
    while True:
        tahmin = int(input("Tahmin ettiğiniz sayıyı girin"))
        if tahmin > sayi:
            print("Daha küçük bir sayı girin")

        elif tahmin < sayi:
            print("Daha büyük bir sayı girin")

        elif tahmin == sayi:
            print("Tahmininiz doğru")
            break

tahmin_oyunu()
