def calcular_area( largura, comprimento ):
    area = float(largura) * float(comprimento)
    return area

altura = 5
volume = altura * calcular_area( 4, 6)
print ( volume )

def calcular_volume( largura, comprimento, altura ):
    volume = float(largura) * float(comprimento) * float(altura)
    return volume

def calcular_volume2( largura, comprimento, altura ):
    volume = calcular_area( largura, comprimento) * float( altura )
    return volume

# Codigo da colega...
def calcular_volume3( altura, area):
    volume = altura * area
    return volume

print( calcular_volume3(5, calcular_area(2,4)))
# Codigo da colega...

def abrirPorta( portas ):
    if portas > 0:
        print(portas)
        portas = portas -1
        abrirPorta( portas )

abrirPorta( 3 )

carros = ["Doblo", "Novo Uno", "Sandero"]
print(carros)

print(carros[1])

def calcular_volume4(altura):
    volume = altura * calcular_area(4, 6)
    return volume