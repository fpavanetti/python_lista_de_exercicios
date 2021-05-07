def aumentar(preço, porcentagem, formata=False):
    preço = preço + (preço * porcentagem / 100)
    if formata:
        return f'R${preço:.2f}'.replace('.', ',')
    else:
        return preço


def diminuir(preço, porcentagem, formata=False):
    preço = preço - (preço * porcentagem / 100)
    if formata:
        return f'R${preço:.2f}'.replace('.', ',')
    else:
        return preço


def dobro(preço, formata=False):
    dobro = preço + preço
    if formata:
        return f'R${dobro:.2f}'.replace('.', ',')
    else:
        return dobro


def metade(preço, formata=False):
    metade = preço - (preço / 2)
    if formata:
        return f'R${metade:.2f}'.replace('.', ',')
    else:
        return metade


def moeda(preço):
    return f'R${preço:.2f}'.replace('.', ',')


def resumo(preço=0, aumento=0, diminui=0):
    print('-' * 30)
    print(f'{"RESUMO DOS VALORES":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}', f'R${preço:>.2f}'.replace('.', ','))
    print(f'{"Dobro do preço:":<20}', f'{dobro(preço, formata=True)}')
    print(f'{"Metade do preço:":<20}', f'{metade(preço, formata=True)}')
    print(f'{aumento}% {"de aumento:":<16}', f'{aumentar(preço, porcentagem=aumento, formata=True)}')
    print(f'{diminui}% {"de desconto:":<16}', f'{diminuir(preço, porcentagem=diminui, formata=True)}')

