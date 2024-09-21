import random

x=[12,13,45,33,66]

x.append(88)
x.insert(3,27)
x.pop(3)
x.remove(13)
print(x)
#append() - insere na ultima posição
#insert() - insere na posição desejada
#pop() - Deleta uma posição
#remove() - Deleta um valor
#sum() - soma todos os valores do vetor
#max() - procura o maior valor do vetor
#min() - procura maior valor do vetor
#chioce - escolhe um valor aleatorio
#sort - ordena o vetor (ordem crescente)
#set - elimina elementos repetidos
x.sort()
print(x)
x.sort(reverse=True)
print(x)