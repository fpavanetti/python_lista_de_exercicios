'''

DESAFIO 87

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
'''
m = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        m[l].append(int(input(f"Digite o valor da posição {l}x{c}: ")))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^7}]', end='')
    print()


'''
Entendendo o código:
primeiro = declaração de lista com três listas dentro
segundo = for com variáveis genéricas representando as linhas e dentro dele as colunas
>>> as linhas primeiro porque primeiro preenchemos as linhas de cada coluna para depois
>>> preenchermos as linhas da próxima coluna e assim sucessivamente
é feito um input com append para matriz no índice da variável genérica do primeiro for, pois ela
começa em 0, passa pelo 0 1 2 da variável genérica do for abaixo e depois 1 e 2, preenchendo as
três listas dentro da lista principal

depois, para imprimir a matriz, outros dois for, com a mesma lógica. utilizamos um end='' no último
for para que os números fiquem posicionados corretamente e fora deste for mas dentro do primeiro,
damos um print() para o pulo de linha.
'''

