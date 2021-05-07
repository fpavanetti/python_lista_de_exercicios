'''

DESAFIO 71

Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) QUal é o NOME do produto mais barato.

'''
#PRIMEIRO PASSO: CRIAR AS VARIÁVEIS CONTADORAS OU DEFINIDAS PELO ENUNCIADO

t_g = float(0.00)
p_m = int(0)
p_b = float(0.00)
p_m_b = str('')

print("----- LOJA DE ELETRÔNICOS -----")
while True:
    pt = str(input("Nome do produto: ")) #ler o nome e o preço do produto
    pr = float(input("Valor do produto: R$"))
    if pr > 0.01 and p_b == 0: #o primeiro produto sempre será o mais barato e o mais caro
        p_b = pr
        p_m_b = pt
    elif pr < p_b:
        p_b = pr
        p_m_b = pt
    if pr > 1000:
        p_m = p_m + 1
    t_g = t_g + pr
    d = str(input("Deseja comprar mais produtos? [S/N] ")).strip().upper()
    while d not in "SsNn":
        d = str(input("Deseja comprar mais produtos? [S/N] ")).strip().upper()
    if d == "N":
        break
print()
print("COMPRAS ENCERRADAS")
print(f"VALOR TOTAL DAS COMPRAS: R${t_g:.2f}\n"
      f"PRODUTOS MAIS CAROS QUE R$1000: {p_m}\n"
      f"PRODUTO MAIS BARATO FOI {p_m_b}: R${p_b:.2f}")



