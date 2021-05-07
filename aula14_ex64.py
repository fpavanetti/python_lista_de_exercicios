'''

DESAFIO 64 -

Escreva um programa que leia um número n inteiro e
mostre na tela os n primeiros elementos de uma sequência
de fibonacci.

0 1 1 2 3 5 8
'''

n = int(input("Quantos elementos da Sequência de Fibonacci você deseja ver? "))
print()
print()
print("~" * 25)
print("\033[31m SEQUÊNCIA DE FIBONACCI \033[m")
t1 = 0
t2 = 1
c = 3
print(t1, t2, end=' ')
while c <= n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    c = c + 1
print("\n")
print("~" * 25)
