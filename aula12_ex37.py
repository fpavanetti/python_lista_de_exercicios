'''
DESAFIO 37 - APROVANDO EMPRÉSTIMO

Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar:
- o valor da casa
- o salário do comprador
- e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela
não pode exceder 30% do salário ou então o empréstimo
será negado.

'''
from time import sleep
print("Bem-vindo/a ao programa de empréstimo bancário\n"
      "para interessados em adquirir seu imóvel próprio!\n"
      "Realizaremos algumas perguntas para informar se\n"
      "você está apto a receber o empréstimo.\n"
      "Vamos lá?")

# PRIMEIRO PASSO: ESTABELECER AS VARIÁVEIS SOLICITADAS

valor = float(input("Qual é o valor do imóvel? R$"))
salario = float(input("Qual é o valor do seu salário? R$"))
tempo = int(input("Em quantos anos você pretende realizar o pagamento do imóvel? "))

# SEGUNDO PASSO: calcular o valor da prestação mensal

prestação = valor / (tempo * 12)
print()
print("Processando pedido...")
sleep(2)
print("Valor da prestação: {}R${:.2f}{}".format('\033[4;33m', prestação, '\033[m'))
if prestação > salario * 0.30:
    print("\033[4;31mEMPRÉSTIMO NEGADO\033[m\n"
          "O valor da prestação excede 30% da sua renda.\n"
          "Sentimos muito.")
elif prestação <= salario * 0.30:
    print("\033[4;36mEMPRÉSTIMO APROVADO!\033[m")
print()
print("Agradecemos a preferência.")
