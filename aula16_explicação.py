'''
Aula 16 - Tuplas em Python

Variáveis compostas
> Em Python, existem 3 tipos de variáveis compostas:
Tuplas
Listas
Dicionários

Uma variável é um espaço que é reservado na memória. Uma variável composta é uma
variável com vários espaços de memória. Strings são variáveis compostas!

Tuplas: um tipo de variável composta

print(lanche[2])
print(lanche[0:2]) // do 0 até o 2 - 1
print(lanche[1:]) // do 1 até o final
print(lanche[-1]) // último elemento

len(lanche) // 4

for c in lanche: // o "lanche" já é o range
    print(c)

As tuplas são IMUTÁVEIS
'''

#() [] {}

lanche = 'hambúrguer'
lanche = 'suco'
# uma é substituída pela outra

lanchão = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanchão[1])
print(lanchão[1:3]) #Suco e pizza
print(lanchão[2:]) #até o final
print(lanchão[:2]) #até o elemento 2 - 1
print(lanchão[-2:]) #começar no -2 até o final da esquerda para a direita

for comida in lanche:
    print(f"Eu vou comer {comida}")

for pos, comida in enumerate(lanchão): #pos = posição
    print(f"Eu vou comer {comida} na posição {pos}")
print("Comi pra caramba!")

for cont in range(0, len(lanchão)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}") # quando necessário mostrar a posição do item na tupla
print("Comi pra caramba!")

print(sorted(lanche)) # ordenado, vira uma lista

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # junção de tuplas, não é a mesma coisa que b + a
print(c)
print(len(c))
print(c.count(5)) # quantas vezes o 5 aparece
print(c.index(8)) # em que posição está, pega a 1a ocorrência
print(c.index(5, 1)) # para verificar o próximo

# tuplas são semelhantes a vetores, mas aceita dados diferentes
pessoa = ("Gustavo", 39, "M", 99.88)
del(pessoa) # apaga a tupla (ou qualquer outra coisa)












