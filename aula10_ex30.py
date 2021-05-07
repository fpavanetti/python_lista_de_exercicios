'''
Escreva um programa que leia a velocidade de um carro.
Se ele ULTRAPASSAR 80km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.

'''
# PRIMEIRO: LER A VELOCIDADE DO CARRO

v = float(input("Em que velocidade (Km/h) estava seu carro ao passar no radar? "))

# SEGUNDO: CONSTRUIR AS CONDIÇÕES
if v >= 80:
    print("Você foi multado.")
    # TERCEIRO: CALCULAR E EXIBIR A MULTA
    print("Para cara Km acima de 80, você deverá pagar \n"
          "R$7,00 de multa.")
    n = v - 80
    m = n * 7
    print("Você estava andando a uma velocidade de {}km/h e \n"
          "terá de pagar uma multa no valor de R${:.0f},00.".format(v, m))
else:
    print("Parabéns! Continue dirigindo com segurança!")
