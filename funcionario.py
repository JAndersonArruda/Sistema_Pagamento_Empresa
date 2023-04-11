from pessoa import Pessoa as P


class Funcionario(P):
    def __init__(self, nome, fone, endereco, cpf, salarioBruto, descontos, bonificacoes):
        P.__init__(self, nome, fone, endereco, cpf, salarioBruto)
        self._descontos = descontos
        self._bonificacoes = bonificacoes

    # get
    @property
    def descontos(self):
        return self._descontos

    @property
    def bonificacoes(self):
        return self._bonificacoes

    # set
    @descontos.setter
    def descontos(self, valor):
        self._descontos = valor
        return self._descontos

    @bonificacoes.setter
    def bonificacoes(self, valor):
        self._bonificacoes = valor
        return self._bonificacoes

    def calculaSalarioLiquido(self):
        valor = self._descontos - (197 + 15)
        salarioLiquido = (self._salarioBruto + self._bonificacoes) - valor
        print(F"Salario Liquido:{salarioLiquido}")
