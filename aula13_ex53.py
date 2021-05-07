'''

DESAFIO 53 - Números primos

Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.

'''

n = int(input("Digite um número inteiro (0 e 1 são inválidos!): "))
tot_div = int(0)

if n == 1 or n == 0:
    print("Números inválidos!")

for c in range(1, n+1):
    if n % c == 0:
        tot_div = tot_div + 1
if tot_div > 2:
    print("O número {} NÃO é PRIMO.".format(n))
else:
    print("O número {} É PRIMO.".format(n))


