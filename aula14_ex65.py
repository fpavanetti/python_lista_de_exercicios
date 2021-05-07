'''

DESAFIO 65

Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada (flag).
No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).

'''

print("Digitador de números! Digite quantos números quiser e depois veja\n"
      "a soma entre eles. Para interromper o programa, selecione 999.")
print()
n = int #variável de teste
nn = int #variável que, superando o teste, computa os números
s = int(0) #variável de soma
c = int(0) #variável de contador de números digitados
while n != 999:
    n = int(input("Digite um número inteiro: "))
    if n != 999:
        nn = n
        s = s + nn
        c = c + 1
print("QUANTIDADE DE NÚMEROS DIGITADOS: {}\n"
      "SOMA DOS NÚMEROS DIGITADOS: {}".format(c, s))

