#harf notu hesaplama#
vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
toplam_not = (vize * 0.4) + (final * 0.6)

if toplam_not >= 90:
    print("Harf Notunuz: AA")
elif toplam_not >= 85:
    print("Harf Notunuz: BA")
elif toplam_not >= 80:
    print("Harf Notunuz: BB")
elif toplam_not >= 75:
    print("Harf Notunuz: CB")
elif toplam_not >= 70:
    print("Harf Notunuz: CC")
else:
    print("Harf Notunuz: FF")