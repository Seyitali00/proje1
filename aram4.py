def havadurumu():
    print("\33[1;31;40m")
    print("╔═════════════════════╗")
    print("║                     ║")   
    print("║  1-Ankara           ║")
    print("║  2-İstanbul         ║")
    print("║  3-İzmir            ║")
    print("║  4-Antalya          ║")
    print("║  5-Bursa            ║")
    print("║  6-Ana menüye dön   ║")
    print("║                     ║") 
    print("╚═════════════════════╝")

    secim = input("Bir şehir seçin(1-5)")

    if secim == "1":
        print("Ankara Bugün Güneşli, En yüksek sıcaklık 24 Derece")

    if secim == "2":
        print("İstanbul Bugün Parçalı Bulutlu, En Yüksek Sıcaklık 22 Derece")

    if secim == "3":
        print("İzmir Bugün Güneşli, En Yüksek sıcaklık 28 Derece") 

    if secim == "4":
        print("Antalya Bugün Güneşli, En Yüksek Sıcaklık 30 derece")

    if secim == "5":
        print("Bursa Bugün Güneşli, En Yüksek Sıcaklık 26 derece")   

    if secim== "6":
        print("Ana menü açılıyor...")
        import anamenu
        anamenu.anamenu() 

    