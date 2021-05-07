'''
DESAFIO 45 - GERENCIADOR DE PAGAMENTOS

Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e
condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

# PRIMEIRO: INSERIR O PREÇO NORMAL DO PRODUTO E A FORMA DE PAGAMENTO

p = float(input("Informe o valor do produto: R$"))
print("Formas de pagamento: \n"
                   "[1] À vista no dinheiro/cheque\n"
                   "[2] À vista no cartão\n"
                   "[3] Em até 2x no cartão \n"
                   "[4] 3x ou mais no cartão")
f_p = int(input("Informe a forma de pagamento: "))

# SEGUNDO: ESTRUTURA CONDICIONAL COM CÁLCULO DOS NOVOS VALORES

if f_p == 1:
    p_f = p - (p * 0.10)
    print("Nesta condição de pagamento, o produto tem 10% de desconto\n"
          "e seu preço final será de R${:.2f}.".format(p_f))
elif f_p == 2:
    p_f = p - (p * 0.05)
    print("Nesta condição de pagamento, o produto tem 5% de desconto\n"
          "e seu preço final será de R${:.2f}.".format(p_f))
elif f_p == 3:
    print("Nesta condição de pagamento, o produto não sofre alteração\n"
          "de preço e seu preço final continua sendo R${:.2f}.".format(p))
elif f_p == 4:
    p_f = p + (p * 0.20)
    np = int(input("Quantas parcelas serão? "))
    par = p_f / np
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(np, par))
    print("Nesta condição de pagamento, o produto tem 20% de juros\n"
          "sobre seu preço normal e custará R${:.2f}.".format(p_f))
else:
    print("\033[1;31mINFORME UMA OPÇÃO DE PAGAMENTO VÁLIDA.\033[m")
