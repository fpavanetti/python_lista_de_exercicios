''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0.15 por Km rodado'''

km = float(input("Quantos km's foram rodados com o carro? "))
print("{}km".format(km))
d = int(input("Por quantos dias o carro foi alugado? "))
print("{} dia(s) alugado".format(d))
v_d = 60.0 * d
v_km = km * 0.15
v_f = v_d + v_km
print("Tendo sido alugado por {} dias, o valor do aluguel foi de R${:.2F}.".format(d, v_d))
print("Adicionalmente, foram cobrados R$0,15 por cada Km rodado, um total de {}km(s), totalizando R${:.2f}.".format(km, v_km))
print("=" * 30)
print()
print("VALOR FINAL A SER PAGO: R${:.2f}".format(v_f))
print()
print("=" * 30)