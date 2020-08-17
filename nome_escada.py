'''
Faça um programa que solicite o nome do usuário e imprima-o em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO
'''

print("*** NOME USUARIO EM ESCADA ***")
print("Informe o nome do usuário: ")
usuario = str(input()).upper()

for i in range(0, len(usuario)+1):
    print(usuario[:i])