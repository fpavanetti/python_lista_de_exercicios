'''
Crie um programa que leia um número inteiro qualquer
e mostre na tela se ele é PAR ou ÍMPAR.

'''

# PRIMEIRO: LER O NÚMERO

n = int(input("Digite um número inteiro qualquer: "))

# SEGUNDO: CRIAR A CONDIÇÃO PARA IDENTIFICAR SE ELE É PAR OU ÍMPAR
if (n % 2 == 0):
    print("O número {} é PAR.".format(n))
else:
    print("O número {} é ÍMPAR.".format(n))
