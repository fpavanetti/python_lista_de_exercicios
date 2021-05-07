'''

DESAFIO 51 - SOMA DOS PARES

Desenvolva um programa que leia seis números
inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar,
desconsidere-o.

'''
s = int(0)

for c in range(1, 7, 1):
    n = int(input("Digite o {}º valor: ".format(c)))
    if n % 2 == 0:
        s = s + n
        print("{} é par".format(n))
print("A soma dos números pares informados é {}".format(s))
