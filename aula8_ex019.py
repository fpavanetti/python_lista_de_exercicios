'''
Faça um programa que leia um número qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.

sen x = co/h
cos x = ca/h
tgt x = co/ca
'''
import math
n = float(input("Digite um ângulo qualquer: "))
print("O seno de {} é {:.2f}".format(n, math.sin(math.radians(n))))
print("O cosseno de {} é {:.2f}.".format(n, math.cos(math.radians(n))))
print("A tangente de {} é {:.2f}.".format(n, math.tan(math.radians(n))))


