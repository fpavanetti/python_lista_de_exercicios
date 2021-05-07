'''
Faça um programa que leia um ano qualquer e
MOSTRE SE ELE É BISSEXTO.
'''
import datetime
# PRIMEIRO: LER O ANO
print("Este programa determinará se um ano é bissexto.")
a = int(input("Digite um ano qualquer: "))

# SEGUNDO: FAZER A CONDIÇÃO COM CÁLCULO QUE DETERMINA SE O ANO É BISSEXTO)
if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
    print("{} é um ano bissexto.".format(a))
else:
    print("{} não é um ano bissexto.".format(a))
print()
ano = datetime.date.today().year
print("Por sinal, como você deve saber, estamos no ano de {}. =)".format(ano))
