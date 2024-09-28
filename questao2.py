import random 

numeros = []

while True:
    valor = int(input('digite um número: '))
    if valor==0:
        break
    else:
        numeros.append(valor)

print(f'A soma dos números digitados é: {sum(numeros)}')        
