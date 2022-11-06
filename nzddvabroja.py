n=int(input("Unesi broj:  "))
m=int(input("Unesi broj:  "))
d=n # krenemo od jednog broja
while n%d !=0 or m%d !=0: # dok d nije djeljitelj od n ili d nije djeljitelj od m ponavljaj
    d=d-1 # smanji d za 1
print(d)
