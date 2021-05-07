'''

DESAFIO 68

Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuários. O programa será interrompido quando o número
solicitado for negativo.



'''

print("----- CALCULADORA DE TABUADAS -----")
print("Para interromper, solicite a tabuada de um número NEGATIVO")
print()
while True:
    n = int(input("Deseja ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("-" * 10)
    for c in range(1, 11):
        print(f"{n} x {c} = {n * c}")
    print("-" * 10)
    print()
print("Programa encerrado.")
