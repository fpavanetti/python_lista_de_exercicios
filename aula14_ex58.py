'''

Desafio 58 - Validação de dados

Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''

s = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while s not in "MF": #enquanto não houver a variável s em "MF", o programa não continuará.
    print("Dados inválidos.")
    s = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(s))





