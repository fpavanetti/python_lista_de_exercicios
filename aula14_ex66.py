'''

DESAFIO 66

Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer continuar
ou não a digitar valores.
'''
resp = str
s = int(0)
maior_valor = int(0)
menor_valor = int
c = 0
while resp != '2':
    n = int(input("Digite um número inteiro: "))
    c = c + 1
    if c == 1:
        maior_valor = menor_valor = n
    else:
        if n > maior_valor:
            maior_valor = n
        if n < menor_valor:
            menor_valor = n
    s = s + n
    resp = str(input("Deseja continuar a digitar valores? [SIM: 1]/[NÃO: 2]: "))
    while resp not in "12":
        resp = str(input("Informe uma opção válida. Deseja continuar a digitar valores? [SIM: 1]/[NÃO: 2]: "))
print("MAIOR VALOR: {}".format(maior_valor))
print("MENOR VALOR: {}".format(menor_valor))
m = s / c
print("MÉDIA DOS VALORES LIDOS: {}".format(m))