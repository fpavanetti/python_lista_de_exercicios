'''

Aula 22 - Módulos e pacotes

Modularização - ato de construir módulos. Surgiu no início da década de 60. Os
sistemas estavam ficando cada vez maiores. O foco principal é dividir um programa
grande, aumentando a legibilidade. Dessa forma, é facilitada a manutenção do pro-
grama.

Para o Python, todo arquivo .py pode ser importável, desde que ele possua funções
internas. Durante o curso trabalhamos com diversos módulos: random, math, time,
datetime, etc. Porém, nada nos impede de criar nossos próprios módulos, sempre
que nossos programas necessitarem de um excessivo número de funções.

Quando realizamos diversas importações, não é recomendado que façamos a importação
de apenas algumas funções (como aconteceu durante o curso, mas por questões especí-
ficas), pois, caso dois módulos possuam funções com o mesmo nome, o Python, quando
tiver a função chamada, vai executar apenas a última importada.

VANTAGENS DA MODULARIZAÇÃO

- Organização do código
- Facilidade na manutenção
- Ocultação de código detalhado
- Reutilização em outros projetos

Quando os módulos não nos satisfazem mais, entra em questão os PACOTES.

O objetivo da modularização é tornar meu código mais fácil de se utilizar;
mas e quando um módulo acaba acumulando funções demais? Em outras linguagens
de programação, a solução era criar mais módulos. O Python oferece a criação
de PACOTES, que são pastas contendo módulos separados por assuntos.

Pacote uteis (exemplo)

módulo números (funções relacionadas a números)
módulo strings
módulo datas
módulo cores

import uteis (importa tudo)

from uteis import datas

Todo arquivo .py pode ser um módulo
Toda pasta é considerada um pacote

Dentro de cada pasta é necessário que haja um arquivo __init__.py

Um pacote pode conter outros pacotes

'''


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num = int(input('Digite um número'))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


import uteis

num = int(input('Digite um número: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')
