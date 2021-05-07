'''
--- AULA 11: CORES NO TERMINAL ---

Existem diferentes formas de colocar cores no Python.
Aqui veremos apenas o básico, utilizando o padrão ANSI,
também utilizado pela linguagem C.

Tudo em ANSI começa com \ (contrabarra)

\33[cor]
    estilo/texto/fundo
\33[0;33;44m

Estilo
0 none
1 bold
4 underline
7 negative

Texto
30 cinza
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza escuro

Fundo
40 cinza
41 vermelho
42 verde
43 amarelo
44 azul
45 magenta
46 ciano
47 cinza escuro

'''

print("\033[31;43mOlá, mundo\033[m!")
nome = "Fagner"
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'} #isso é um exemplo de dicionários


print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format('\033[4;33;44m', nome,'\033[m'))
print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format(cores['pretoebranco'], nome, cores['limpa']))
s = "prova de python"
print(len(s))