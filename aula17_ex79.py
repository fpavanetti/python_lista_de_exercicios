'''

DESAFIO 79 - MAIOR E MENORES VALORES NA LISTA

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
'''
lista = []
ma = me = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite o {c+1}º elemento da lista: ")))
    if c == 0:
        ma = me = lista[c]
    else:
        if ma < lista[c]:
            ma = lista[c]
        if me > lista[c]:
            me = lista[c]
print(f'A lista informada foi {lista} \n'
      f'O maior valor informado foi {ma} na(s) posição(ões) ', end='')
for indice, itens in enumerate(lista):
    if itens == ma:
        print(indice, end='... ')
print(f"\nO menor valor informado foi {me} na(s) posição(ões) ", end='')
for indice, itens in enumerate(lista):
    if itens == me:
        print(indice, end='...')
