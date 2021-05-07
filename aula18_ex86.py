'''

DESAFIO 86

Crie um programa em que o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e
ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

'''
#primeira solução, criando três listas e unificando-as depois
l = list()
p = list()
i = list()
for c in range(1, 8):
    n = int(input(f"Digite o {c}º valor: "))
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
p.sort()
l.append(p[:])
i.sort()
l.append(i[:])
print(l)

#segunda solução, com apenas uma lista com duas listas dentro dela
u = [[], []]
for c in range(1, 8):
    n = int(input(f"Digite o {c}º valor: "))
    if n % 2 == 0:
        u[0].append(n)
    else:
        u[1].append(n)
u[0].sort()
u[1].sort()
print(f"Valores pares em ordem crescente: {u[0]}")
print(f'Valores ímpares em ordem crescente: {u[1]}')