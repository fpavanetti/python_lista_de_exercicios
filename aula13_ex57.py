'''

DESAFIO 57 - ANALISADOR COMPLETO

Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas. No
final do programa, mostre:

- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos

'''
tot_i = int(0) # total das idades
i_m_v = int(0) # idade do homem mais velho
h_m_v = str # homem mais velho
tot_m_m = int(0) #mulheres menores

for c in range(1, 5):
    n = str(input("Digite o nome da {}ª pessoa: ".format(c)))
    i = int(input("Digite a idade da {}ª pessoa: ".format(c)))
    s = str(input("Digite o sexo da {}ª pessoa [M] ou [F]: ".format(c))).upper().replace("[", "").replace("]", "")
    tot_i = tot_i + i
    if s == "M":
        if i > i_m_v:
            i_m_v = i
            h_m_v = n
    elif s == "F":
        if i < 20:
            tot_m_m = tot_m_m + 1
m_i = tot_i / 4
print("A média de idade do grupo é: {:.2f}".format(m_i))
print("O homem mais velho se chama {} e tem {} anos.".format(h_m_v, i_m_v))
print("{} mulher(es) têm menos de 20 anos.".format(tot_m_m))