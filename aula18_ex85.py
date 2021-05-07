'''

DESAFIO 85

Faça um programa que leia o nome e o peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradasa

B) Uma listagem com as pessoas mais pesadas

C) Uma listagem com as pessoas mais leves

'''
print("*" * 30)
print("{:^30}".format("LISTAGEM DE PESSOAS"))
g = list()
i = list()
maior = menor = 0
while True:
    i.append(str(input("Nome: ")))
    i.append(float(input("Peso: ")))
    if menor == 0:
        maior = menor = i[1]
    else:
        if i[1] > maior:
            maior = i[1]
        elif i[1] < menor:
            menor = i[1]
    g.append(i[:])
    i.clear() # a função clear limpará os valores já contidos em i, para não replicá-los nas próximas sub-listas
    r = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    while r not in 'sSnN':
        r = str(input('OPÇÃO INVÁLIDA. Deseja continuar? [S/N]: ')).upper().strip()
    if r == 'N':
        break
print(g)
print(f'Foram cadastradas {len(g)} pessoas.')
print(f'O maior peso registrado foi {maior}. Pessoas com este peso: ', end='')
for p in g:
    if p[1] == maior:
        print(f"[{p[0].format(' ')}]", end='')
print()
print(f'O menor peso registrado foi {menor}. Pessoas com este peso: ', end=' ')
for p in g:
    if p[1] == menor:
        print(f'[{p[0].format(" ")}]', end=' ')
