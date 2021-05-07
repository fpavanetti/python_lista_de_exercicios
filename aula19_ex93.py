'''

DESAFIO 93

Crie um programa que leia
NOME
ANO DE NASCIMENTO
CARTEIRA DE TRABALHO
e cadastre-os (com IDADE) em um dicionário. Se por acaso
a CTPS for diferente de ZERO, o dicionário receberá também
o ano de contratação e o salário. Calcule e acrescente, além
da idade, com quantos anos a pessoa vai se aposentar.

PARA SE APOSENTAR: 35 ANOS DE CONTRIBUIÇÃO
'''
import datetime
d = dict()
d['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
d['Idade'] = datetime.date.today().year - nasc
d['CTPS'] = int(input('Número da CTPS [0 se não houver]: '))
if d['CTPS'] != 0:
    d['Ano de contratação'] = int(input('Ano de contratação: '))
    d['Salário'] = float(input('Salário: '))
    d['Idade para se aposentar'] = (d['Ano de contratação'] + 35) - nasc
    print(f'\t--- DADOS DO CONTRIBUINTE ---')
    for k, v in d.items():
        print(f'{k}: {v}')
else:
    del d['CTPS']
    for k, v in d.items():
        print(f'{k}: {v}')
    print('O contribuinte ainda não possui previsão para se aposentar.')