'''

DESAFIO 84 - VALIDANDO EXPRESSÕES MATEMÁTICAS

Crie um programa em que o usuário digite uma expressão matemática qualquer
que utilize parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.
'''
e = str(input("Digite uma expressão matemática: "))
p = []
for s in e:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão está errada!")