import random

def adam_asmaca():
    kelimeler = ["elma", "kitap", "masa", "araba", "python", "oyun", "kalem"]
    secilen = random.choice(kelimeler)
    gizli_kelime = ["_"] * len(secilen)
    tahmin_hakki = 6

    print("Adam Asmaca Oyununa Hoşgeldiniz!")
    print("Tahmin hakkınız:", tahmin_hakki)
    print(" ".join(gizli_kelime))

    for hak in range(tahmin_hakki):
        harf = input("Bir harf tahmin edin: ").lower()

        if harf in secilen:
            print("Doğru tahmin!")
            for i in range(len(secilen)):
                if secilen[i] == harf:
                    gizli_kelime[i] = harf
        else:
            print("Yanlış tahmin!")
            tahmin_hakki -= 1

        print(" ".join(gizli_kelime))
        print("Kalan hak:", tahmin_hakki)

        if "_" not in gizli_kelime:
            print("Tebrikler! Kelimeyi buldunuz:", secilen)
            break
    else:
        print("Hakkınız bitti! Kaybettiniz.")
        print("Doğru kelime:", secilen)
        