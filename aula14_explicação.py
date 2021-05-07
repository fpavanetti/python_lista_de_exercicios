'''

AULA 14 - ESTRUTURA DE REPETIÇÃO WHILE

Para a ESTRUTURA for criamos um laço em que temos que determinar um final.
> Com variável de controle
Para a ESTRUTURA while sabemos o limite, enquanto o valor booleano não
for verdadeiro, o programa rodará em loop.
> Com teste lógico

enquanto não fim do caminho
    passo
pega

while not end of the road:
    passo
pega

== para situações com variações no caminho ==

while não maça:
    if chão:
        passo:
    if buraco:
        pulo
    if moeda:
        pega
pega

'''

for c in range(1, 10):
    print(c)
print("Fim")

c = 1
while c < 10:
    print(c)
    c = c + 1
print("Fim")

n = 1
for n in range(1, 5):
    n = int(input("Digite um valor: "))
print("fim")

while n != 0:
    n = int(input("Digite um valor: "))
print("fim")

# FLAG: CONDIÇÃO DE PARADA

r = 'S'
while r == 'S':
    n = int(input("Digite um número: "))
    r = str(input("Quer continuar [S/N]: "))
print("Fim")


m = 1
par = 0
ímpar = 0
while m != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            ímpar = ímpar + 1
print("Acabou")
