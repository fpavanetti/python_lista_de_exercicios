'''
Aulas 18 - Listas Parte 2

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) /// Pedro
print(dado[1] /// 25

pessoas = lista()
pessoas.append(dados[:]) /// fatiamento completo da estrutura de dados

pessoas = [['Pedro', 25], ['Maria', 19], [João, 32]]
print(pessoas[0][0]) >>> printará Pedro
print(pessoas[1][1]) >>> 19
print(pessoas[2][0] >>> João
print(pessoas[1]) >>> [Maria, 19]


'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galerinha = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.') # para imprimir

galerona = list()
dado = list()
totmen = totmai = 0
for c in range(0, 5):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galerona.append(dado[:])
    dado.clear()
for p in galerona:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
