'''

DESAFIO 81 - LISTA ORDENADA SEM REPETIÇÕES

Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar
o sort)

No final, mostre a lista ordenada na tela.
'''
l = list()
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0:
        l.append(n)
    elif n > l[-1]:
        l.append(n)
    else:
        j = 0
        while j < len(l):
            if n <= l[j]:
                l.insert(j, n)
                break
            j += 1
print(f"Lista formatada: {l}")
