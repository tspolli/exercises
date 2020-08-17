'''
Faça um programa que peça dois números, base e expoente, calcule e mostre 
o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

print("*** CALCULO DE POTENCIA ***")
print("Informe a base: ")
base = int(input())
print("Informe o exponente: ")
exponente = int(input())

if exponente == 0:
    print("O resultado do cálculo de potência é: 1")
else:    
    total = base
    for i in range(1, exponente):
        total = total * base

    print("O resultado do cálculo de potência é: ", total)