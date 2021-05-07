'''

Desafio 103

Crie um programa que tenha uma função chamada fatorial() que receba dois
parâmetros: o primeiro, que indique o número a calcular, e o outro chamado
show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.

'''


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número, mostrando apenas o resultado ou o cálculo.
    :param n: número cujo fatorial será calculado
    :param show: valor lógico opcional para exibir cálculo (True para mostrar, False para não mostrar)
    :return: o valor do fatorial do número n
    """
    print('-' * 30)
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return f


print(fatorial(5, True))
help(fatorial)
