import random 
T_sayi = random.randint(1,100)

while True:
    G_sayi = int(input("tahmininizi girin"))

    if T_sayi < G_sayi:
        print("daha küçük sayı girin")

    elif T_sayi > G_sayi:
        print("daha büyük sayı girin")

    elif T_sayi == G_sayi:
        print("çıkılıyor")
        break 
    
