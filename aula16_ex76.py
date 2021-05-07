'''

DESAFIO 76 - ANÁLISE DE DADOS EM UMA TUPLA

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
'''
pares = 0
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
tupla = (n1, n2, n3, n4)
print(f"Você informou os valores {tupla}")
print(f"O valor nove apareceu {tupla.count(9)} vez(es)")
if 3 in tupla:
    print(f"O número 3 apareceu na posição {tupla.index(3)+1}")
else:
    print("O valor 3 não apareceu nenhuma vez.")
for c in tupla: # tupla é o range (4), a cada laço o "c" (variável genérica) pegara o valor contido em tupla no range determinado (tupla 1: valor x = c)
    if c % 2 == 0:
        pares = pares + 1
print(f"Foram digitados {pares} número(s) par(es)")

#eu poderia ter feito uma tupla automaticamente; é possível fazer uma tupla por meio
#de um input