'''

Desafio 106

Faça um programa que tenha uma função chamada notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.

'''


def notas(* valores, situação=False):
    """
    nota(*valores, situação=False)
    -> Função para analisar notas e situação de vários alunos e reservar os dados obtidos num dicionário.
    :param valores: notas dos alunos
    :param situação: valor lógico opcional, que mostra a situação da turma (boa, ruim, razoável)
    :return:
    """
    print(valores)
    i = 0
    mai = men = s = 0
    for c in valores:
        s += c
        if i == 0:
            mai = c
            men = c
        else:
            if c > mai:
                mai = c
            if c < men:
                men = c
        i = i + 1
    m = s / i
    d = {'Total': i, 'Maior nota': mai, 'Menor Nota': men, 'Média da turma': m}
    if situação:
        if m >= 7:
            d['Situação'] = 'Boa'
        elif 7 > m >= 6:
            d['Situação'] = 'Razoável'
        else:
            d['Situação'] = 'Ruim'
        return d
    else:
        return d


resp = notas(7.5, 8.0, 9.0, 10, 2.0, 7, 4, 7, 8.5, 3, situação=True)
print(resp)