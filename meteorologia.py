'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e 
a maior temperaturas informadas, bem como a média das temperaturas.
'''

lista_temperaturas = [-10, 40, 33, 29, 50, -5, 14, 5, -30, 0]
temperatura = 0

print("*** DEPARTAMENTO ESTADUAL DE METEOROLOGIA ***")
print(lista_temperaturas)
print("A menor temperatura é: ", min(lista_temperaturas), "graus celsius")
print("A maior temperatura é: ", max(lista_temperaturas), "graus celsius")

total = temperatura
for temperatura in lista_temperaturas:
    total = total + temperatura
    
media_temperaturas = total/len(lista_temperaturas)
print("A média de temperaturas é: ", media_temperaturas)