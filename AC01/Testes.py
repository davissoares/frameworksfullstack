from abc import ABC, abstractclassmethod


class Calcular(ABC):
    @abstractclassmethod
    def calculo(self, a, b):
        pass


class Dividir(Calcular):
    def calculo(a, b):
        return(a/b)


class Somar(Calcular):
    def calculo(a, b):
        return(a+b)


class Multiplicar(Calcular):
    def calculo(a, b):
        return(a*b)


class Subtrair(Calcular):
    def calculo(a, b):
        return(a-b)
