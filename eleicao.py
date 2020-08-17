'''
Numa eleição existem quatro candidatos. 
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que peça o número total de eleitores, receba o voto de cada eleitor
em seguida calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A porcentagem de votos nulos sobre o total de votos;
A porcentagem de votos em branco sobre o total de votos. 
A porcentagem de votos de cada candidato.
'''

import os

lista_votos = []
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

def menu_eleicao():
    print("*** ELEIÇÕES 2020 ***")
    print("Em quem você vota? ")
    print("1- Lula")
    print("2- Dilma")
    print("3- Bolsonaro")
    print("4- Fernando Henrique")
    print("5- Nulo")
    print("6- Em branco")
    print("Selecione uma opção: ")

print("Forneça o número total de eleitores: ")
num_eleitores = int(input())

for eleitor in range(1, num_eleitores+1):
    os.system("cls")
    menu_eleicao()
    opcao = int(input())
    lista_votos.append(opcao)

for voto in lista_votos:
    if voto == 1:
        count_1 = count_1 + 1
    elif voto  == 2:
        count_2 = count_2 + 1
    elif voto  == 3:
        count_3 = count_3 + 1
    elif voto  == 4:
        count_4 = count_4 + 1
    elif voto  == 5:
        count_5 = count_5 + 1
    elif voto  == 6:
        count_6 = count_6 + 1

print("O total de votos para o candidato Lula foi de: ", count_1)
print("O total de votos para a candidata Dilma foi de: ", count_2)
print("O total de votos para o candidato Bolsonaro foi de: ", count_3)
print("O total de votos para o candidato Fernando Henrique foi de: ", count_4)
print("O total de votos nulos foi de: ", count_5)
print("O total de votos em branco foi de: ", count_6)

percentual_nulos = (count_5/num_eleitores)*100
percentual_brancos = (count_6/num_eleitores)*100
percentual_lula = (count_1/num_eleitores)*100
percentual_dilma = (count_2/num_eleitores)*100
percentual_bolsonaro = (count_3/num_eleitores)*100
percentual_fhc = (count_4/num_eleitores)*100

print("\nPressione enter para computar o percentual de votos...")
opcao = str(input())
os.system("cls")
print("O percentual de votos nulos sobre o total de votos foi de: ", percentual_nulos, "%")
print("O percentual de votos em branco sobre o total de votos foi de: ", percentual_brancos, "%")
print("O percentual de votos no Lula foi de: ", percentual_lula, "%")
print("O percentual de votos no Dilma foi de: ", percentual_dilma, "%")
print("O percentual de votos no Bolsonaro foi de: ", percentual_bolsonaro, "%")
print("O percentual de votos no Fernando Henrique foi de: ", percentual_fhc, "%")

