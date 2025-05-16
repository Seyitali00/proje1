from adamasmaca import adam_asmaca
from yilanoyunu import yilan
from tetris import tetris
def menu2():
    print("\33[1;31;40m")
    print("╔═════════════════════╗")
    print("║  Oyunlar            ║")   
    print("║  1-Tetris           ║")
    print("║  2-Adam asmaca      ║")
    print("║  3-Yilan            ║")
    print("║                     ║")
    print("║  4-Ana menuye don   ║")
    print("║    Seçim yapin      ║") 
    print("╚═════════════════════╝")

    secim=input("Seçiminizi yapiniz : ")  
    if secim == "1" : 
        print("Tetris Seçildi")
        tetris()
        menu2()
        
        
    elif secim == "2":
        print("Adam asmaca seçildi")
        adam_asmaca()
        menu2()
        
        

    elif secim == "3":
        print("Yılan seçidli")
        yilan()
        menu2()

    elif secim== "4":
        print("Ana menü açılıyor...")
        import anamenu
        anamenu.anamenu()
    