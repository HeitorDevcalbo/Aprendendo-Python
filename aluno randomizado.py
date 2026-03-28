from random import choice
n1 = str(input('Digite o nome do aluno1:'))
n2 = str(input('Digite o nome do aluno2:'))
n3 = str(input('Digite o nome do aluno3:'))
n4  = str(input('Digite o nome do aluno4:'))

lista = [n1,n2,n3,n4]

escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')