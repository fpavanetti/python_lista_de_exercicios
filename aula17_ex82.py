'''

DESAFIO 82 - EXTRAINDO DADOS DE UMA LISTA

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados. / len
B) A lista de valores, ordenada de forma decrescente. / sort(reverse=True)
C) Se o valor 5 foi digitado e está ou não na lista. / if
'''
lista = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    r = str(input("Deseja continuar? [S/N]: "))
    while r not in "SsNn":
        r = str(input("RESPOSTA INVÁLIDA. Deseja continuar? [S/N]: "))
    if r in 'Nn':
        break
print(f"Foram digitados {len(lista)} valores.")
lista.sort(reverse=True)
print(f'Valores ordenados de maneira descrescente: \n'
      f'{lista}')
if 5 in lista:
    print("O valor 5 foi digitado e está na lista.")
else:
    print("O valor 5 não foi informado.")