from random import *
lista = [randint(1, 20) for i in range(20)]
lista.sort()
print(lista)
#lista = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
#a = int(input('Unesi cijeli broj'))
pocetak = 0          # pocetni indeks
kraj = len(lista)-1  # zadnji indeks

while pocetak <= kraj:
    sredina = (pocetak + kraj)//2  # izračun indeksa srednjeg elementa
    if lista[sredina] == 10:        # ako je traženi element upravo srednji element
        print('Vrijednost 10 je na indeksu', sredina)  # u sortiranoj listi
        break
    elif lista[sredina] > 10:   # ako je srednj ielement liste veći od traženog
        kraj = sredina - 1
    else:               # ak oje srednji element liste manji od traženog
        pocetak = sredina + 1  # povećanje vrijednosti varijable početak
