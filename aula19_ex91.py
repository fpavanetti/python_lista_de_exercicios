'''

DESAFIO 91

Faça um programa que leia nome e média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo
da estrutura na tela.

'''
aluno = {}
aluno['Nome'] = str(input("Nome: "))
aluno['Média'] = float(input("Média: "))
if aluno['Média'] >= 7:
    aluno['Status'] = 'APROVADO'
elif 6 <= aluno['Média'] < 7:
    aluno['Status'] = 'RECUPERAÇÃO'
else:
    aluno['Status'] = 'REPROVADO'
print(aluno)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
print('>>> FIM DO PROGRAMA <<<')