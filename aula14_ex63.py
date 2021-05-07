'''

DESAFIO 63

Melhore o desafio 62, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.
'''

p1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
resp = int
while resp != 0:
    resp = int(input("Quantos termos deseja verificar? "))
    for resp in range(1, resp + 1):
        print(p1, end=' ')
        p1 = p1 + r
    print()
print("Leitor de PAs encerrado com sucesso.")

'''
Resolução Guanabara

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo, end='')
        termo = termo + razão
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))



'''