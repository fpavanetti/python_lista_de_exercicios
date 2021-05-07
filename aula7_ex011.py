''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar. Considere US$1,00 = R$3,27 '''

print("=" * 30)
r = float(input("Para este cálculo, consideraremos o valor do dólar em US$3.27. \nQuantos reais você tem? R$"))
d = 3.27
c = r / d
print("Você pode comprar US${:.2f} dólares.".format(c))
print("=" * 30)