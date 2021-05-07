'''
AULA 13 - Estrutura de repetição FOR

Laços / Repetições / Iterações (Parte 1)

O comando for utiliza um CONTADOR para interromper o laço

Laço com variável de controle

laço c no intervalo(1, 10)
    passo
pega

for c in range (1, 10):
    passo
pega

for c in range(0, 3):
    passo
    pula
passo
pega

for c in range(0, 3):
    if moeda == true:
        pega
    passo
    pula
passo
pega

'''

print("oi")
print("oi")
print("oi")
for c in range(1, 6): # o python não considera o último número
    print("oi")
    print(c)
print("FIM")

for c in range(6, 0, -1): # o passo está negativo
    print(c) # em portugol seria algo como "para c de 6 ate 0 passo -1 faca"

for c in range(0, 7, 2): # o passo é 2
    print(c)

n = int(input("Digite um número: "))
for c in range(0, n+1): #o +1 é necessário em python pq ele para no número final
    print(c)
print("FIM")

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("Fim")

s = 0 #somatorio
for c in range(0, 4):
    n = int(input("Digite um número: "))
    s = s + n
print(s)
print("Fim")


















