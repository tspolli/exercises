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

lista_votos = {
1 : 0,
2 : 0,
3 : 0,
4 : 0,
5 : 0,
6 : 0,
}

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
    lista_votos[opcao] = lista_votos[opcao] + 1

print("O total de votos para o candidato Lula foi de: ", lista_votos[1])
print("O total de votos para a candidata Dilma foi de: ", lista_votos[2])
print("O total de votos para o candidato Bolsonaro foi de: ", lista_votos[3])
print("O total de votos para o candidato Fernando Henrique foi de: ", lista_votos[4])
print("O total de votos nulos foi de: ", lista_votos[5])
print("O total de votos em branco foi de: ", lista_votos[6])

percentual_nulos = (lista_votos[5]/num_eleitores)*100
percentual_brancos = (lista_votos[6]/num_eleitores)*100
percentual_lula = (lista_votos[1]/num_eleitores)*100
percentual_dilma = (lista_votos[2]/num_eleitores)*100
percentual_bolsonaro = (lista_votos[3]/num_eleitores)*100
percentual_fhc = (lista_votos[4]/num_eleitores)*100

print("\nPressione enter para computar o percentual de votos...")
opcao = str(input())
os.system("cls")
print("O percentual de votos nulos sobre o total de votos foi de: ", percentual_nulos, "%")
print("O percentual de votos em branco sobre o total de votos foi de: ", percentual_brancos, "%")
print("O percentual de votos no Lula foi de: ", percentual_lula, "%")
print("O percentual de votos no Dilma foi de: ", percentual_dilma, "%")
print("O percentual de votos no Bolsonaro foi de: ", percentual_bolsonaro, "%")
print("O percentual de votos no Fernando Henrique foi de: ", percentual_fhc, "%")

