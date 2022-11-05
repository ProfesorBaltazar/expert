n = int(input("Upiši cijeli broj:  "))
br=0
while n!=0:   #dok je n različito od nula ponavljaj
    br=br+1   # brojač prolaska kroz petlju
    n = n//10 # cjelobrojno dijeljenje, brisanje znamenke
print(br)
 