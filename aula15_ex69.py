'''

DESAFIO 69

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquis-
tou no final do jogo.

> diga um valor
> é par ou ímpar
> o que vc jogou e o que o pc jogou
> se venceu joga novamente

'''
from random import randint
i = 0
print("=-=" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR\n"
      "  CONTRA O COMPUTADOR?")
print("=-=" * 10)
print()
while True:
    j = int(input("Diga um valor de 0 a 10: "))
    if j > 10 or j < 0:
        print("\033[1;31mVocê informou um número inválido\033[m")
    else:
        c = randint(0, 10)
        e = str(input("Escolha P/I: ")).strip().upper()
        if e != "P" and e != "I":
            print("\033[1;31mVocê informou uma opção inválida\033[m")
        else:
            s = j + c
            if s % 2 == 0 and e == "P":
                print("-" * 20)
                print(f"Você ganhou esta rodada! \n"
                      f"Número digitado: {j}\n"
                      f"Número do computador: {c}\n"
                      f"TOTAL PAR: {s}")
                print()
                i = i + 1
            elif s % 2 != 0 and e == "P":
                print(f"Você perdeu! O número escolhido pelo computador foi {c}\n"
                      f"e a soma dos valores foi {s}. TOTAL ÍMPAR")
                break
            elif s % 2 != 0 and e == "I":
                print("-" * 20)
                print(f"Você ganhou esta rodada!\n"
                      f"Número digitado: {j}\n"
                      f"Númerp do computador: {c}\n"
                      f"TOTAL ÍMPAR: {s}")
                print()
                i = i + 1
            elif s % 2 == 0 and e == "I":
                print(f"Você perdeu! O número escolhido pelo computador foi {c}\n"
                      f"e a soma dos valores foi {s}. TOTAL PAR")
                break
print()
print(f"GAME OVER! Você venceu {i} vez(es).")
