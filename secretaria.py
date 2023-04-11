from funcionario import Funcionario as F
from abc import ABC, abstractmethod


class Secretaria(F, ABC):
    def __init__(self, nome, fone, endereco, cpf, salarioBruto, descontos, bonificacoes):
        F.__init__(self, nome, fone, endereco, cpf,
                   salarioBruto, descontos, bonificacoes)

    @abstractmethod
    def paraFuturo(self):
        pass
