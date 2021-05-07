'''

DESAFIO 62

Refaça o desafio 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.

'''

p1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
c = 1

while c <= 10:
    print(p1, end=' ')
    p1 = p1 + r
    c = c + 1