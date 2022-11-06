m=int(input("Unesi broj:  ")) #unesi veći broj
n=int(input("Unesi broj:  ")) #unesi manji broj
while n!=0: # sve dok je n različit od 0 ponavljaj
    pom=n   # n spremi u pomoćnu varijablu
    n=m%n   # u varijablu n spremi ostatak pri dijeljenju m i n
    m=pom   # u m spremi vrijednost od n koja se mijenja pri prolasku kroz petlju
print(m)    # ispiši m