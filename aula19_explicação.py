'''
Aula 19 - Estruturas compostas (DICIONÁRIOS)

As estruturas compostas no Python são:
> Tuplas
> Listas
> Dicionários

Relembrando listas:
dados. list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1)

Como obter índices literais? >>> Por meio dos Dicionários

Tuplas: ()
Listas: []
Dicionários: {}
dados = dict{} ou dados = {'nome': 'Pedro', 'idade': 25}
                        [IDENTIFICADOR][VALOR]
print(dados['nome'] >>> Pedro
print(dados['idade']) >>> 25

APPEND NÃO FUNCIONA COM DICIONÁRIOS
dados['sexo'] = 'M' <<< adicionando elementos aos dicionários
del dados['idade'] <<< eliminando elementos e valores

filme = {
         'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
            }
O Python chama os elementos de CHAVES (KEYS)
print(filme.values()) >>> retorna todos os VALORES
print(filme.keys()) >>> retorna todas as CHAVES
print(filme.items()) >>> retorna TODOS os VALORES e CHAVES

for key, value in filme.items():
    print(f'O {key} é {value}')
            título    Star Wars
            ano       1977
            diretor   diretor
'''

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.keys():
    print(f'{k} = {v}')
del pessoas['sexo']
pessoas['nome'] = 'Leandro' # muda o valor dentro da chave
pessoas['peso'] = 98.5 # adiciona uma nova chave e valor

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[1]['Sigla'])

estado = dict()
brasill = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasill.append(estado.copy())
for e in brasil:
    print(e)

for e in brasill: #primeiro for para lista, segundo para dicionário
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

