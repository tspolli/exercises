'''
Faça um programa que simule um lançamento de dados. 
Lance o dado 100 vezes e armazene os resultados em um vetor. 
Depois, mostre quantas vezes cada valor foi conseguido.
'''

from random import choice

lancando_dados = []
lancamento_dados = 100
numero_acertado = [1, 2, 3, 4, 5, 6]

for lanca in range(1, lancamento_dados+1):
    lancamento = choice(numero_acertado)
    lancando_dados.append(lancamento)
    contador_1 = lancando_dados.count(1)
    contador_2 = lancando_dados.count(2)
    contador_3 = lancando_dados.count(3)
    contador_4 = lancando_dados.count(4)
    contador_5 = lancando_dados.count(5)
    contador_6 = lancando_dados.count(6)

print("O valor 1 foi conseguido: ", contador_1, "vezes", "\nO valor 2 foi conseguido: ", contador_2, "vezes", "\nO valor 3 foi conseguido: ", contador_3, "vezes",  "\nO valor 4 foi conseguido: ", contador_4, "vezes", "\nO valor 5 foi conseguido: ", contador_5, "vezes", "\nO valor 6 foi conseguido: ", contador_6, "vezes")


