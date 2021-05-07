'''
locadora = []
jogo1 = {'Título': 'The Legend of Zelda: Majoras Mask',
         'Ano': 2000,
         'Desenvovedora': 'Nintendo'}
jogo2 = {'Título': 'The Legend of Zelda: Breath of The Wild',
         'Ano': 2017,
         'Desenvolvedora': 'Nintendo'}
jogo3 = {'Título': 'The Legend of Zelda: Twilight Princess',
         'Ano': 2006,
         'Desenvolvedora': 'Nintendo'}
locadora.append(jogo1)
locadora.append(jogo2)
locadora.append(jogo3)
for d in range(0, 3):
    print(locadora[d]['Ano'])


sobre dicionários

é possível inserir dados em dicionários por meio de inputs
é possível utilizar laços que utilizem decisões para complementar ou não dicionários
for k, v in dicionário.items() é a forma mais simples de exibir de maneira organizada os dados dentro de um dicionário
posso colocar uma lista como valor de uma chave de um dicionário por meio de um copy ou [:]
função sum() faz a soma dos elementos de uma lista
[0] num input pega apenas a primeira letra
a função clear, utilizada em laços ao preencher estruturas compostas em python, vem ao final do laço em for e ao início do laço em while
{:5 (quantas casas).2f (quantos pontos flutuantes)}
dicionario.get('nome da chave') busca chave
d1.update({'nova_chave':'novo_valor'), atualizar chave
del dicionario['chave aleatória] para apagar chave
"desempacotar": pegar estruturas compostas e exibi-las por meio de um laço
podemos colocar um dicionário dentro de um dicionário
\t identação

for clientes_k, clientes_v in clientes.items():
	print(f'Exibindo {clientes_k}')
	for dados_k, dados_v in clientes_v.items():
		print(f'\t{dados_k} = {dados_v}')

>> cópia rasa (.copy), cópia profunda (módulo copy = copy.deepcopy(dicionário)
'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'{k} - {v}')
