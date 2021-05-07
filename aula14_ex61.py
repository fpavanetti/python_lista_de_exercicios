'''

DESAFIO 61

Faça um programa que leia um número qualquer
e mostre seu fatorial.

Ex: 5! = 5.4.3.2.1 = 120
'''

n = int(input("Digite o número cujo fatorial deseja saber: "))
f = int(1)
c = n

while c > 0:
    f = f * c #se utilizasse o numero para fazer o cálculo, a cada interação o valor do fatorial diminuiria. 5 * 5 = 25 / 5 * 4 = 20...
    c = c - 1
    print(f, end= ' ')
print()
print("O fatorial de {}! é {}".format(n, f))

#Primeiro: ler um número
n = int(input("Digite o número cujo fatorial deseja saber: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end='')
while c > 0:
    print("{} x".format(c), end ='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print("{}".format(f))
