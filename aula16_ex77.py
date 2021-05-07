'''

DESAFIO 77 - LISTA DE PREÇOS COM TUPLA

Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma
TABULAR.
'''

listagem = ("Lápis", 2.70, "Borracha", 1.90, "Caderno", 19.90, "Kit Canetas", 7.60, "Estojo", 14.65, "Mochila", 69.99)
print("-" * 50)
print(f'{"LISTAGEM DE PREÇOS - ESCOLAR":^50}')
print("-" * 50)
for item in listagem:
    if type(item) is str:
        print(f"{item:.<30}", end= '')
    else:
        print(f"R${item:>6.2f}")



tupla = ("Lápis", 2.70, "Borracha", 1.90, "Caderno", 19.90, "Kit Canetas", 7.60, "Estojo", 14.65, "Mochila", 69.99)
print('*' * 50)
print(f"{'LISTA DE COMPRAS ESCOLARES':^50}")
print('*' * 50)
for i in tupla: #a "tupla" é o range; para cada elemento(i) na tupla(range) faça: ..........
    if type(i) is str:
        print(f"{i:.<30}", end= '')
    else:
        print(f"R${i:>6.2f}")



















