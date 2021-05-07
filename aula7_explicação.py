'''
Operadores aritméticos no Python

+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto da divisão
== igual

Ordem de precedência:
1: () 2: ** 3: * / // % 4: + -

pow(4, 3) > potência
81**(1/2) > raiz quadrada

'''

'''nome = input("Qual é o seu nome? ")
print("Prazer em te conhecer {:20}!".format(nome))
{:<20} > alinhado à esquerda
{:^20} > centralzado
{:=^20} > coloca entre símbolos'''

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
m = n1 * n2
sub = n1 - n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, \na subtração é {}, a multiplicação é {} e a divisão é {:.2f}".format(s, sub, m, d), end=' ')
print("A divisão inteira é {} e a exponênciação é {}".format(di, e))












