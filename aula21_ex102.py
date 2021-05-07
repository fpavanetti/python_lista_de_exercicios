'''

Desafio 102

Crie um programa que tenha uma função chamada voto(), que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓ-
RIO nas eleições.

'''


def vota(nascimento):
    import datetime
    i = datetime.date.today().year - nascimento
    if 18 > i >= 16:
        return print(f"Com {i} anos: VOTO OPCIONAL.")
    elif 18 <= i < 65:
        return print(f'Com {i} anos: VOTO OBRIGATÓRIO.')
    elif i >= 65:
        return print(f'Com {i} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {i} anos: VOTO NEGADO.')


n = int(input('Em que ano você nasceu? '))
vota(n)
