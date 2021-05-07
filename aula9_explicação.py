''''
AULA 9 - Manipulando Texto

frase = 'Curso em Vídeo Python'
         0123456789...

FATIAMENTO DE STRINGS

frase[9] (colchetes são os identificadores de uma lista)

print(frase[9]) > V

print(frase[9:13]) > Víde (o Python exclui o último número)

print(frase[9:21]) > Vídeo Python

frase[9:21:2] > onde começa > onde para > salto

frase[:5] > quando omito o ínicio, ele vai até onde foi determinado

frase[15:] > do 15 até o final

frase[9::3] > exclui o final; salto 3

ANÁLISE DE STRINGS

len(frase) > qual o comprimento da string

frase.count('o') > contar quantas vezes aparece 'o' minúsculo

frase.count('o', 0, 13) > contagem com fatiamento (do início até o 13 (12))

frase.find('deo') > quantas vezes encontra 'deo' (em que momento começou)

frase.find('Android') > -1 (não existe na string)

'Curso' in frase > retorna True ou False

TRANSFORMAÇÃO

frase.replace('Python', 'Android') > substitui

frase.upper() > maiúscula
frase.lower() > minúscula
frase.capitalize() > SÓ o primeiro caractere fica em maiúscula
frase.title() > TODOS os PRIMEIROS caracteres ficam em maiúsculas

frase.strip() > remove os espaços vazios do ínicio e do fim

frase.rstrip() > remove os espaços vazios da direita

frase.lstrip() > remove os espaços vazios da esquerda

DIVISÃO

frase.split() > remove os espaços vazios e cria novos índices isolados

JUNÇÃO

'-'.join(frase) > junta todos os elementos de strings com um - (ou o que
você desejar)

'''

frase = "Curso em Vídeo Python"
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])

print("""asdiocasdcionaycioniosacnasoicnasdiocnasd
iciaosdncaioscnasoicnsadcioasynioasncasdcnoisadnio""")

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace("Python", "Android"))

frase[0] = 'J' # não é possível modificar

print('Curso' in frase)

print(frase.find('Curso'))
print(frase.lower().find('curso'))

print(frase.split())
dividido = frase.split()
print(dividido[0]) # exibe o primeiro elemento da lista
print(dividido[2] [3]) # exibe a terceira letra do elemento 2







