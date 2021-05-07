'''
DESAFIO 39 - COMPARANDO NÚMEROS

Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior,
os dois são iguais

'''

# PRIMEIRO: LER OS NÚMEROS

n1 = int(input("Digite o 1o número: "))
n2 = int(input("Digite o 2o número: "))

# ESTABELECER A ESTRUTURA DE DECISÃO

if n1 > n2:
    print("\033[1;33mO primeiro valor é o maior.\033[m")
elif n1 < n2:
    print("\033[1;33mO segundo valor é o maior.\033[m")
else:
    print("\033[1;31mNão existe valor maior.\033[m")
print()
print("Os valores informados foram, respectivamente, {} e {}.".format(n1, n2))
