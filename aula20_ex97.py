'''

Desafio 97

Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular(largura e comprimento) e mostre a área do terreno.
'''


def area(a, b):
    square = a * b
    print(f'A área de um terreno {a}x{b} é de {square:.2f}m²')


l = float(input("Qual é a largura do terreno? "))
c = float(input("Qual é o comprimento do terreno? "))
area(l, c)
