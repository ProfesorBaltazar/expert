n=int(input("Unesite broj:  ")) # Unesite prirodan broj 
zbroj=0
while n!=0:
    z=n%10
    zbroj=zbroj+z
    n=n//10
print(zbroj)

