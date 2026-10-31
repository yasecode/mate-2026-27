#indirim hesaplama#


indirimtutari = float(input("indirim yuzdesini giriniz: "))
fiyat = float(input("fiyati giriniz: "))

indirimtutari = fiyat * indirimtutari / 100
sonfiyat = fiyat - indirimtutari



print(f"indirimden kazanciniz: {indirimtutari}   ")
print(f"indirimli son fiyat: {sonfiyat} ")
