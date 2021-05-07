'''

DESAFIO 67

Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No
final, mostre quantos números foram digitados e qual foi a soma entre eles (des-
considerando o flag).

O que deve aparecer:

"A soma dos x valores foi y!"


'''

# Primeiro: criar as variáveis de contador e soma
n_d = 0
s_n = 0

print("*-" * 20)
print("          Contador de números")
print("*-" * 20)

# Segundo: criar o leitor de números já com condição de parada
while True:
    n = int(input("Digite um número inteiro (999 para parar): "))
    if n == 999:
        break
    else:
        # criar os contadores de números digitados e a soma entre eles
        n_d = n_d + 1
        s_n = s_n + n
print(f"Foram digitados {n_d} valores e a soma entre eles é {s_n}.")