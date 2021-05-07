'''

DESAFIO 56 - MAIOR E MENOR DA SEQUÊNCIA

Faça um programa que leia o peso de cinco
pessoas. No final, mostre qual foi o maior
e o menor peso lidos.

'''
ma_p = float(0)
me_p = float(500)

for c in range(1, 6):
    p = float(input("Digite o peso da {}ª pessoa (Kg): ".format(c)))
    if p > ma_p:
        ma_p = p
    if p < me_p:
        me_p = p
print("Maior peso lido: {}kg".format(ma_p))
print("Menor peso lido: {}kg".format(me_p))

'''
Solução Guanabara
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(p)))
    if p == 1: // o primeiro termo SEMPRE será o maior e o menor
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

'''