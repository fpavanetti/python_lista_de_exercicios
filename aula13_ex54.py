'''

DESAFIO 54 - DETECTOR DE PALÍNDROMOS

Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando
os espaços.
'''

f = str(input("Digite uma frase qualquer, sem ponto final: ")).strip().upper().replace(" ", "")

if f == f[::-1]:
    print(f[::-1])
    print("É palíndromo")
else:
    print("Não é palíndromo")

'''
Solução Guanabara

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = junto + letra
if inverso == junto:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo")

'''