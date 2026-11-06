#tahmin oyunu#
import random

sayi = random.randint(1, 100)
tahmin = None

while tahmin != sayi:
    try:
        tahmin = int(input("1-100 arasinda bir sayi giriniz: "))
        if tahmin < sayi:
            print("daha buyuk bir sayi girin")
        elif tahmin > sayi:
            print("daha kucuk bir sayi gir")
        else:
            print("helal bildin lan!")
    except ValueError:
        print("gecersiz karakter, lutfen tekrar dene")