class Arac:
    def __init__(self, plaka, marka, model):
        self.plaka = plaka
        self.marka = marka
        self.model = model

    def show_info(self):
        print(f"Plaka: {self.plaka}, Marka: {self.marka}, Model: {self.model}")

class BinekArac(Arac):
    def __init__(self, plaka, marka, model, kapi_sayisi):
        super().__init__(plaka, marka, model)
        self.kapi_sayisi = kapi_sayisi

    def show_info(self):
        super().show_info()
        print(f"Kapı Sayısı: {self.kapi_sayisi}")

class TicariArac(Arac):
    def __init__(self, plaka, marka, model, yuk_kapasitesi):
        super().__init__(plaka, marka, model)
        self.yuk_kapasitesi = yuk_kapasitesi

    def show_info(self):
        super().show_info()
        print(f"Yük Kapasitesi: {self.yuk_kapasitesi}")

binek = BinekArac("35 ASD 35", "Renault", "Clio", 4)
ticari = TicariArac("35 XYZ 35", "Ford", "Transit", 2 )

binek.show_info()
ticari.show_info()
