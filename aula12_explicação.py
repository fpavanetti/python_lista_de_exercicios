'''
--- AULA 12: Condições em Python (If... elif) / Condições Aninhadas

Aninhar: "colocar uma coisa dentro da outra"
Colocar condições dentro de condições: aninhar estrturuas

carro.siga()
if carro.esquerda():
    ...
elif se carro.direita():
    ...
else:
    ...
carro.pare()
'''
nome = str(input("Qual é o seu nome? "))
if nome == "Fagner":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem comum no Brasil")
elif nome == "Veronica":
    print("Seu nome é bem incomum.")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia, {}".format(nome))

# condição aninhada
