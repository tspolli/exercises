'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

print("*** NUMEROS PRIMOS ***")
print("Digite um número inteiro: ")
numero_inteiro = int(input())
numero_dividido_primo = []
numero_dividido_nao_primo = []

for item in range(1, numero_inteiro+1):
    if numero_inteiro % item == 0:
        numero_dividido_primo.append(item)
        item = item + 1
    else:
        numero_dividido_nao_primo.append(item)
        item = item + 1

if numero_dividido_primo[0] == 1 and numero_dividido_primo[1] == numero_inteiro:
    print(numero_inteiro, "é um número primo")
else:
    print(numero_inteiro, "não é um número primo")