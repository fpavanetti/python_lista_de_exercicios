'''

Desafio 107

Faça um minisistema que utilize o Interactive Help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM', o programa se encerrará.

OBS.: use cores.
'''
from time import sleep


def titulo():
    chave = 'SISTEMA DE AJUDA PyHELP'
    linha = len(chave) + 4
    print('\033[1;30;42m~' * linha)
    print(f'  {chave}')
    print('~' * linha)


def pyhelp(função):
    sleep(0.5)
    manual = print(f'\33[1;30;44mACESSANDO O MANUAL DA FUNÇÃO \'{função}\'')
    sleep(1)
    print('\033[1;37;40m\n')
    help(função)


def texto(msg):
    l = len(msg) + 4
    print('\033[1;30;41m~' * len(msg))
    print(f'{msg}')
    print('~' * len(msg))


while True:
    titulo()
    n = input('\033[mFunção ou biblioteca > ').lower()
    if 'fim' in n:
        sleep(1)
        texto('Encerrando...'
              ' Até mais!')
        sleep(1)
        break
    pyhelp(n)
