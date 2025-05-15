def aramenu():
    print("\33[1;31;40m")
    print("╔═════════════════════╗")
    print("║  Hesap Makinesi     ║")   
    print("║  1-Toplama          ║")
    print("║  2-Çikarma          ║")
    print("║  3-Bölme            ║")
    print("║  4-Çarpma           ║")
    print("║  5-Anamenuye don    ║")
    print("║    Seçim yapin      ║") 
    print("╚═════════════════════╝")
    secim=input("Seçiminizi yapiniz : ")  
    if secim == "1" :
        print("Toplama seçildi")
        sayi1 = float(input("1.sayıyı girin:"))
        sayi2 = float(input("2.sayıyı girin:"))
        print("Sonuç:",sayi1+sayi2)
        
    elif secim == "2" : 
        print("Çikarma seçildi")  
        sayi1 = float(input("1.sayıyı girin:"))
        sayi2 = float(input("2.sayıyı girin:"))
        print("Sonuç:",sayi1-sayi2) 
        
    elif secim == "3" : 
        print("Bölme seçildi")
        sayi1 = float(input("1.sayıyı girin:"))
        sayi2 = float(input("2.sayıyı girin:"))
        if sayi2 == 0 : 
            print("Sıfıra bölüm olmaz")
        else: print("Sonuç:",sayi1/sayi2)
        
    elif secim == "4" : 
        print("Çarpma seçildi") 
        sayi1 = float(input("1.sayıyı girin:"))
        sayi2 = float(input("2.sayıyı girin:"))
        print("Sonuç:",sayi1*sayi2)
          
    elif secim== "5":
        print("Ana menü açılıyor...")
        import anamenu
        anamenu()

 
    