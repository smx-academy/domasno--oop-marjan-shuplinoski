from operator import attrgetter


class Akter:
    def __init__(self, ime: str, prezime: str, godina: int, br_filmovi: int, br_nagradi: int, oskar: str):
        self.ime = ime
        self.prezime = prezime
        self.godina = godina
        self.br_filmovi = br_filmovi
        self.br_nagradi = br_nagradi
        self.oskar = oskar

    def setIme(self, novoIme):
        self.ime = novoIme

    def getIme(self):
        return self.ime

    def setPrezime(self, novoPrezime):
        self.prezime = novoPrezime

    def getPrezime(self):
        return self.prezime

    def setGodina(self, novaGodina):
        self.godina = novaGodina

    def getGodina(self):
        return self.godina

    def setBrFilmovi(self, novBrFilmovi):
        self.br_filmovi = novBrFilmovi

    def getBrFilmovi(self):
        return self.br_filmovi

    def setBrNagradi(self, novBrNagradi):
        self.br_nagradi = novBrNagradi

    def getBrNagradi(self):
        return self.br_nagradi

    def setOskar(self, novOskar):
        self.oskar = novOskar

    def getOskar(self):
        return self.oskar


objects = list()

for i in range(5):
    imeAkter = input("Vnesi ime na Akter: ")
    prezimeAkter = input("Vnesi prezime na Akter: ")
    godinaAkter = int(input("Vnesi godini na Akter: "))
    brFilmoviAkter = int(input("Vnesi br na filmovi na Akter: "))
    brNagradiAkter = int(input("Vnesi br na nagradi na Akter: "))
    oskarAkter = input("Vnesi dali dobil oskar (da/ne) ")
    objects.append(Akter(imeAkter, prezimeAkter, godinaAkter, brFilmoviAkter, brNagradiAkter, oskarAkter))

print("__" * 25)

for obj in objects:
    print("Ime:", obj.ime)
    print("Prezime:", obj.prezime)
    print("Godina na ragjanje: ", obj.godina)
    print("Broj na filmovi: ", obj.br_filmovi)
    print("Broj na nagradi: ", obj.br_nagradi)
    print("Dobien Oskar: ", obj.oskar)
    print("__" * 25)

najgolemi_nagradi = max(objects, key=attrgetter('br_nagradi'))
print("Najgolem br nagradi ima {} {} vkupno nagradi {}".format(najgolemi_nagradi.ime, najgolemi_nagradi.prezime,
                                                               najgolemi_nagradi.br_nagradi))
