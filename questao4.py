import random

nomes = []

for i in range(5):
    valor = (input('Digite um nome: ')).title()
    nomes.append(valor)
    
print(nomes)
nomes.sort()
print(nomes)