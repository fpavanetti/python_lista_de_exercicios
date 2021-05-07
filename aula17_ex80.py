'''

DESAFIO 80 - VALORES ÚNICOS EM UMA LISTA

Crie um programa em que o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
será adicionado. No final, serão exibidos todos os valores únicos digi-
tados, em ordem crescente.

'''
lista = []
while True:
    n = int(input("Digite um valor: "))
    if n in lista:
        print("A lista já contém este valor.")
    else:
        lista.append(n)
    r = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    while r not in 'sSnN':
        r = str(input("RESPOSTA INVÁLIDA. Deseja continuar? [S/N]: "))
    if r == 'N':
        break
lista.sort()
print("=" *25)
print(f"Você digitou os valores {lista}")
