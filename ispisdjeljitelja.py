n = int(input("Unesi broj:  "))
for d in range (1,n+1): #za svaki d u intervalu od 1 do n+1 
    if n%d==0:    #provjeri da li je ostatak pri dijeljenju jednak nula
        print(d)