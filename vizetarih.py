#vize sayaç#
from datetime import datetime
print("Vize sayacina hosgeldiniz")
print("Lutfen vize tarihini giriniz (YYYY-AA-GG) formatinda")
while True:
    try:
        vizetarih = input("Vize tarihi: ")
        vizetarih = datetime.strptime(vizetarih, "%Y-%m-%d")
        simdi = datetime.now()
        if vizetarih < simdi:
            print("Gecmis olsun kankam, lutfen tekrar dene.")
            continue
        fark = vizetarih - simdi
        gun = fark.days
        saat = fark.seconds // 3600
        dakika = (fark.seconds // 60) % 60
        print(f"Vizeye {gun} gun, {saat} saat ve {dakika} dakika kaldi.")
        break
    except ValueError:
        print("Yanlis tarih formati. Lutfen YYYY-AA-GG formatinda girin.")
