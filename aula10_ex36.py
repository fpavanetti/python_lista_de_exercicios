'''
Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não
formar um triângulo.

'''

ab = float(input("Digite o valor do primeiro segmento de reta: "))
cd = float(input("Digite o valor do segundo segmento de reta: "))
ef = float(input("Digite o valor do terceiro segmento de reta: "))

if (ab + cd) > ef:
    print("FORMA UM TRIÂNGULO")
else:
    print("NÃO FORMA UM TRIÂNGULO")