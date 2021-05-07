'''
O mesmo professor do desafio anterior quer sortear a
ordem de apresentação de trabalhos dos alunos. Faça um
programa que leia o nome dos quatro alunos e mostre a
ordem sorteada.
'''
import random
print("O professor realizará o sorteiro para determinar a ordem de")
print("apresentação dos alunos.")
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")
lista = [a1, a2, a3, a4]
print("=" * 30)
print()
print("A ordem dos alunos é... ")
random.shuffle(lista)
print(lista)
''' O comando shuffle embaralha os itens de uma lista '''