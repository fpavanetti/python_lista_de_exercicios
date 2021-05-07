''' Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a raiz quadrada '''

n = int(input("Digite um número inteiro qualquer: "))
print("O dobro do número {} é {}, \no tripo é {} \ne sua raiz quadrada é {:.2f}.".format(n, n * 2, n * 3, n**(1/2)))
print("Você também pode calcular a raiz quadrada de {} assim: {}".format(n, pow(n, 1/2)))