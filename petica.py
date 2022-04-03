def djeljiv_s_pet(broj):
    x = ' nije djeljiv s 5'
    if broj % 5 == 0:
        x = ' je djeljiv s 5'
    return x


def main():
    broj = int(input(' Unesi broj:  '))
    povratna_informacija = djeljiv_s_pet(broj)
    print('Uneseni broj ', broj, povratna_informacija)


main()
