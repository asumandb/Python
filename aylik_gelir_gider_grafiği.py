import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

gelir = np.random.randint(20000, 50000, 12)
gider = np.random.randint(15000, 40000, 12)

df = pd.DataFrame({"Ay": aylar, "Gelir" : gelir, "Gider" : gider })

plt.figure(figsize = (8,4))
plt.bar(aylar, gelir, color = "blue")
plt.bar(aylar, gider, color= "green")

plt.title("Aylık Gelir Gider Grafiği")
plt.xlabel("Ay")
plt.ylabel("Miktar")
plt.show()
