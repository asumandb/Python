while True:
    print("1.şifrele")
    print("2.çöz")
    print("3.çıkış")
    secenek = input("bir seçenek girin (1/2/3):")

    if secenek == "1":
        metin = input("şifrelenecek olan metni girin")
        kaydirma = int(input("kaydırma miktarını girin (örneğin(3))"))

        sifreli_metin = []
        for karakter in metin:
            if karakter.isalpha():
                kaydirma_egik = kaydirma%26
                base = ord("a") if karakter.islower() else ord("A")
                sifreli_karakter = chr((ord(karakter) - base + kaydirma_egik) % 26 + base) 
                sifreli_metin.append(sifreli_karakter)

            else:
                sifreli_metin.append(sifreli_karakter)

        print(f"Şifreli metin: {sifreli_metin}")
        
    elif secenek == "2":
         metin = input("çözelecek olan metni girin")
         kaydirma = int(input("kaydırma miktarını girin (örneğin(3))"))

         sifreli_metin = []
         for karakter in metin:
            if karakter.isalpha():
                kaydirma_egik = -kaydirma%26
                base = ord("a") if karakter.islower() else ord("A")
                sifreli_karakter = chr((ord(karakter) - base + kaydirma_egik) % 26 + base) 
                sifreli_metin.append(sifreli_karakter)

            else:
                sifreli_metin.append(sifreli_karakter)

         print(f"Şifreli metin: {sifreli_metin}")
    elif secenek == "3":
        break
        
