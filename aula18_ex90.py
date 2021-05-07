'''

DESAFIO 90

Crie um programa que leia nome e duas notas e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
'''
from time import sleep
l = []
n = []
no = []
while True:
    n.append(str(input("Nome: ")))
    no.append(float(input("Nota 1: ")))
    no.append(float(input("Nota 2: ")))
    n.append(no[:])
    l.append(n[:])
    n.clear()
    no.clear()
    r = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    while r not in 'SN':
        r = str(input("RESPOSTA INVÁLIDA. Deseja continuar? [S/N]")).upper().strip()
    if r == 'N':
        break
print("-" * 40)
print(f'{"BOLETIM ESCOLAR":^40}')
print(f'NO. ALUNO', end='')
print(f'{"MÉDIA":>20}')
for pos, aluno in enumerate(l):
    sleep(0.5)
    print(f'{pos}  {aluno[0]:.<22}', end='')
    print(f'{(l[pos][1][0] + l[pos][1][1]) /2}')
print("-" * 40)
print()
while True:
    nu = int(input("Deseja verificar as notas de qual aluno? (999 para sair): "))
    if nu == 999:
        break
    else:
        if nu <= len(l) - 1:
            print(f'Notas de {l[nu][0]} são {l[nu][1]}')
sleep(0.5)
print("FINALIZANDO...")
'''print(l)
print(l[0])
print(l[0][0])
print(l[1][0])
print(l[0][1])
print(l[0][1][1])
print(len(l))'''