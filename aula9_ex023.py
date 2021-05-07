'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas

- O nome com todas minúsculas

- Quantas letras ao todo (sem consirar espaços)

- Quantas letras tem o primeiro nome

'''

n = str(input("Digite seu nome completo: "))
print()
print("*" * 40)
print(n)
print("Com todas as letras maiúsculas: {}.".format(n.upper()))
print("Com todas as letras minúsculas: {}.".format(n.lower()))
print("Número de caracteres do nome sem espaços: {}.".format((len(n.replace(" ", "")))))
'''Solução do Guanabara
print("Seu nome tem ao todo {} letras.".format(len(nome) - nome.count(" ")'''
print("Primeiro nome: {[0]}.".format(n.split()))
# solução guanabara
# print("Seu primeiro nome tem {} letras.".format(nome.find(' ')))
# separa = n.split()
# print("Seu primeiro nome é {} e ele {} letras".format(separa[0], len(separa[0])))
print("*" * 40)
