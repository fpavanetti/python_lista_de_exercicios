'''

DESAFIO 74 - Tuplas com Times de Futebol

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, NA ORDEM de colocação.

DEPOIS, mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética (usar sorted)
D) Em que posição na tabela está o time da Chapecoense


'''

# criar a tupla com os times
times = ("São Paulo", "Internacional", "Atlético-MG", "Flamengo", "Grêmio", "Palmeiras", "Fluminense", "Santos",
         "Ceará", "Corinthians", "Atheletico-PR", "Atlético-GO", "Red Bull Bragantino", "Sport", "Vasco da Gama",
         "Fortaleza", "Bahia", "Goiás", "Botafogo", "Coritiba")
print("=*" * 50)
print("{:^75}".format("TABELA DO BRASILEIRÃO"))
print("{:^75}".format(f"CINCO PRIMEIROS COLOCADOS: {times[0:5]}"))
print("-*-" * 25)
print("{:<75}".format(f"QUATRO ÚLTIMOS COLOCADOS: {times[-4:]}"))
print("-*-" * 25)
print("{:<75}".format(f"ORDEM ALFABÉTICA DOS TIMES: {sorted(times)}"))
print("-*-" * 25)
print("{:<75}".format(f"O SANTOS ESTÁ NA {times.index('Santos')+1}ª POSIÇÃO")) #se a contagem começa em "1", sei que a posição será sempre +1 daquela identificada pelo index
print("=" * 50)
