'''

DESAFIO 50 - TABUADA 2.0

Refaça o desafio 009, mostrando a tabuada de um
número que o usuário escolher, só que agora
utilizando o laço for.

'''

n = int(input("Informe um número qualquer: "))

for c in range(1, 10+1, 1):
    print("{:2} x {:2} = {:2}".format(n, c, n * c))
