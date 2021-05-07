''' Escreva um programa que converta uma temperatura digitada em ºC para ºF'''

'''Conversão de Celsius para Farenheit: X * 1,8 + 32 = Y'''
'''Conversão de Farenheit para Celsius: (X - 32) * 32 = Y'''

c = float(input("Digite a temperatura atual em graus celsius: º"))
f = (c * 1.8) + 32
print("A temperatura de º{} graus celsius em farenheit é de º{:.2f}".format(c, f))

