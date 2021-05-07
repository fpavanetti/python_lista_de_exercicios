'''
DESAFIO 43 - ANALISANDO TRIÂNGULOS v2.0

Refaça o DESAFIO 036 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será for-
mado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes

'''

# PRIMEIRO PASSO: LER OS SEGMENTOS DE RETA

ab = float(input("Digite o primeiro segmento de reta: "))
cd = float(input("Digite o segundo segmento de reta: "))
ef = float(input("Digite o terceiro segmento de reta: "))

# SEGUNDO PASSO: CHECAR SE PODEM FORMAR UM TRIÂNGULO

if (ab + cd) > ef and (ab + ef) > cd and (cd + ef) > ab:
    # TERCEIRO PASSO: ESTRUTURA DE CONDIÇÃO BASEADA EM COMPARAÇÕES
    if ab == cd and ab == ef:
        print("Triângulo Equilátero - todos os lados são iguais.")
    elif ab == cd and ab != ef or ab == ef and ab != cd:
        print("Triângulo Isósceles - dois lados iguais.")
    else:
        print("Triângulo Escaleno - todos os lados são diferentes.")
else:
    print("Esses segmentos de reta não podem formar um triângulo.")

'''
print("Os segmentos acima podem formar um triângulo", end'')
print("EQUILÁTERO")
'''