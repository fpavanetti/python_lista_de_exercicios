'''

DESAFIO 59 - Jogo de Adivinhação 2.0

Melhore o jogo DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.

'''

from random import randint
from time import sleep
print("=*=" * 20)
print("================ JOGO DA ADIVINHAÇÃO ===============")
print("Quantas tentativas você precisa para derrotar o computador?")
print("=*=" * 20)

cont_tentativas = int(1)
computador = randint(0, 10)
usuario = int(input("Digite um número entre 0 e 10: "))

while usuario != computador:
    print("Você errou! Tente novamente.")
    usuario = int(input("Digite um número entre 0 e 10: "))
    cont_tentativas = cont_tentativas + 1
print("=*=" * 20)
print("Você venceu!!!")
print("Foram necessárias {} tentativa(s) para vencer.".format(cont_tentativas))


'''
Solução Guanabara

from random import randint
computador = randint(0, 10)
print("Sou o seu computador e acabei de pernsar num número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...")
        elif jogador > computador:
            print("Menos...")
print("Acertou com {} tentativas!".format(palpites))



'''
