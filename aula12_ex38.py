'''
DESAFIO 38 - CONVERSOR DE BASES NUMÉRICAS

Escreva um programa que leia um número inteiro
qualquer e peça para o usuário esclher qual será
a base de conversão:

[1] para binário
[2] para octal
[3] para hexadecimal
'''

'''
O python permite a conversão de bases de diferentes maneiras. Existem as funções
bin, oct e hex, que retornam o código das bases + os números convertidos. Aqui
utilizarei o format, para que sejam exibidos apenas os números convertidos
'''
n = int(input("Digite um número inteiro qualquer: "))
print("Código da conversão de bases:\n"
      "[1] para binário\n"
      "[2] para octal\n"
      "[3] para hexadecimal\n"
      "-Digite apenas o número-")
escolha = int(input("Para qual base você deseja converter o número {}? ".format(n)))

if escolha == 1:
    print("O número {1} convertido para binário é {0:b}".format(n, n))
elif escolha == 2:
    print("O número {1} convertido para octal é {0:o}".format(n, n))
elif escolha == 3:
    print("O número {1} convertido para hexadecimal é {0:x}".format(n, n))
else:
    print("Você não informou um digito válido.")

'''
Resolução Guanabara:
ao invés de formatar diretamente como eu fiz no exercício,
o professor fez .format(bin(num)[2:]) /// fatiamento de strings
para ocultar os códigos de identificação iniciais do python
'''
