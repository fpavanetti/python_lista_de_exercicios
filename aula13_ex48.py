'''

DESAFIO 48 - Contagem de pares

Crie um programa que mostre na tela
todos os números pares que estão no
intervalo entre 1 e 50

'''

for c in range(1, 51, 1):
    if (c  % 2 == 0):
        if c != 50:
            print(c, end=", ")
        else:
            print(c, end=".")

'''
Solução Guanabara

for n in range(2, 51, 2):
    print(n, end= ' ')
print("Acabou")

Economizar espaço na memória RAM
'''