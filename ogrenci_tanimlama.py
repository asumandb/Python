class Ogrenci:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def tanit(self):
        print(f"Ad:{self.ad}, soyad: {self.soyad}, yaş:{self.yas}")

ogrenci1 = Ogrenci("asuman", "dirbisoğlu", 20)
ogrenci1.tanit()
