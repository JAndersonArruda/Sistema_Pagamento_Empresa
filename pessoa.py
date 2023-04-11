from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, fone, endereco, cpf, salarioBruto):
        self._nome = nome
        self._fone = fone
        self._endereco = endereco
        self._cpf = cpf
        self._salarioBruto = salarioBruto

    # get
    @property
    def nome(self):
        return self._nome

    @property
    def fone(self):
        return self._fone

    @property
    def endereco(self):
        return self._endereco

    @property
    def cpf(self):
        return self._cpf

    @property
    def salarioBruto(self):
        return self._salarioBruto

    # set
    @fone.setter
    def fone(self, fone):
        self._fone = fone
        return self._fone

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
        return self._endereco

    # @salarioBruto.setter
    # def salarioBruto(self, valor):
    #   return self._salarioBruto = valor

    @abstractmethod
    def calculaSalarioLiquido(self):
        pass
