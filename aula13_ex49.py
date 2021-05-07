'''

DESAFIO 49 - Soma ímpares múltiplos de 3

Faça um programa que calcule a soma entre
todos os números ímpares que são múltiplos
de 3 e que se encontram no intervalo de 1
até 500.

'''
s = int(0)

for c in range(1, 501, 2): #pois só quero a soma dos ÍMPARES
    if c % 3 == 0:
        print(c)
        s = s + c
print("A soma de todos os números múltiplos de 3 é igual a {}".format(s))

'''
Solução Guanabara

- Economizar memória do PC

for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
print(s)
'''
