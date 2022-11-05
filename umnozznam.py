n=int(input("Unesite broj:  "))
umnoz=1
while n!=0:
    z=n%10     # zadnja znamenka
    umnoz=umnoz*z # umnozak zadnje znamenke i prethodne
    n=n//10  # brisanje znamenke
print(umnoz)