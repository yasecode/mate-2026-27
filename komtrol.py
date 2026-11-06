#sayı kontrolu#

while True:
    try:
        sayi = int(input("bir sayi gir: "))
        print(f"helal lan sayi girdin: {sayi}")
        break
    except ValueError:
        print("gecersiz karakter, lutfen tekrar dene")