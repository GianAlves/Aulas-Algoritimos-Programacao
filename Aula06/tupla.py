carros = "Uno", "Doblo", "Toro", "Hylux", "Ferrari"
print(carros[1])

print("-------------")

for car in carros:
    print(car)

print("-------------")
texto = "Carro: " + str(carros[1:2])
print(texto)

print("-------------")

print(carros[1: 6])

print("------- Ordenado -----")

print(sorted(carros))
print(carros)
print("-------------For com range ")
for car in range(len(carros) - 2):
    print("Posição " + str(car) + ": " + carros[car])


def calcular(x, y):
    return (x+y), (x-y), (x*y), (x/y)

print("\n--------- Usando Função -----")
print(calcular(5, 2))


# Lembrando de vetores
vet = [1, 5, 20]
vet = [100, 50, 20, 60]
vet[1] = 10
vet.sort()
print(vet)
