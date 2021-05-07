'''
DESAFIO 44 - ÍNDICE DE MASSA CORPORAL

Desenvolva uma lógica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: obesidade mórbida

'''

#PRIMEIRO: DESENVOLVER O CÁLCULO DO IMC

a = float(input("Digite sua altura (em metros): "))
p = float(input("Digite seu peso (em Kgs): "))
imc = p / (a * a)
# imc = p (a ** 2)
#SEGUNDO: ESTRUTURA CONDICIONAL

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc < 25:
    print("Você está no seu peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 40:
    print("Você está obeso.")
else:
    print("Cuidado; sua obesidade já é mórbida.")
print("Seu IMC é de {:.2f}".format(imc))
