import enum
from enum import unique

@unique #adnotare de cod
class Tara(enum.Enum):
    def __init__(self, nrOrdineTara, numeTara, prescurtareTara, codPasaportTara, codIsoTara, prefixTelefonic):
        self.idTara = id
        self.numeTara = numeTara
        self.nrOrdineTara = nrOrdineTara
        self.prescurtareTara = prescurtareTara
        self.codPasaportTara = codPasaportTara
        self.codIsoTara = codIsoTara
        self.prefixTelefonicTara = prefixTelefonic

    def __str__(self):
        return "Tara {} ({})".format(self.numeTara, self.nrOrdineTara)

    def getNrOrdineTara(self):
        return self.nrOrdineTara

    def getNumeTara(self):
        return self.numeTara

    def getPrescurtareTara(self):
        return self.prescurtareTara

    def getCodIsoTara(self):
        return self.codIsoTara

    def getCodPasaportTara(self):
        return self.codPasaportTara

    def getPrefixTelefonic(self):
        return self.prefixTelefonicTara

    Romania = (36, "Romania", "RO", "ROU", 642, "+40")
    Andorra = (2, "Andorra", "AD", "AND", 20, "+376")
    '''
    Armenia = (3, "AM", "ARM", 32, "+374")
    Austria = (4, "AT", "AUT", 40, "+43")
    Azerbaidjan = (5, "AZ", "AZE", 31, "+994")
    Belarus = (6, "BY", "BLR", 112, "+375")
    Belgia = (7, "BE", "BEL", 56, "+32")
    BosniasiHertegovina = (8, "BA", "BIH", 70, "+387")
    Bulgaria = (9, "BG", "BGR", 100, "+359")
    Cehia = (10, "CZ", "CZE", 203, "+42")
    Cipru = (11, "CY", "CYP", 196, "+357")
    Croatia = (12, "HR", "HRV", 191, "+385")
    Danemarca = (13, "DK", "DNK", 208, "+245")
    Elvetia = (14, "CH", "CHE", 756, "+41")
    Estonia = (15, "EE", "EST", 233, "+372")
    Finlanda = (16, "FI", "FIN", 246, "+358")
    Franta = (17, "FR", "FRA", 250, "+33")
    Georgia = (18, "GE", "GEO", 268, "+995")
    Germania = (19, "DE", "DEU", 276, "+49")
    Grecia = (20, "GR", "GRC", 300, "+30")
    Irlanda = (21, "IE", "IRL", 372, "+353")
    Islanda = (22, "IS", "ISL", 352, "+354")
    Italia = (23, "UT", "ITA", 380, "+39")
    Kazahstan = (24, "KZ", "KAZ", 398, "+7")
    Letonia = (25, "LV", "LVA", 428, "+371")
    Liechtenstein = (26, "LI", "LIE", 438, "+4175")
    Lituania = (27, "LT", "LTU", 440, "+370")
    Luxemburg = (28, "LU", "LUX", 442, "+352")
    Malta = (29, "MT", "MLT", 470, "+356")
    MareaBritanie = (30, "GB", "GBR", 826, "+44")
    Moldova = (31, "MD", "MDA", 498, "+373")
    Monaco = (32, "MC", "MCO", 492, "+33")
    Norvegia = (33, "NO", "NOR", 578, "+47")
    Polonia = (34, "PL", "POL", 616, "+48")
    Portugalia = (35, "PT", "PRT", 620, "+351")
    Rusia = (37, "RU", "RUS", 643, "+7")
    SanMarino = (38, "SM", " SMR", 674, "+378")
    Serbia = (39, "RS", "SRB", 220, "+381")
    Slovacia = (40, "SK", "SVK", 703, "+420")
    Slovenia = (41, "SI", "SVN", 705, "+386")
    Spania = (42, "ES", "ESP", 724, "+34")
    Suedia = (43, "SE", "SWE", 752, "+46")
    Turcia = (44, "TR", "TUR", 792, "+90")
    Ucraina = (45, "UA", "UKR", 804, "+380")
    Ungaria = (46, "HU", "HUN", 348, "+36")
    '''