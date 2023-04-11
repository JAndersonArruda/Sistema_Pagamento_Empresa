from funcionario import Funcionario as F

class Gerente(F):
    def __init__(self, nome, fone, endereco, cpf, salarioBruto, descontos, bonificacoes, comisao):
        F.__init__(self, nome, fone, endereco, cpf, salarioBruto, descontos, bonificacoes)
        self.comisao = int(comisao)
        
    def calculaComissao(self):
        valor = int((self.salarioBruto / 100) * self.comisao)
        print(f"Comisão do Gerente: {valor}")
    
