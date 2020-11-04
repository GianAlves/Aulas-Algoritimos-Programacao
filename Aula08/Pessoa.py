class Pessoa:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        print("Nome: " + self.nome)
        print("Endereco: " + self.endereco)

    @staticmethod
    def toPessoa(pessoa):
        p = Pessoa(pessoa.nome, pessoa.endereco)
        return p
