from aula23_ex116.lib.interface import *
from aula23_ex116.lib.arquivo import *
from time import sleep
#as importações assim garantem um código menos poluído

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Exibir Usuários Cadastrados', 'Cadastrar Novo Usuário', 'Sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Encerrando o sistema...')
        sleep(2)
        break
    else:
        print('\033[1;31mOpção inválida.\033[m')
    sleep(2)

s = 0
a = open(arq, 'rt')
for l in a:
    dado = l.split(';')
    if dado[1].isnumeric:
        i = int(dado[1])
        s = s + i
print(s)