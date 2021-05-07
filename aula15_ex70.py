'''

DESAFIO 70

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadas-
trada, o programa deverá perguntar se o usuário quer continuar ou não. No final,
mostre:
A) Quantas pessoas tem mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos.

'''

#PRIMEIRO: CRIAR VARIÁVEIS CONTADORAS

maiores = homens = mulheres = 0

while True:
    print("-" * 15)
    print("CADASTRO DE PESSOAS")
    print("-" * 15)
    print()
    i = int(input("Qual é a idade da pessoa? "))
    s = str(input("Qual é o sexo da pessoa? [F/M] ")).strip().upper()[0]
    if s not in "FfMm":
        print("Digite um sexo válido.")
    else:
        if i > 18:
            maiores = maiores + 1
        if s == "M":
            homens = homens + 1
        if s == "F":
            if i < 20:
                mulheres = mulheres + 1
    print()
    r = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    while r not in "SsNn":
        r = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if r == "N":
        break
print()
print(f"Número de pessoas maiores de 18 anos: {maiores}")
print(f"Número de homens informados: {homens}")
print(f"Número de mulheres com menos de 20 anos informados: {mulheres}")