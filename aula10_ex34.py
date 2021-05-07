'''
Faça um programa que leia 3 números e mostre:
- qual é o maior e
- qual é o menor

'''

# PRIMEIRO: INSERIR OS 3 NÚMEROS

n = float(input("Digite o 1o número: "))
n2 = float(input("Digite o 2o número: "))
n3 = float(input("Digite o 3o número: "))

# DETERMINAR QUAL É O MAIOR DENTRO DE UMA CONDIÇÃO
print()
if n > n2 and n > n3:
    print("{} é o maior número.".format(n))
elif n2 > n and n2 > n3:
    print("{} é o maior número".format(n2))
else:
    print("{} é o maior número.".format(n3))
# DETERMINAR QUAL É O MENOR DENTRO DE UMA CONDIÇÃO
print()
if n < n2 and n < n3:
    print("{} é o menor número.".format(n))
elif n2 < n and n2 < n3:
    print("{} é o menor número.".format(n2))
else:
    print("{} é o menor número.".format(n3))
print()
print()
print("Os números informados foram, respectivamente: {}, {}, {}.".format(n, n2, n3))
