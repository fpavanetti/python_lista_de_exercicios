'''

Aula 23 - Tratamento de erros e exceções

----- ERROS ACONTECEM: SEMPRE -----

Existem erros de diferentes tipos
> primt(x), por exemplo, é um erro de sintaxe
O programa estar escrito corretamente não quer dizer que ele está "certo"

print('Oi')
print(x) -> x não foi inicializado. Erro semânetico

Quando o erro não é de ordem sintático, não costumamos chamar de erro,
mas sim de EXCEÇÃO. No caso demonstrado acima, é uma exceção do tipo 'NameError'

n = int(input('Num') > No caso de não ser inserido um número inteiro, retornará

'ValueError' < isso é uma exceção

a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r})

'ZeroDivsionError': erro de divisão por zero

r = 2 / '2'

'TypeError'

lst = [3, 6, 4]
print(lst[3])

'IndexError' / em dicionários: 'KeyError'

import uteis

'ModuleNotFoundError'

'EOFError'

... Existem muitas exceções em Python

Toda exceção é filha de uma classe maior chamada de Exception

> para tratamento de erros e exceções: comandos try/except

try
    operação
except
    falhou


Verificar a conexão de um site com um Python:
import urllib
import urllibr.request

erros: urllib.error.URLError
site.read() < acessa o código HTML do site


ACESSO A ARQUIVOS

open(nome do arquivo, 'rt') #readtext
open(nome, 'wt+') #writetext +(paracriar)
open('at') append text
readlines
read
'''
try: # tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Infelizmente tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividr um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado {erro.__cause__}')
else: #deu certo (opcional)
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado.')

