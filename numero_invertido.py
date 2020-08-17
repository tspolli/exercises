'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489 => 98467321
'''

print("*** NUMERO INVERTIDO ***")
print("Informe um número inteiro e positivo: ")
num_inteiro = list(input())
numero = ""

num_invertido = numero
for numero in reversed(num_inteiro):
  num_invertido = num_invertido + numero

# num_invertido = int(str(num_inteiro)[::-1])
print("O número informado invertido é: ", num_invertido)