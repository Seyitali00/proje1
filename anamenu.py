import aramenu
import aramenu2
import aram3
def anamenu():
    print("\33[1;31;40m")
    print("╔═════════════════════╗")
    print("║                     ║")   
    print("║  1-Hesap Makinesi   ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Çizim            ║")
    print("║  4-Hava Durumu      ║")
    print("║  5-Çikis yap        ║")
    print("║                     ║")
    print("║                     ║") 
    print("╚═════════════════════╝")
    secim=input("Seçiminizi yapiniz : ")  
    if secim == "1" :
        print("Hesap Makinesi seçildi")
        aramenu.aramenu()
        
    if secim == "2" : 
        print("Oyunlar Secildi")
        aramenu2.menu2()

    if secim == "3" : 
        print ("Çizim Seçildi")
        aram3.cizim()

    if secim == "4" :
        print("Hava Durumu Seçildi")

        
anamenu()