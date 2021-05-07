'''
DESAFIO 41 - AQUELE CLÁSSICO DA MÉDIA

Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO

'''

# PRIMEIRO: LER AS NOTAS E CALCULAR A MÉDIA

n1 = float(input("Informe a 1a nota: "))
n2 = float(input("Informe a 2a nota: "))
m = (n1 + n2) / 2
print("Sua média é {:.1f}".format(m))

# CLASSIFICAR A MÉDIA DENTRO DA ESTRUTURA DE CONDIÇÃO

if m < 5:
    print("\033[1;31m REPROVADO \033[m")
elif (m >= 5) and (m <= 6.9):
    print("\033[1;33m RECUPERAÇÃO \033[m")
else:
    print("\033[4;34m APROVADO! Parabéns e boas férias!\033[m")
