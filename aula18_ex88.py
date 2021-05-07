'''

DESAFIO 88

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados

B) A soma dos valores da terceira coluna

C) O maior valor da segunda linha
'''
matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f"Digite um número para a posição {linha}x{coluna}: ")))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^7}]', end='')
    print()
print()
# A
s = 0
p = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            s = s + matriz[linha][coluna]
            p = p + 1
print(f'Foram encontrados {p} números pares. A soma entre eles foi igual a {s}.')
# B
stc = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma entre os valores da terceira coluna foi igual a {stc}.')
# C
m = 0
for linha in range(1, 2):
    for coluna in range(0, 3):
        if coluna == 0:
            m = matriz[linha][coluna]
        else:
            if matriz[linha][coluna] > m:
                m = matriz[linha][coluna]
print(f'O maior valor da segunda linha é {m}.')


'''
B
for l in range(0, 2)
    scol += matriz[l][2]
'''