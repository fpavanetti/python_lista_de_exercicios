''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento'''

s = float(input("Qual é o seu salário? R$"))
a = s + (s * 0.15)
print("=" * 30)
print("PARABÉNS! \nVOCÊ RECEBEU UM AUMENTO!")
print("Seu novo salário é de R${:.2f}.".format(a))
print("Seu aumento foi de 15%, ou R${:.2f}.".format(s * 0.15))
print("=" * 30)
