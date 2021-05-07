'''

DESAFIO 55 - GRUPO DA MAIORIDADE

Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade
e quantas já são maiores.

CONSIDERE 21 ANOS

'''
import datetime
a = datetime.date.today().year
tot_menor = int(0)
tot_maior = int(0)

for c in range(1, 8):
    n = int(input("Digite o ano de nascimento da {}ª pessoa do grupo: ".format(c)))
    if a - n < 21:
        tot_menor = tot_menor + 1
    else:
        tot_maior = tot_maior + 1
print("O número de pessoas que são maiores de idade é {} e o de pessoas que são\n"
      "menores é {}.".format(tot_maior, tot_menor))
