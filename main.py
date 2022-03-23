
import math

#zad 1

a=[]

for x in range(10):
    a.append(x-1)
print(a)

b=[]

for y in range(8):
    b.append(7**y)
print(b)

c = []
for z in b:
    if z % 2 == 0:
        c.append(z)
print(c)
#zad 2
#zad 3

produkty ={'mleko': 'L', 'kawa': 'kg', 'jajka': 'szt', 'chipsy': 'szt', 'czosnek':  'szt'}

sztuki = [i for i in produkty.values() if produkty.values() == 'szt']
print(sztuki)

#zad 4

def czy_jest_prostokatny():
    a = float(input("Podaj dlugosc 1 boku: "))
    b = float(input("teraz drugiego: "))
    c = float(input("i trzeciego: "))
    ab = a**2 + b**2
    c2 = c**2
    if(ab == c2):
        print("Jest prostokatny!")
    else:
       print("Nie jest prostokatny")

#czy_jest_prostokatny()

#zad 5

def pole_trapezu(a= 3, b=5, h = 4):

    pole = (a+b)*h/2
    print(pole)
#pole_trapezu()

#zad 6

def iloczyn_elementów():

    a = 1
    b = 4
    ile = 10

    c = a * b**ile
    print(c)
#iloczyn_elementów()











