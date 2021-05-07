'''
Desenvolva um programa que pergunte a distância
de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por
Km para viagens de até 200Km e R$0,45 para via-
gens mais longas.

'''

#PRIMEIRO: PERGUNTAR A DISTÂNCIA DA VIAGEM

d = float(input("Informe a distância da viagem que você fará em Kms: "))

#SEGUNDO: CALCULAR O PREÇO COM BASE NAS CONDIÇÕES

if d >= 200:
    print("O preço cobrado por viagens de 200 ou mais Kms é de R$0,45 \n"
          "por Km.")
    p1 = d * 0.45
    print("VALOR DA VIAGEM: R${:.2f}".format(p1))
else:
    print("O preço cobrado por viagens de menos de 200km de distância\n"
          "é de R$0,50 por Km.")
    p2 = d * 0.50
    print("VALOR DA VIAGEM: R${:.2f}".format(p2))
print("DISTÂNCIA: {:.0f}km".format(d))
