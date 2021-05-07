'''

Aula 20 - Funções (Parte 1)

As funções estão relacionadas às rotinas. Exemplos: print(), len(), input(),
int(), float()...

>> Criamos funções para executar rotinas que realizamos constantemente em nossos
códigos, de modo a otimizar nosso tempo - e muito mais. Nem todas as funções de
que possamos vir a precisar estão incluídas no Python, mesmo que ele seja uma
linguagem bastante robusta nesse sentido - em C, por exemplo, para realizarmos
um print sequer, é necessário importar uma biblioteca.

Em Python, para criarmos uma função utilizamos o comando def, que significa
"definição de função".

FUNÇÕES > PARÂMETROS

'''


def lin():
    print('-' * 30)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def soma(a, b):
    s = a + b
    print(f'A = {a} e B = {b}')
    print(f'A soma A + B = {s}')


def cont(* num):
    for valor in num:
        print(valor, end=' ')
    print(f'\n{len(num)}')
    print(sum(num))


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def soma_suprema(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')


# PROGRAMA PRINCIPAL
lin()
print("\t\tCurso em vídeo")
lin()
print("\t\tFagner Pavanetti")
lin()
print("\t\t\tPYTHON")
lin()
print()
titulo('\t\tCURSO EM VÍDEO')
print()
soma(5, 4)
soma(10, 100)
soma(b=15, a=20)
print()
cont(2, 1, 7)
cont(8, 0)
cont(4, 4, 7, 6, 2)
print()
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
print()
soma_suprema(20, 40, 60)