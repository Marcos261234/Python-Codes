def somar(valor):
    soma = sum(numeros)
    print(f'A soma dos números é: {soma}')

numeros = []
for i in range (2):
    valor = int(input(f'Digite o Valor {i+1}: '))
    numeros.append(valor)
    
somar(valor)
    
