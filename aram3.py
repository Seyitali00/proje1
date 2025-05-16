import turtle as t
import random

def cizim():
    print("\33[1;31;40m")
    print("╔═════════════════════╗")
    print("║     Çizimler        ║")   
    print("║  1-Kare             ║")
    print("║  2-Dikdörtgen       ║")
    print("║  3-Daire            ║")
    print("║  4-Üçgen            ║")
    print("║  5-Rastgele Desen   ║")
    print("║  6-Ana Menüye Dön   ║")
    print("║     Seçim Yapın     ║") 
    print("╚═════════════════════╝")

    secim = input("Seçiminizi yapınız: ")

    if secim == "1":
        print("Kare çiziliyor...")
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)

        input()

    if secim == "2":
        print("Dikdörtgen Çiziliyor...")
        t.forward(160)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(160)
        t.right(90)
        t.forward(100)

        input()

    if secim == "3":
        print("Daire çiziliyor...")
        t.circle(90)

        input()

    if secim == "4":
        print("Üçgen Çiziliyor")
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(120)
        t.forward(100)

        input()

    if secim == "5":
        print("Rastgele Çiziliyor...")
        t.speed(0)
        t.bgcolor("black")
        colors = ["red", "green", "blue","green", "purple","yellow","orange"]

        angle = random.choice([90, 100, 150, 120, 60, 220, 135, 160])

        for i in range(1000):
            t.color(random.choice(colors))
            t.forward(i*1)
            t.right(angle)
            t.forward(i*3)
            t.right(angle)
    
        t.done()

    if secim == "6":
        print("Ana Menüye Dönülüyor...")
        import anamenu
        anamenu.anamenu()