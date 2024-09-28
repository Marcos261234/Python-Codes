import random

numeros = []

for i in range(10):
    valor = int(input('Digite um número: '))
    numeros.append(valor)

print(numeros)
print(max(numeros))
print(sum(numeros))