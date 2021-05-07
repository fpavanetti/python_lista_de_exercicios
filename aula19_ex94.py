'''

Desafio 94

Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL.
O programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou. Depois,
vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso
será guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS feitos durante
o campeonato.
'''
jogador = dict()
l = list()
jogador['Nome'] = str(input("Nome do jogador: "))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, jogador['Partidas']):
    l.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {c+1}? ')))
jogador['Gols'] = l
jogador['Total'] = sum(l)
print('=' * 50)
print(jogador)
print('=' * 50)
for k, v in jogador.items():
    print(f'\tO campo {k} tem o valor {v}')
print('=' * 50)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for p, g in enumerate(l):
    print(f'\t=> Na partida {p+1} ele fez {g} gols.')
print(f'Sendo um total de {jogador["Total"]} gols.')