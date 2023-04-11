#
from secretariaexecutiva import SecretariaExecutiva as SE
from funcionario import Funcionario as F
from gerente import Gerente as G

se1 = SE("José", 23456789, "Rua Amelino", 12367589900, 1000, 30, 70)
f1 = F("Antonio", 39006678, "Rua Esmeralda", 12309876544, 1500, 60, 120)
g1 = G("Lucas", 12345678, "Rua Santos", 12346589037, 1600, 50, 150, 20)

print("Secretaria Executiva")
print(se1.nome, se1.fone, se1.endereco, se1.cpf, se1.salarioBruto, se1.descontos, se1.bonificacoes)
se1.paraFuturo()
print()
print("Funcionario")
print(f1.nome, f1.fone, f1.endereco, f1.cpf, f1.salarioBruto, f1.descontos, f1.bonificacoes)
f1.calculaSalarioLiquido()
print()
print("Gerente")
print(g1.nome, g1.fone, g1.endereco, g1.cpf, g1.salarioBruto, g1.descontos, g1.bonificacoes)
g1.calculaComissao()