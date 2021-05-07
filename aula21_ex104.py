'''

Desafio 104

Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
dado não tenha sido informado corretamente.

'''


def ficha(nome='', gols=''):
    print('-' * 30)
    if nome == '' and gols == '':
        return print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
    elif nome == '' and gols != '':
        return print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    elif nome != '' and gols == '':
        return print(f'O jogador {nome} fez 0 gol(s) no campeonato.')
    else:
        return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de Gols: ')).strip()
ficha(n, g)
