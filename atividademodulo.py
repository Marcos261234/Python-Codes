'''import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))'''

'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))'''

'''from math import sin, tan, radians, cos

ang = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cosseno))
tang = tan(radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}: '.format(ang, tang))'''

'''import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''

'''import random

n1 = str(input('Primeiro jogador: '))
n2 = str(input('Segundo jogador: '))
n3 = str(input('Terceiro jogador: '))
n4 = str(input('Quarto jogador: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('O Top 4 é respectivamente: ')
print(lista)'''

