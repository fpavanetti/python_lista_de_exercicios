'''

DESAFIO 92

Crie um programa onde 4 jogadores joguem um dado e tenham resultados
ALEATÓRIOS. Guarde esses resultados em um DICIONÁRIO. No final, colo-
que esse dicionário EM ORDEM, sabendo que o VENCEDOR tirou o MAIOR
NÚMERO no dado.
'''
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'O {k} tirou {v} em seu dado.')
ranking = dict()
print()
print('\t\t=== VENCEDORES ===')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, l in enumerate(ranking):
    print(f'\t{i+1}o Colocado: {l}')
print(ranking)
