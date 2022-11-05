n=int(input("Unesite broj:  ")) # Unesite prirodan broj 
zbroj=0            # postavite brojac na nulu
while n!=0:        #ponavljaj sve dok je n razlicito od nula
    z=n%10         #MOD izdvoji zadnju znamenku
    zbroj=zbroj+z  #zbroji zadnju znamenku sa zbrojem
    n=n//10        #cjelobrojno dijeljenje, obriši zadnju zanmenku
print(zbroj)

