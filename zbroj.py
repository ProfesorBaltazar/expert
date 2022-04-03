def umnozak(prvi_broj, drugi_broj):
    if drugi_broj == prvi_broj:
        return prvi_broj
    else:
        return drugi_broj * umnozak(prvi_broj, drugi_broj - 1)


def main():
    prvi_broj = int(input('Unesi prvi broj : '))
    drugi_broj = int(input('Unesi drugi broj: '))

    if prvi_broj <= drugi_broj:
        rezultat = umnozak(prvi_broj, drugi_broj)
        print('Rezultat = ', rezultat)
    else:
        print('Neispravni podaci: Prvi broj mora biti manji od drugoga ')


main()
