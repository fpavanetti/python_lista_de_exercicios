# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis.

n = input("Digite algo: ")
print("O tipo primitivo de n é ", type(n))
print('É um dígito?', n.isdigit())
print('É decimal?', n.isdecimal())
print('É numérico?', n.isnumeric())
print('É alfa?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('É wtf?', n.isidentifier())
print('É minúsculo?', n.islower())
print('É maiúsculo?', n.isupper())
print('É ascii?', n.isascii())

''' o n é um objeto - possui atributos e métodos'''