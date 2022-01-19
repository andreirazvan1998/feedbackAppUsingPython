import random

import Tara
import Judet
from random import *

class Adresa:
    __listaID=[] #atribut de clasa, atribut STATIC si privat
    def __init__(self, id,s, n, b, a, o, j, c, t):
        self.__strada = s
        self.__numar = n
        self.__bloc = b
        self.__apartament = a
        self.__oras = o
        self.__judet = j
        self.__codPostal = c
        self.__tara = t
        self.gdpr=True
        x=random.randint(1000,100000)
        while x in Adresa.__listaID:
            x = random.randint(1000, 100000)
        self.__id=x



    def __str__(self):
        return "Strada: {}, Numar: {}, Bloc: {}, Apartament: {}, Oras: {}, {}, Cod Postal: {}, {},id".format(self.__strada,self.__numar,self.__bloc,
                                                                                                          self.__apartament,
                                                                                                          self.__oras,
                                                                                                          self.__judet,
                                                                                                          self.__codPostal,
                                                                                                          self.__tara,
                                                                                                          self.__id)
        return s

    def getStrada(self):
        return self.__strada

    def getNumar(self):
        return self.__numar

    def getBloc(self):
        return self.__bloc

    def getApartament(self):
        return self.__apartament

    def getOras(self):
        return self.__oras

    def getJudet(self):
        return self.__judet

    def getCodPostal(self):
        return self.__codPostal

    def getTara(self):
        return self.__tara

    def gdprAccord(self):
        gdprAccord = True
        return gdprAccord

a1=Adresa("Revolutiei", "12A", 62, 4, "Timisoara", Judet.Judet.Timis, 300145, Tara.Tara.Romania)
a2=Adresa("Clabucet", "10", None, None, "Oravita", Judet.Judet.CarasSeverin, 325600, Tara.Tara.Romania)