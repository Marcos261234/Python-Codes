'''import random, time

valores = [0, 1, 2, 3, 4, 5]
advinho = int(input('Tente adivinhar qual número estou pensando entre 0-5, Vamos lá: '))

numero_pensado = random.choice(valores)
print('Processando...')
time.sleep(3)

if advinho == numero_pensado:
    print(f'Você acertou! Eu pensei no número: {numero_pensado}')
else:
    print(f'Você errou! Eu pensei no número: {numero_pensado}')
    
velocidade_carro = float(input('Quantos km/h o carro estava percorrendo? '))
multa = (velocidade_carro - 80) * 7
if velocidade_carro > 80:
    print(f'Você foi multado! E a multa é de {multa}R$')
else:
    print('Você não foi multado.')
    
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('PAR')
else:
    print('IMPAR')
    
    
distancia = float(input("Qual é a distância da sua viagem em km? "))

if distancia <= 200:
    preco = distancia * 0,50
else:
    preco = distancia * 0,45

print(f"O preço da sua passagem será: R$ {preco:.2f}")

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
import random

numeros = []

for i in range(3):
    num = int(input('Digite um número: '))
    numeros.append(num)
    
maior = max(numeros)

menor = min(numeros)

print('Maior número: {}  Menor número: {}.'.format(maior, menor))'''

salario = float(input('Digite seu salário para calcularmos alguns ajustes: '))

if salario > 1250:
    aumento = salario * 10 / 100
    print('Salário ajustado para: {}' .format(salario + aumento))
elif salario <= 1250:
    aumento = salario * 15 / 100
    print('Salário ajustado para: {}' .format(salario + aumento))