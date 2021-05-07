from aula22_exercícios.utilidadesCeV import dados
from aula22_exercícios.utilidadesCeV import moeda

#p = float(input('Digite o preço do produto: R$'))
#print(f'A metade de {p} é {moeda.metade(p)}')
#print(f'O dobro de {p} é {moeda.dobro(p)}')
#print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
#print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')

#108 - FEITO

#p = float(input('Digite o preço do produto: R$'))
#print(f'A metade de {p} é {moeda.moeda(moeda.metade(p))}')
#print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
#print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
#print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')

#109 - FEITO

#p = float(input('Digite o preço do produto: R$'))
#print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
#print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
#print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
#print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')

#110 - FEITO

#p = float(input('Digite o preço do produto: R$'))
#moeda.resumo(p, 50, 20)

#111 - FEITO

#p = float(input('Digite o preço do produto: R$'))
#moeda.resumo(p, 80, 30)

#112 - FEITO

p = dados.leiaDinheiro('Digite o preço do produto: R$')
moeda.resumo(p, 35, 25)
