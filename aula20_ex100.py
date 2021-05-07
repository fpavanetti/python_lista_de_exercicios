'''

Desafio 100

Faça um programa que tenha uma função maior(), que receba
vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles
é o maior.
'''


def maior(* num):
    print('-' * 50)
    if len(num) > 0:
        print(f'{num}. Foram informados {len(num)} números.')
        print(f'O maior número é {max(num)}.')
    else:
        print("Nenhum número foi informado.")


maior(5, 7, 9, 3, 2, 8, 12, 5, -1, -18)
maior(-18, -25, -12, -15, -14, -13)
maior()
