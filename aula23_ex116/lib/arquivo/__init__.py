from aula23_ex116.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #readtext
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #write text plus (criar)
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        #print(a.read())
        for line in a:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arc, name='desconhecido', age=0):
    try:
        a = open(arc, 'at') #abre o arquivo e append
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('Houve um erro na inserção dos dados')
        else:
            print(f'Novo registro de {name} adicionado.')
            a.close()