

sayi1 = int(input("1.Sayı Giriniz: "))

sayi2 = int(input("2.Sayı Giriniz: "))

islem=input("Yapmak İstediğiniz İşlem(+,-,*,/): ")


def Carp(x, y):
    return x * y


def Bol(x, y):
    return x / y


def Topla(x, y):
    return x + y


def Cikar(x, y):
    return x - y



if islem == '+':

    print("\n", sayi1, " + ", sayi2, " = ", Topla(sayi1, sayi2))

elif islem == '-':

    print("\n", sayi1, " - ", sayi2, " = ", Cikar(sayi1, sayi2))

elif islem == '*':

    print("\n", sayi1, " * ", sayi2, " = ", Carp(sayi1, sayi2))

elif islem == '/':

    print("\n", sayi1, "/ ", sayi2, " = ", Bol(sayi1, sayi2))
else:
    print(" Lütfen geçerli bir sayi giriniz ya da geçerli bir işlem seçiniz! ")