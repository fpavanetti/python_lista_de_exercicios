'''
Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
'''

import random

a1 = "Pedro"
a2 = "Ana"
a3 = "Maria"
a4 = "Fernando"
alunos = [a1, a2, a3, a4]
print("O professor sorteará um aluno para limpar o quadro.")
print("O aluno selecionado será...")
print(random.choice(alunos))
''' É necessário criar uma lista para sortear strings. '''
''' O comando choice seleciona um item de uma lista '''

