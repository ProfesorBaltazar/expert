n=int(input("Unesi broj:  "))
max=0   # pretpostavimo da je najveća znamenka 0
while n!=0:
    z = n%10    #zadnja znamenka
    if z > max: #ako je z veće od max 
        max=z   #z spremamo u max
    n =n//10    #brisanje zadnje zanemnke
print(max)
