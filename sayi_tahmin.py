import tkinter as tk
import random


class Oyun:
    def __init__(self):
        self.yeni()

    def yeni(self):
        self.__sayi = random.randint(1, 100)  # private: dışarıdan erişilemez
        self.deneme = 0

    def tahmin_et(self, t):
        self.deneme += 1
        if t < self.__sayi:
            return "Daha büyük!"
        if t > self.__sayi:
            return "Daha küçük!"
        return f"Doğru, {self.deneme} denemede buldun!"


class Arayuz:
    def __init__(self, pencere):
        self.oyun = Oyun()
        pencere.title("Sayı Tahmin Oyunu")
        tk.Label(pencere, text="1-100 arası bir sayı tut:").pack(pady=5)
        self.giris = tk.Entry(pencere)
        self.giris.pack()
        tk.Button(pencere, text="Tahmin Et", command=self.tahmin).pack(pady=5)
        self.sonuc = tk.Label(pencere, text="")
        self.sonuc.pack()
        tk.Button(pencere, text="Yeni Oyun", command=self.yeni).pack(pady=5)

    def tahmin(self):
        try:
            self.sonuc.config(text=self.oyun.tahmin_et(int(self.giris.get())))
        except ValueError:
            self.sonuc.config(text="Lütfen bir sayı gir!")

    def yeni(self):
        self.oyun.yeni()
        self.giris.delete(0, tk.END)
        self.sonuc.config(text="Yeni oyun başladı!")


pencere = tk.Tk()
Arayuz(pencere)
pencere.mainloop()
