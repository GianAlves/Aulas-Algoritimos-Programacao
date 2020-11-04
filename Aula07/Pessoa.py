from Cidade import Cidade


class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        self.idade = 18
        self.cidade = None

    def imprimirDados(self):
        print("Nome: " + self.nome)
        print("Idade: " + str(self.idade))
        print("Cidade: " + str(self.cidade.id) + " - " + self.cidade.nome)

    def getMesesVividos(self):
        return (12 * self.idade)

    def getMesesVividos2(self, meses):
        return (12 * self.idade) + meses
