pessoa = {"nome": "Júlia", "idade": 11}
print(pessoa)

print(pessoa["nome"])

pessoa["altura"] = 1.3
print(pessoa)


pessoa["terminouTema"] = True
print(pessoa)

if pessoa["terminouTema"]:
    print("Parabéns")
else:
    print("Sem refrigerante")

del pessoa["idade"]
print(pessoa)

pessoa2 = {"nome": "Maria", "idade": 25, "altura": 1.75, "terminouTema": False}


listPessoas = pessoa, pessoa2

print(listPessoas)
