'''
DESAFIO 42 - CLASSIFICANDO ATLETAS

A Confederação Nacional de Natação precisa
de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo
com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''
import datetime

# PRIMEIRO: LER O ANO DE NASCIMENTO, O ANO ATUAL E DETERMINAR A IDADE
nasc = int(input("Em que ano você nasceu? "))
ano = datetime.date.today().year
idade = ano - nasc
print("O atleta tem {} anos de idade.".format(idade))

# SEGUNDO: CRIAR A ESTRUTURA DE CONDIÇÃO COMPOSTA

if idade <= 9:
    print("Categoria: Mirim")
elif idade <= 14:
    print("Categoria: Infantil")
elif idade <= 19:
    print("Categoria: Junior")
elif idade == 20:
    print("Categoria: Sênior")
else:
    print("Categoria: Master")