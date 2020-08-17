import math
'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

print("*** LOJA DE TINTAS ***")
print("Informe o tamanho da área em metros quadrados a ser pintada: ")
metragem = float(input())
cobertura_litros = 1
cobertura_metros = 3
litros_lata = 18
preco = 80.00

qtde_latas_tinta = (metragem/cobertura_metros)/litros_lata
qtde_latas_tinta = math.ceil(qtde_latas_tinta)
preco_total = float(qtde_latas_tinta*preco)

print("Você precisa comprar: ", qtde_latas_tinta, "latas de tinta e o preço total é de R$: ", preco_total)
