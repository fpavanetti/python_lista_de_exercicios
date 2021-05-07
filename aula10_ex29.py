'''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usu-
ário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu
ou perdeu.

'''

import random
from time import sleep
n = random.randrange(0, 5) # o método randrange seleciona um número aleatório dentro de um intervalo determinado

print("=" * 30)
print("Neste jogo, você precisa adivinhar o número em que o computador \n"
      "está pensando, entre 0 e 5.\n"
      "Será que você consegue?")
u = int(input("Digite um valor de 0 a 5: "))
print("PROCESSANDO...")
sleep(2)
if n == u:
    print("PARABÉNS! Você venceu! O número escolhido pelo computador foi {}.".format(n))
else:
    print("Você perdeu! :( O número em que o computador pensou foi {}.".format(n))
print("=" * 30)
