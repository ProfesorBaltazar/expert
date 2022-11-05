# napravimo broj s obratnim poretkom znamenki i usporedimo ga s polaznim brojem
# palindrom je broj koji se čita jednako s obje strane 14741 
n = int(input("Unesi broj:  "))
temp = n 
inverz = 0
while n!=0:
    z = n % 10
    inverz = inverz*10 + z
    n = n//10
if (inverz == temp):
    print("Broj je palindrom")
else:
    print("Broj nije palindrom")