'''

DESAFIO 83 - DIVIDINDO VALORES EM VÁRIAS LISTAS

Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input("Digite um número inteiro: "))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    r = str(input("Deseja continuar? [S/N]: "))
    while r not in 'sSnN':
        r = str(input("Deseja continuar? [S/N]: "))
    if r in 'nN':
        break
print("-" * 30)
print(f'Lista completa: {lista}')
print(f'Lista par: {lista_par}')
print(f'Lista ímpar: {lista_impar}')

'''
Solução Guanabara
num = list()
pares = lista()
impares = lista()
while True:
    num.append(int(input("Digite um número: ")))
    resp = str(input("Quer continuar? [S/N]: "))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
'''