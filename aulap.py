import random 

alunos = []

while True:
    valor = (input('digite um nome: '))
    if valor=="0":
        break
    else:
        alunos.append(valor)

escolhido = random.choice(alunos)
print(alunos)
print(f'O aluno escolhido foi: {escolhido}')        
