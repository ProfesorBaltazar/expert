n=int(input("Unesi broj:  "))
d=2  # d=2 jer je 1 najmanji djeljitelj
while n%d!=0: # ponavljaj sve dok je ostatak pri dijeljenju različit od 0
    d=d+1
print(n//d)


