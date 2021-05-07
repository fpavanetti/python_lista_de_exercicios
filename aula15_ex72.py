'''

DESAFIO 72

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues.

OBS. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''

# PRIMEIRO: CRIAR O LOGO DA INTERAÇÃO COM USUÁRIO
print("=" * 15)
print("{:^15}".format("BANCO FAGNER"))
print("=" * 15)

#SEGUNDO: PEDIR INFORMAÇÕES AO USUÁRIO

n1 = int(50)
n2 = int(20)
n3 = int(10)
n4 = int(1)
s1 = int(0)
s2 = int(0)
s3 = int(0)
s4 = int(0)
valor = int(input("Valor a ser sacado: R$"))
while True:
    while valor >= n1:
        valor = valor - n1
        s1 = s1 + 1
    while valor >= n2:
        valor = valor - n2
        s2 = s2 + 1
    while valor >= n3:
        valor = valor - n3
        s3 = s3 + 1
    while valor >= n4:
        valor = valor - n4
        s4 = s4 + 1
    if valor == 0:
        break

print(f"Total de células de R${n1}: {s1}\n"
      f"Total de células de R${n2}: {s2}\n"
      f"Total de células de R${n3}: {s3}\n"
      f"Total de células de R${n4}: {s4}")
print("=" * 15)
print()
print("Obrigado por usar o BANCO FAGNER. Volte sempre!")

'''
SOLUÇÃO GUANABARA
valor = int(input("Que valor você quer sacar? R$"))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if tótced > 0:
            print(f"Total de {tótced} celulas de R${céd}")
        if céd == 50:
            céd = 20:
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break


'''