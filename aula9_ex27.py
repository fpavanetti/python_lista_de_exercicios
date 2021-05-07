'''
Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez

'''

f = str(input("Digite uma frase qualquer: ")).upper().split()
print(f)
print("A frase possui {} espaços.".format(len(f)))

print("Número de vezes em que a letra A aparece:")
print(f.count('A')) # Quantas vezes a letra A aparece

# Em que posição A aparece pela primeira vez
print("Posição em que A aparece pela primeira vez:")
print(f.find('A'))

# Em que posição ele aparece pela última vez
print("Posição em que A aparece pela última vez, analisando do fim ao começo:")
print(f[::-1].find('A')) # string[inicio:fim:passo]

'''
Solução Guanabara
frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count('A')))
print("A primeira letra A apareceu na posição {}".format(frase.find('A')+1))
print("A última letra A apareceu na posição {}".format(frase.rfind('A')+1))

A função rfind procura da direita para a esquerda.
O +1 foi adicionado para que o usuário veja na ordem em que estamos acostumados,
contando a partir do 1, e não do 0, como o Python.
'''