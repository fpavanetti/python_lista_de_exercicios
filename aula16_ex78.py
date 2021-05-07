'''

DESAFIO 78 - CONTANDO VOGAIS EM TUPLA

Crie um programa que tenha uma tupla com várias palavras
(não use acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
'''
tupla = ("aprender", "programar", "linguagem", "python", "curso", "gratis",
         "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
# importante lembrar que cada string é, também, uma lista
for palavra in tupla:
    print(f"\nNa palavra {palavra.upper()} temos ", end=' ')
    for letra in palavra:
        if letra in "aeiou":
            print(letra, end= ' ')