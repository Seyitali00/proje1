NOT = int(input("Ortalama kaç"))
if NOT<=100 and NOT>=0:
    if NOT>85 : print("çok iyi")
    elif NOT>70 : print("iyi")
    elif NOT>=50 : print("Eh")
    if NOT<50 : print("Daha Çok Çalış")
else:
    print("Öyle bir not yok")