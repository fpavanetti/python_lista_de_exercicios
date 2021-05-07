'''
Aula 10: Estruturas Condicionais Simples e Compostas

> todo método recebe () ao final

objeto.método()

if objeto.metodo()
    bla bla bla
else
    bla bla bla

Numa condição, nunca ambos os blocos serão executados.

(O que são operadores ternários?)
double salario = 1000;
double bonus = salario * (salario > 1000 ? 0.10 : 0.15);
System.out.println(bonus);

< EXEMPLO DE OPERADOR TERNÁRIO EM JAVA >

print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS')

< O PYTHON NÃO TEM OPERADORES TERNÁRIOS >

Condições simples
> Utilizam apenas o if
Condições compostas
> Utilizam if e else
Condições simplificadas
> Utilizam o if e o else na mesma linha, quase como
um operador ternário.


'''

nome = str(input("Qual é o seu nome? "))
if nome == "Gustavo":
    print("Que nome lindo você tem!")
else:
    print("Seu nome não é lá muito especial.")
print("Bom dia, {}".format(nome))

n1 = float("Digite a 1a nota: ")
n2 = float("Digite a 2a nota: ")
m = (n1 + n2) / 2
print("A sua média foi {:.1f}".format(m))
if m >= 6.0:
    print("Sua média foi boa!")
else:
    print("Sua média precisa melhorar. Você foi reprovado")


