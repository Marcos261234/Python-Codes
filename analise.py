'''ANALISE
len(frase)
frase.count('o')
frase.count('o', 0, 13)
frase.find('deo')
frase.find('Android')
'curso' in frase
TRANSFORMACAO
frase.replace('Python', 'Android')   trocar palavras
frase.upper()            letras maisculas
frase.lower()            letras minusculas
frase.capitalize()       tudo em minusculo menos a primeira letra
frase.title()            capitalize com todas as palavras
frase.rstrip()           remove espaco(vazio) da direita p esq
frase.lstrip()           remove espaco(vazio) da esquerda p dir
DIVISAO
frase.split()           cada palavra recebe outra lista(index)
JUNCAO
'-'.join(frase)

EXERCICIO 1

nome = str(input('Digite seu nome: '))
print(f'Nome: {nome}')

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
separa = nome.split()
print(separa[0], len(separa.count))

EXERCICIO 2

num = str(input('Digite um numero entre 0 a 9999 que mostraremos a unidade de medida separadamente: '))
print(f'unidade: {num[0]}')
print(f'dezena: {num[1]}')
print(f'centena: {num[2]}')
print(f'milhar: {num[3]}')

EXERCICIO 3

nome = str(input('Digite seu nome: '))
analise = nome.split()
print(analise[1])
if analise[1] == 'Silva':
    print('Tem "Silva" no nome.')
else:
    print('Não tem "Silva" no nome.')
    
EXERCICIO 4
    
frase = 'O rato roeu a roupa do rei de roma'
analise = frase.upper()
print(f'A letra A aparece {analise.count('A')} vezes')
print(f'Pela primeira vez a letra A aparece na posição {analise.find('A')+1}')
print(f'Pela ultima vez a letra A aparece na posição {analise.rfind('A')+1}')

nome = str(input('Digite seu nome completo: '))

nome_sep = nome.split()
print(nome_sep[0])
print(nome_sep[len(nome_sep)-1])'''
