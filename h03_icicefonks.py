def hesapla(a,b,c):
    def topla(a,b):
        print("Toplam:", a+b)

    def carp(a,b):
        print("Çarpım:", a*b)

    if c=="+": topla(a,b)
    elif c=="*": carp(a,b)
    elif c not in ["+","*"]:
        print("böyle bir işlem yoktur")
hesapla(7,9,"/")