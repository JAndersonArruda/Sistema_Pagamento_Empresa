from secretaria import Secretaria as S


class SecretariaExecutiva(S):
    def __init__(self, nome, fone, endereco, cpf, salarioBruto, descontos, bonificacoes):
        S.__init__(self, nome, fone, endereco, cpf,
                   salarioBruto, descontos, bonificacoes)

    def paraFuturo(self):
        print(f"Nome:{self._nome}, Telefone:{self._fone}, Endereço:{self._endereco}, CPF:{self._cpf}, Salário Bruto:{self._salarioBruto}")
