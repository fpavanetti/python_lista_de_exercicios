'''

AULA 17 - VARIÁVEIS COMPOSTAS (LISTAS: PARTE 1)

Os índices em Python são chamados de KEY

Para casos em que precisamos de listas CONSTANTES = tuplas
Para casos em que precisamos manipular os dados dentro
da estrutura = LISTAS

lista = [1, 2, 3, 4]
lista[3] = 'outra coisa'

Para adicionar elementos na lista: lista.append('elemento novo')
Para adicionar elementos em outras posições: lista.insert(0, "outro novo elemento")
Para apagar elementos:
del lanche[3]
lanche.pop[3] > geralmente elimina o último elemento
lanche.remove("Elemento")

Para descobrir se um elemento estiver na lista:
if elemento in lista:
    lista.remove('elemento')

criando listas com ranges:

valores = list(range(4,11))
cria uma lista chamada valores, com os valores de 4 a 10, índice 0 a 6

ordenar os valores > valores.sort()
valores.sort(reverse=True) > ordenar ao contrário
ler o número de valores > len(valores)

'''

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0) # na posição 2, adiciona o 0
num.pop() # elimina o último elemento
num.pop(2) # elimina a key índice 2
# o remove remove o 1o valor encontrado
print(num)
print(f'Essa lista tem {len(num)} elementos.')

lista = []
lista.append(5)
lista.append(9)
lista.append(4)
for valores in lista:
    print(f'{valores}...', end=' ')
print()
for chaves, valores in enumerate(lista):
    print(f'Na posição {chaves} encontrei o valor {valores}!')
print('Cheguei ao final da lista.')
listinha = list()
for cont in range(0, 5):
    listinha.append(int(input("Digite um valor: ")))
for c, v in enumerate(listinha):
    print(f'Na posição {c} encontrei o valor {v}!')
listinha.sort(reverse=True)
print(listinha)

a = [2, 3, 4, 7]
b = a # o python não COPIA simplesmente; ele faz uma ligação
c = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')







