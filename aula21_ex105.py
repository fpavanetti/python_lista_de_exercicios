'''

Desafio 105

Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python. Só que fazendo a validação para aceitar
apenas um valor numérico.

Ex:
n = leiaInt('Digite um número: ')

'''


def leiaInt(msg):
    """
    Função leiaInt para ler apenas números inteiros.
    :param msg: recebe o texto em que será informado o número a ser verificado.
    :return: valor (se msg receber um número, valor receberá este número e será o valor retornado para n)
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')