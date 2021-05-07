'''
Tipos primitivos

n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
s = n1 + n2
print('A soma vale', s)
print('A soma vale{}'.format(s))

> Os tipos primitivos no Python (e em muitas outras linguagens de programação.
Em outros casos, como o VBA e o Java, subdividem int em outros subtipos.)

str
int
float
bool

'''

n1 = input('Digite um valor: ')
print(type(n1)) #typecast
n2 = int(input('Digite outro número: '))
print(type(n2))
s = n2 + n2
print('A soma entre {} e {} é {}'.format(n2, n2, s))

n3 = float(input("Digite um valor: "))
print(n3)
print(type(n3))

n4 = input('Digite algo: ')
print(n4.isnumeric())
print(n4.isdecimal())
print(n4.isdigit())

















