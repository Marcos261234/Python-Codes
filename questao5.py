numeros = []

for i in range(10):
    valor = int(input('Digite um número: '))
    numeros.append(valor)
    
media = (sum(numeros)) / len(numeros)
print(f'A média é: {media:.2f}')