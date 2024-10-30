class Dikdortgen:
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan_hesapla(self):
        return self.uzunluk*self.genislik

    def cevre_hesapla(self):
        return 2*(self.uzunluk + self.genislik)

    def kare_mi(dikdortgen):
      return dikdortgen.uzunluk == dikdortgen.genislik 


dikdortgen1 = Dikdortgen(5,5)
print("Alan:", dikdortgen1.alan_hesapla())
print("Çevre:", dikdortgen1.cevre_hesapla())
print("Kare mi", Dikdortgen.kare_mi(dikdortgen1))
