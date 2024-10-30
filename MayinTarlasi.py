import numpy as np
import pandas as pd

boyut = 10
mayin_sayisi = 15

# Oyun alanını oluşturalım
alan = np.zeros((boyut, boyut), dtype=int)

# Mayınları rastgele yerleştirelim
for i in range(mayin_sayisi):
    while True:
        x = np.random.randint(0, boyut)
        y = np.random.randint(0, boyut)
        if alan[x, y] != -1:
            alan[x, y] = -1  # Mayın yerleştir

            # Çevredeki hücrelerin sayısını güncelleyelim
            for i in range(max(0, x-1), min(boyut, x+2)):
                for j in range(max(0, y-1), min(boyut, y+2)):
                    if alan[i, j] != -1:
                        alan[i, j] += 1  # Mayın sayısını artır
            break  # Mayın başarıyla yerleştirildiğinde döngüden çık

# Gizli alanı gösterelim
gizli_alan = pd.DataFrame(' ', index=range(boyut), columns=range(boyut))

# Alanı ekrana yansıtalım
print("Mayın Tarlası Alanı:")
print(gizli_alan)

# Kullanıcıdan satır ve sütunu alalım
while True:
    try:
        x = int(input("Bir satır numarası seçin (0-9): "))
        y = int(input("Bir sütun numarası seçin (0-9): "))

        if alan[x, y] == -1:
            print("Patladınız! Oyun bitti.")
            break
        else:
            gizli_alan.iloc[x, y] = alan[x, y]  # Seçilen hücreyi güncelle
            print(gizli_alan)
    except (ValueError, IndexError):
        print("Geçersiz giriş! Lütfen 0-9 arasında bir değer girin.")