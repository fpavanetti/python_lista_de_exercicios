''' Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros '''
m = int(input("Digite um valor qualquer em metros: "))
''' 1m = 100cm = 1000ml '''
cm = m * 100
mm = m * 1000
print("O valor de {}m convertido em cm é \n{}cm \ne em milímetros é \n{}mm.".format(m, cm, mm))
