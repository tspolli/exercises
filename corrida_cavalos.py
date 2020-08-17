'''
Sua equipe foi contratada para desenvolver um programa para computar cada aposta em uma corrida de cavalos, 
a telefonista digitará um número, entre 1 e 15, correspondente ao número do cavalo. 
Um número de cavalo igual zero, indica que as apostas foram encerradas. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, 
e voltando a pedir outro número. Após o final das apostas, o programa deverá exibir:

O total de apostas computadas;
Os números e respectivas apostas de todos os cavalos que receberam aposta;
O percentual de aposta de cada um destes cavalos;
O número do cavalo escolhido como preferido na corrida, juntamente com o número de apostas e o 
percentual dados a ele.

Observe que as apostas inválidas e o zero final não devem ser computados. 
O resultado aparece ordenado pelo número do cavalo. O programa deve fazer uso de arrays.

Resultado das apostas:

Foram computados 8 apostas.

Cavalo        Votos               %
9               4               50,0%
10              3               37,5%
11              1               12,5%
A maior quantidade de apostas foi no número 9, com 4 apostas, correspondendo a 50% do total de apostas.
'''

cavalos = { 
1:0,
2:0,
3:0,
4:0,
5:0,
6:0,
7:0,
8:0,
9:0,
10:0,
11:0,
12:0,
13:0,
14:0,
15:0
}

print("*** CORRIDA DE CAVALOS ***")
print("Insira sua aposta: ")
aposta = int(input())

total_apostas = 0
while aposta != 0:
        if (aposta == 1 or aposta == 2 or aposta == 3 or aposta == 4 or aposta == 5 or aposta == 6 or
            aposta == 7 or aposta == 8 or aposta == 9 or aposta == 10 or aposta == 11 or aposta == 12 or
            aposta == 13 or aposta == 14 or aposta == 15):
            cavalos[aposta] = cavalos[aposta] + 1
            print("Insira sua aposta: ")
            aposta = int(input())
            total_apostas = total_apostas + 1
        else:
            print("Cavalo inválido!")
            print("Insira a sua aposta: ")
            aposta = int(input())
else:
    print("Apostas encerradas!")

print("O resultado das apostas: \n")
print("Foram computadas ", total_apostas, "apostas\n\n")
print("Cavalo      Votos        %\n")

maior_aposta = 0
for i in cavalos:
    percentual_apostas = (cavalos[i]/total_apostas)*100
    linha = str(i).ljust(12) + str(cavalos[i]).ljust(13) + str(percentual_apostas)
    print(linha)
    if cavalos[i] > maior_aposta:
        maior_aposta = cavalos[i]
        maior_cavalo_apostado = i

print("A maior quantidade de apostas foi no número ", maior_cavalo_apostado, "com ", maior_aposta, "apostas, correspondendo a ", "{0:.2f}% do total de apostas".format((maior_aposta/total_apostas)*100))