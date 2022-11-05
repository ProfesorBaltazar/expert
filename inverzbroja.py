n = int(input("Unesi broj:  "))
inverz=0
while n!=0:
    z = n%10     # zadnja znamenka
    inverz = inverz*10 + z  
    n = n//10
print(inverz)
