import enum
from enum import unique


@unique
class Judet(enum.Enum):
    def __init__(self, nrOrdine, nume, prescurtare, r, *serie):
        self.nrOrdine = nrOrdine
        self.nume = nume
        self.prescurtare = prescurtare
        self.serie = []
        self.regiune = r
        for s in serie:
            self.serie.append(s)

    def __str__(self):
        return "Judet {} ({})".format(self.nume, self.nrOrdine)

    def getNrOrdine(self):
        return self.nrOrdine

    def getPrescurtare(self):
        return self.prescurtare

    def getSerie(self):
        return self.serie

    def getRegiune(self):
        return self.regiune

    Alba = (1, "ALBA", "AB", 51, "AX")
    Arad = (2, "ARAD", "AR", 31, "AR", "ZR")
    Arges = (3, "ARGES", "AG", 11, "AS", "AZ")
    Bacau = (4, "BACAU", "BC", 60, "XC", "ZC")
    Bihor = (5, "BIHOR", "BH", 41, "XH", "ZH")
    Bistrita = (6, "BISTRITA-NASAUD", "BN", 41, "XB")
    Botosani = (7, "BOTOSANI", "BT", 71, "XT")
    Brasov = (8, "Brasov", "BV", 50, "BV", "ZV")
    Braila = (9, "Braila", "BR", 81, "XR")
    Bucuresti = (10, "Bucuresti", "B", 1, "DP", "DR", "DT", "DX", "RD", "RR", "RT", "RX", "RK")
    Buzau = (11, "Buzau", "BZ", 12, "BZ")
    CarasSeverin = (12, "Caras-Severin", "CS", 32, "KS")
    Calarasi = (13, "Calarasi", "CL", 91, "CL")
    Cluj = (14, "Cluj", "CJ", 40, "CJ", "KX")
    Constanta = (15, "Constanta", "CT", 90, "KT", "KZ")
    Covasna = (16, "Covasna", "CV", 52, "KV")
    Dambovita = (17, "Dambovita", "DB", 13, "DD")
    Dolj = (18, "Dolj", "DJ", 20, "DX", "DZ")
    Galati = (19, "Galati", "GL", 80, "GL", "ZL")
    Giurgiu = (20, "Giurgiu", "GR", 8, "GG")
    Gorj = (21, "Gorj", "GJ", 21, "GZ")
    Harghita = (22, "Harghita", "HR", 53, "HR")
    Hunedoara = (23, "Deva", "HD", 33, "HD")
    Ialomita = (24, "Slobozia", "IL", 92, "SZ")
    Iasi = (25, "Iași", "IS", 70, "MX", "MZ")
    Ilfov = (26, "București", "IF", 7, "IF")
    Maramures = (27, "Baia Mare", "MM", 43, "MM")
    Mehedinti = (28, "Drobeta-Turnu Severin", "MH", 22, "MH")
    Mures = (29, "Târgu Mureș", "MS", 54, "MS", "ZS")
    Neamt = (30, "Piatra Neamț", "NT", 61, "NT")
    Olt = (31, "Olt", "OT", 23, "OT")
    Prahova = (32, "Prahova", "PH", 10, "PH", "PH")
    SatuMare = (33, "Satu Mare", "SM", 44, "SM")
    Salaj = (34, "Salaj", "SJ", 45, "SX")
    Sibiu = (35, "Sibiu", "SB", 55, "SB")
    Suceava = (36, "Suceava", "SV", 72, "SV", "XV")
    Teleorman = (37, "Teleorman", "TR", 17, "TR")
    Timis = (38, "Timis", "TM", 30, "TM", "TZ")
    Tulcea = (39, "Tulcea", "TL", 82, "TC")
    Vaslui = (40, "Vaslui", "VS", 73, "VS")
    Valcea = (41, "VALCEA", "VL", 24, "VX")
    Vrancea = (42, "VRANCEA", "VN", 62, "VN")