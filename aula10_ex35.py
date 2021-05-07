'''
Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00, calcule
um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.

'''

#PRIMEIRO: PERGUNTAR O SALÁRIO

s = float(input("Qual o valor do seu salário atual? R$"))

if s > 1250.00:
    ns = s + (s * 0.10)
    print("Você recebeu um aumento de 10% e seu salário agora é de R${:.2f}.".format(ns))
else:
    ns = s + (s * 0.15)
    print("Você recebeu um aumento de 15% e seu salário agora é de R${:.2f}".format(ns))
