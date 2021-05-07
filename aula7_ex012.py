''' Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintála, sabendo que cada litro de tinta, pinta uma área de
2m² '''

b = float(input("Qual é a largura da parede em metros? "))
a = float(input("Qual é a altura da parede em metros? "))

ar = b * a
print("Sua parede tem a dimensão de {}x{}.".format(b, a))
print("A área da parede é de {}m²".format(ar))
qnt = ar / 2
print("Serão necessários {:.2f}lts de tinta para pintar esta parede.".format(qnt))