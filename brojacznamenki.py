n=int(input("Unesi broj:  "))
brojac=0
while n!=0:
    if n%10==2:
        brojac=brojac+1
    n=n//10
print(brojac)