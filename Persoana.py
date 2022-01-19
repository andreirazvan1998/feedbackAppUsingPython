from Judet import Judet
from Adresa import Tara
from Adresa import Adresa
from Sex import Sex

class Persoana:
    def __init__(self, cnp, n, p, c, e, t, a, s, dn, v):
        self.__cnp = cnp
        self.nume = n
        self.prenume = p
        self.__calitate = c
        self.__emails = e
        self.__telefoane = t
        self.__adrese = a
        self.__sex = s
        self.__dataNasterii = dn
        self.__varsta = v

    def __repr__(self):
        return "Nume:" + self.nume

    def validareCNP(self):
        validareCNP = True
        return validareCNP

    def addEmail(self):
        addEmail = True
        return addEmail

    def isEmailValid(self):
        isEmailValid = True
        return isEmailValid

    def getEmails(self):
        return self.__emails

    def addTelefon(self):
        addTelefon = True
        return addTelefon

    def isTelefonValid(self):
        isTelefonValid = True
        return isTelefonValid

    def addAdresa(self):
        self.adresa = "Romania"
        return

    def getAdresa(self):
        return self.adresa

    def deleteEmail(self):
        return

    def deleteTelefon(self):
        return

    def deleteAdresa(self):
        return

    def getPersoana(self):
        return

    def validareCNP(self, s):
        v = []  # lista de cifre
        for c in s:
            v.append(int(c))
        if len(v) != 13:
            return False
        if 1 > v[0] and v[0] > 8:
            return False
        an = 0
        if v[0] in [1, 2]:
            an = 1900
        if v[0] in [3, 4]:
            an = 1800
        if v[0] in [5, 6]:
            an = 2000
        an = an + v[1] * 10 + v[2]
        luna = v[3] * 10 + v[4]
        zi = v[5] * 10 + v[6]
        if an <= 0 or luna <= 0 or zi <= 0:
            return False
        if luna in [1, 3, 5, 7, 8, 10, 12] and zi > 31:
            return False
        elif luna in [4, 6, 9, 11] and zi > 30:
            return False
        elif luna == 2 and an % 4 == 0 and zi > 29:
            return False
        elif luna == 2 and an % 4 != 0 and zi > 28:
            return False
        listaJudete = [judet.value[0] for judet in Judet]
        listaJudete.append(41)
        listaJudete.append(42)
        listaJudete.append(46)
        j = v[7] * 10 + v[8]
        if not j in listaJudete:
            return False
        c = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
        s = 0
        for i in range(0, 12):
            s += c[i] * v[i]
        cifraControl = 0
        if s % 11 == 10:
            cifraControl = 1
        else:
            cifraControl = s % 11
        if cifraControl != v[12]:
            return False
        return True


R = Adresa("xxx", 1, "-", 1, "Timisoara", Judet.Timis, 300260, Tara.Romania)

p = Persoana("1820521445897", "Ion", "Ionescu", "Cursant", "cursant@it-labs.ro", "0724561765", R, Sex.MASCULTIN,
             "12.12.1982", "39")
print(p.validareCNP("1820521445897"))