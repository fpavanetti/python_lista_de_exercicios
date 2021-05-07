'''

DESAFIO 52 - PROGRESSÃO ARITMÉTICA

Desenvolva um programa que leia o primeiro termo
e a razão de uma PA; no final, mostre os 10 primeiros
termos dessa progressão.

'''

print("*" * 10, "\033[1;33mLeitor de Progressão Aritmética\033[m", "*" * 10)
p1 = int(input("Informe o 1º termo da PA: "))
r = int(input("Informe a razão da PA: "))

for c in range(1, 11):
    print(p1, end=' ')
    p1 = p1 + r #dessa forma funcionará pois o valor de p1 já vai modificado para o próximo laço

'''
Solução Guanabara não utiliza a soma do laço,
mas uma variável que calcula o enésimo termo
de uma PA.
'''