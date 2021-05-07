'''

DESAFIO 115

Crie um código em Python que teste se o site Pudim está acessível pelo computador
usado.

'''
import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'O site está indisponível no momento.')
else:
    print('Consegui acessar o site com sucesso!')
    print(site.read())
