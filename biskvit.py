from webbrowser import get


class Posuda:
    # poziv funkcije unosa biskvita
    def insertBiskvit(self, biskvit):
        self.biskvit = biskvit
# poziv funkcije ispisa biskvita

    def getBiskvit(self):
        print(self.biskvit)


# pozivi klase i funkcija
mojaPosuda = Posuda()
mojaPosuda.insertBiskvit('mojBiskvit')
mojaPosuda.getBiskvit()
