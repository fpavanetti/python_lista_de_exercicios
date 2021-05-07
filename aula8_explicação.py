'''

AULA 8: MÓDULOS EM PYTHON

Bibliotecas: são importáveis que adicionam funcionalidades
Sintaxe: import [...] (no início do programa)
from [...] import [...] (para quando precisamos de algo específico)

Biblioteca math: importa funcionalidades relacionadas à matemática.
ceil (arredondamento para cima)
floor (arredondamento para baixo)
trunc (trunca o número)
pow
sqrt (raíz quadrada)
factorial (fatorial)

from math import sqrt (para importar apenas uma funcionalidade)

'''
'''from math import sqrt, floor'''
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz do número {} é {:.2f}".format(num, math.floor(raiz)))

import random
num = random.random()
print(num)
num1 = random.randint(1, 10)
print(num1)
''' comando para ver as bibliotecas import ctrl + espaço
built-in
frameworks
PyPi Python Package Index - pacotes extras'''

import emoji
print(emoji.emojize("Olá, Mundo Triste... :cry:", use_aliases=True))











