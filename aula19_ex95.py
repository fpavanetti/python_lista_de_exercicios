'''

Desafio 95

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma
lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todos as mulheres
D) Uma lista com todas as pessoas com idade acima da média
'''
grupo = list()
pessoa = dict()
c = 0
t = 0
s = 0
mulheres = list()
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Nome: "))
    pessoa['Sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input("INFORMAÇÃO INVÁLIDA. Sexo [M/F]: ")).strip().upper()[0]
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    pessoa['Idade'] = int(input("Idade: "))
    s += pessoa['Idade']
    grupo.append(pessoa.copy())
    t += 1
    r = str(input("Deseja continuar? [S/N]: ")).upper()[0]
    while r not in 'SN':
        r = str(input("OPÇÃO INVÁLIDA. Deseja continuar? [S/N]: "))
    if r == 'N':
        break
print('=-' * 30)
print(f'\t=> No total, foram cadastradas {t} pessoas.')
m = s / t
print(f'\t=> A média de idade do grupo é de {m:.2f}')
print(f'\t=> As mulheres cadastradas foram: {mulheres}')
'''acima_da_media = list()
for p in grupo:
    if p['Idade'] > m:
        acima_da_media.append(p['Nome'])'''
print(f'\t=> As pessoas cuja idade está acima da média são:')
for p in grupo:
    if p['Idade'] >= m:
        for k, v in p.items():
            print(f'[{k} = {v}] ', end='')
        print()
print('<<< ENCERRADO >>>')