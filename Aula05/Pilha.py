from No import No

class Pilha:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        
    def adicionar( self, dado ):
        no = No( dado )
        if self.tamanho == 0:
            self.inicio = no
        else: 
            no.proximo = self.inicio
            self.inicio = no
            
        self.tamanho += 1
   

    def remover(self):
        if self.tamanho == 0:
            print("Pilha Vazia!")
        elif self.tamanho == 1:
            self.inicio = None
            self.tamanho -= 1
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def imprimir(self):
        if self.tamanho == 0:
            print("Pilha Vazia!")
        else:
            aux = self.inicio
            while( aux ):
                print( aux.dado )
                aux = aux.proximo 