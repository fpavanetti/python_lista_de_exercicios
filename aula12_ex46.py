'''
DESAFIO 46 - GAME: Pedra Papel e Tesoura

Crie um programa que faça o computador JOGAR
Jokenpô com você.

'''

from random import randint
from time import sleep

print("\033[1mVamos jogar Jokenpô com o computador!\033[m")
print("PAPEL: [1]\n"
      "PEDRA: [2]\n"
      "TESOURA: [3]")

escolha = int(input("Escolha sua opção: "))
pc = randint(1, 3)
print("Processando...")
sleep(2)
print("JO")
sleep(0.3)
print("KEN")
sleep(0.3)
print("PÔ!")
sleep(0.2)
if escolha == 1 and pc == 1 or escolha == 2 and pc == 2 or escolha == 3 and pc == 3:
    print("EMPATE! O computador usou a mesma opção que você.")
elif escolha == 1 and pc == 2:
    print("Computador: Pedra\n"
          "Você venceu!")
elif escolha == 1 and pc == 3:
    print("Computador: Tesoura\n"
          "Você perdeu. :(")
elif escolha == 2 and pc == 1:
    print("Computador: Papel\n"
          "Você perdeu. :(")
elif escolha == 2 and pc == 3:
    print("Computador: Tesoura\n"
          "Você venceu!")
elif escolha == 3 and pc == 1:
    print("Computador: Papel\n"
          "Você venceu!")
elif escolha == 3 and pc == 2:
    print("Computador: Pedra\n"
          "Você perdeu. :(")
else:
    print("\033[1mESCOLHA UMA OPÇÃO VÁLIDA\033[m")
print("Fim de jogo.")

'''
RESOLUÇÃO GUANABARA

itens = ('Pedra', 'Papel', 'Tesoura') # guanabara usou objetos
computador = randint(0, 2)
print("O computador escolheu {}".format(itens[computador]

'''