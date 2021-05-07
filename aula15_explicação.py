'''

AULA 15 - Laços de repetição (parte 3)

While -> Teste lógico no início

For

Do While / Repeat (não existe no Python)

while True:
    if chão
        passo
    if vazio
        pula
    if moeda
        pega
    if trofeu
        pula
        break
pega

'''

cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print("Acabou")

while True: # não existe condição; o loop é eterno, a menos que seja quebrado
    break

n = s = cont = 0
while n != 999:
    n = int(input("Digite um número: "))
    cont += 1
    s = s + n

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print("A soma vale {}".format(s))
print(f'A soma vale {s:.2f}')
print("O %s tem %d anos." % (nome, idade))
#{s:^20}
# PEP