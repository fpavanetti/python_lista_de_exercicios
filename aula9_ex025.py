'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome SANTO.

'''

c = str(input("Digite o nome de uma cidade: ")).upper() #upper para não haver problemas com a digitação do usuário
print(c)
cc = c.split() # nova variável para que a alteração seja salva

print('SANTO' in cc[0]) # posição 0 (primeira) para verificar

# usei o split, para criar listas e depois verifiquei o 1o elemento da lista

'''
Solução Guanabara

cid = str(input("Em que cidade você nasceu? ")).strip()
print(cid[:5].upper() == 'SANTO')
'''