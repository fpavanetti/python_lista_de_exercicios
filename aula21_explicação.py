'''

AULA 21 - FUNÇÕES PT. 2

Conteúdo:
> Interactive Help
> docstrings
> Argumentos opcionais
> Escopo de variáveis
> Retorno de resultados

Interactive Help - Ajuda interativa

help() < uma função interna do Python que retorna a documentação daquele
comando
help(input)
print(input.__doc__)

Docstrings < basicamente, uma string de documentação. Criamos para quando
nosso código é utilizado por outras pessoas, seja num processo interno ou
na criação de uma biblioteca.

Parâmetros Opcionais

São parâmetros criados para o caso de funções que não informem todos os
parâmetros "solicitados". Na declaração da função, atribuímos um valor
genérico ao parâmetro que será utilizado no caso de nada ser informado
para aquela opção. Pode ser utilizada para TODOS os parâmetros. Exemplo

def soma(a=0, b=0, c=0):
    ...

somar(8, 3)

Nesse caso, o C não foi informado, então a soma utilizará o valor genérico
atribuído a C (0).

ESCOPO DE VARIÁVEIS

Em programação, escopo é o local em que uma variável vai existir e o local
em que a variável não vai mais existir.

A importação de bibliotecas também acontece de forma global ou local.

Parâmetro real > aquele que passamos para a função
Parâmetro formal > aquele que é estabelecido no corpo da função

É possível utilizar funções globais dentro do Python

RETORNO DE VALORES

As funções em Python pode ou não retornar valores. Para isso, utilizamos
uma palavra reservada: return

'''

# criando uma docstring:
# :param: é parâmetro


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')


def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
    return s


def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# PROGRAMA PRINCIPAL
n = 2
print(f'No programa principal, n vale {n}')
# n é uma variável global, ou seja, cujo valor é válido para
# todo o escopo do programa. Já x é uma variável local, pois
# foi inserida dentro de uma função, cujo escopo também é LOCAL

contador(0, 100, 10)
somar(3, 2, 5)
somar(8, 4)
resp = somar(5, 4, 2)
print(somar(3, 2, 5))
print(f'Meus cálculos deram {resp}')
r1 = somar(2, 2, 4)
r2 = somar(4, 4, 6)
r3 = somar(6, 6, 8)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')


def função():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
função()
print(f'N1 fora vale {n1}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
if par(num):
    print('É par!')
else:
    print('Não é par!')