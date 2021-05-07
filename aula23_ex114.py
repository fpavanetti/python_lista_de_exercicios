'''

DESAFIO 114

Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação de um número de tipo inválido. Aproveite e crie
também uma função leiaFloat() com a mesma funcionalidade.
'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO. Digite um número inteiro.\033[m')
            continue
        else:
            break
    return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(TypeError, ValueError):
            print(f'\033[1;31mERRO. Digite um número real.\033[m')
            continue
        else:
            break
    return n


num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {num1}')
print(f'Você digitou {num2}')
