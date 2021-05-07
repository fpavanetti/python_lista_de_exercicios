'''

DESAFIO 73 - Número por extenso

Crie um programa que tenha uma tupla TOTALMENTE PREENCHIDA com uma
contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.
'''
#criar a tupla
contagem = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
            "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
#ler um número pelo teclado
num = int(input("Digite um número inteiro de 0 até 20: "))
while True:
    if num < 0 or num > 20:
        num = int(input("ERRO. Digite um número inteiro de 0 até 20: "))
    else:
        break
print()
print("=" * 100)
print("{:^100}".format(f"O número digitado por extenso é {contagem[num]}.".upper()))
print("=" * 100)

