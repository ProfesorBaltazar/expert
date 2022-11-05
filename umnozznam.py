n=int(input("Unesite broj:  "))
umnoz=0
while n!=0:
    z=n%10
    umnoz=umnoz*z
    n=n//10
print(umnoz)