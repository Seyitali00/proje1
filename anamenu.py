import aramenu2
import aramenu
def anamenu():
    print("\33[1;31;40m")
    print("╔═════════════════════╗")
    print("║                     ║")   
    print("║  1-Hesap Makinesi   ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Çizim            ║")
    print("║  4-Çikis yap        ║")
    print("║                     ║")
    print("║    Seçim yapin      ║") 
    print("╚═════════════════════╝")
    secim=input("Seçiminizi yapiniz : ")  
    if secim == "1" :
        print("Hesap Makinesi seçildi")
        aramenu.aramenu()
        anamenu()
    if secim == "2" : 
        print("Oyunlar Secildi")
        aramenu2.menu2()
        
anamenu()