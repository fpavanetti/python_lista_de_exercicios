'''
Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira.

Ex.: Digite um número: 6.123
O número 6.123 tem a parte inteira 6
'''

import math

n = float(input("Digite um número real: "))
print("A parte inteira do número {} é: {}".format(n, math.trunc(n)))
print("A parte inteira do número é {} é: {}".format(n, int(n)))
