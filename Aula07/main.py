from Pessoa import Pessoa
from Cidade import Cidade

city = Cidade(1, "POA")

p = Pessoa("Maria")
p.idade = 20
p.cidade = city
p.imprimirDados()


print("----------------")
capao = Cidade(None, None)
capao.id = 2
capao.nome = "Capao da Canoa"

p2 = Pessoa("Julia")
p2.idade = 30
p2.cidade = capao
p2.imprimirDados()

print("----------------")

print(p)
print("----------------")
print(p2)
