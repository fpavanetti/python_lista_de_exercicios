'''
DESAFIO 40 - ALISTAMENTO MILITAR

Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta
ou que passou do prazo para o alistamento.

Utilizar o módulo que usa o ano do sistema
'''

# PRIMEIRO: IMPORTAR O MÓDULO PARA OBTER O ANO ATUAL DO SISTEMA

import datetime

# SEGUNDO: LER O ANO DE NASCIMENTO, O ANO ATUAL E O ANO DE ALISTAMENTO

nasc = int(input("Digite seu ano de nascimento: "))
ano = datetime.date.today().year
idade = ano - nasc
alistamento = nasc + 18
tempo_restante = alistamento - ano
tempo_excedente = ano - alistamento

# TERCEIRO: CRIAR A ESTRUTURA DE CONDIÇÃO

if idade < 18:
    print("Você ainda se alistará no serviço militar.\n"
          "Ano em que você deverá se alistar: \033[1;36m{}\033[m\n"
          "Faltam {} anos.".format(alistamento, tempo_restante))
elif idade > 18:
    print("\033[1;31mVocê já deveria ter se alistado no serviço militar.\033[m\n"
          "Ano em que você deveria ter se alistado: {}\n"
          "Tempo excedente: {} anos".format(alistamento, tempo_excedente))
else:
    print("\033[1;36mVocê tem 18 anos e é hora de se alistar.\033[m")

