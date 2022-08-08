def function(sayi):
    if(sayi==1):
        return False
    elif(sayi==2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi % i== 0):
                return False
        return True

while True:
    sayı=input("sayı")
    if(sayı=="q"):
        print("program sonlandı")
        break
    else:
        sayı=int(sayı)
        if(function(sayı)):
            print(sayı,"asal sayıdır")
        else:
            print("asal sayı degıldır")


