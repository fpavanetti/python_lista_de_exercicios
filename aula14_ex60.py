'''

DESAFIO 60 - Criando um Menu de opções

Crie um programa que leia dois valores e mostre um menu
na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada
em cada caso.

'''

n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
print("MENU: \n"
      "[1] SOMAR\n"
      "[2] MULTIPLICAR\n"
      "[3] MAIOR\n"
      "[4] NOVOS NÚMEROS\n"
      "[5] SAIR DO PROGRAMA")
resp = int(input("Qual ação deseja realizar? "))

while resp != 5:
    if resp == 1:
        print()
        print("A soma entre {} e {} é igual a {}".format(n1, n2, n1 + n2))
        resp = int(input("Qual ação deseja realizar agora? "))
    elif resp == 2:
        print()
        print("A multiplicação entre {} e {} é igual a {}".format(n1, n2, n1 * n2))
        resp = int(input("Qual ação deseja realizar agora? "))
    elif resp == 3:
        if n1 > n2:
            print()
            print("O maior valor é {}".format(n1))
            resp = int(input("Qual ação deseja realizar agora? "))
        else:
            print()
            print("O maior valor é {}".format(n2))
            resp = int(input("Qual ação deseja realizar agora? "))
    elif resp == 4:
        print()
        n1 = int(input("Digite o 1º valor: "))
        n2 = int(input("Digite o 2º valor: "))
        resp = int(input("Qual ação deseja realizar agora? "))
    elif resp > 5:
        print()
        print("OPÇÃO INVÁLIDA.")
        resp = int(input("Qual ação deseja realizar? "))
print()
print("PROGRAMA ENCERRADO COM SUCESSO")