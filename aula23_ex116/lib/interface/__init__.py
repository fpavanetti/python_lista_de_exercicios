def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO. Digite um número inteiro.\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;31mO usuário decidiu não informar nenhum dado.')
            continue
        else:
            break
    return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c = c + 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
