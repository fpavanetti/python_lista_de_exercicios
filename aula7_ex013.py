''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto '''

p_i = float(input("Digite o preço do produto: R$"))
d = p_i * 0.05
p_f = p_i - d
print("O preço final do produto com 5% é R${:.2f}.".format(p_f))
print("O desconto foi de R${:.2f}".format(d))

''' Também é possível calcular porcentagem dessa forma: 10*5/100'''
