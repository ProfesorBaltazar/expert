n = int(input("Unesi broj:  "))
min=9 # pretpostavimo da je 9 najveća znamenka u broju
while n !=0:
    z = n%10    # uzimamo zadnju znamenku 
    if z < min: # ako je z manje od 9
        min=z   # onda min prima vrijednost z
    n = n//10   # brišemo zadnju znamenku
print(min)

