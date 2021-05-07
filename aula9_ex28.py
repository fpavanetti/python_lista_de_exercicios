'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza


'''

n = str(input("Digite seu nome completo: "))
print(n)
lista = (n.split())
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(lista[0]))
print("Seu último nome é {}".format(lista[-1]))
