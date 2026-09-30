# BOZ213d01u01-SayiTahminOyunu
Ruhan Sadef USTA 25040221 BÖTE 2.Sınıf
# Sayı Tahmin Oyunu

Python ve tkinter ile yazılmış, 1-100 arası bir sayıyı tahmin etmeye dayalı basit bir masaüstü oyunu. Nesne Tabanlı Programlama dersi için hazırlanmıştır.

## Nasıl Oynanır?

1. Kutuya 1-100 arası bir sayı yaz ve **Tahmin Et** butonuna bas.
2. Program "Daha büyük!" veya "Daha küçük!" diyerek seni yönlendirir.
3. Sayıyı bulunca kaç denemede bulduğun gösterilir.
4. **Yeni Oyun** butonuyla yeni bir sayı tutulur ve baştan başlarsın.

## Kurulum ve Çalıştırma

Sadece Python 3 gerekir. Harici kütüphane yoktur (tkinter Python ile birlikte gelir).

```bash
python sayi_tahmin.py
```

## Kod Yapısı

| Sınıf | Görevi |
|-------|--------|
| `Oyun` | Oyun mantığı: gizli sayıyı tutar, tahmini karşılaştırır, deneme sayısını sayar. |
| `Arayuz` | tkinter arayüzü: Entry, Button ve Label bileşenlerini oluşturur, kullanıcıdan veri alıp sonucu ekranda gösterir. |

## Kullanılan OOP Kavramları

- **Constructor:** `__init__` metotları nesneleri başlangıç durumuyla oluşturur.
- **Encapsulation:** Gizli sayı `__sayi` olarak private tanımlanmıştır, sadece `Oyun` sınıfının metotlarıyla kullanılır.
- **Composition:** `Arayuz` sınıfı içinde bir `Oyun` nesnesi tutar (has-a ilişkisi).
- **Sorumlulukların ayrılması:** Oyun mantığı ve arayüz ayrı sınıflardadır.

## Gereksinimler

- Python 3.x
- tkinter (standart kütüphane)
