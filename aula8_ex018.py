'''
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre
o comprimento da hipotenusa.


'''
import math
a = float(input("Digite o valor do cateto oposto: "))
b = float(input("Digite o valor do cateto adjacente: "))
c = (a ** 2) + (b ** 2)
h = c**(1/2)
'''
O valor do cálculo do teorema de Pitágoras é resolvido por meio da raiz da potência
dos catetos
'''
print("O valor da hipotenusa é {:.2f}.".format(h))
hi = math.hypot(a, b)
print("A hipotenusa vai medir {:.2f}".format(hi))
