'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 999 e imprima-o na tela por extenso.
'''

print("*** NUMERO POR EXTENSO ***")
print("Informe um número até 999: ")
numero = int(input())

unidade = {
    0:"zero",
    1:"um",
    2:"dois",
    3:"três",
    4:"quatro",
    5:"cinco",
    6:"seis",
    7:"sete",
    8:"oito",
    9:"nove"
}

dezena = {
    10:"dez",
    11:"onze",
    12:"doze",
    13:"treze",
    14:"quatorze",
    15:"quinze",
    16:"dezesseis",
    17:"dezessete",
    18:"dezoito",
    19:"dezenove",
    20:"vinte",
    30:"trinta",
    40:"quarenta",
    50:"cinquenta",
    60:"sessenta",
    70:"setenta",
    80:"oitenta",
    90:"noventa",
}

centena = {
    100:"cem",
    200:"duzentos",
    300:"trezentos",
    400:"quatrocentos",
    500:"quinhentos",
    600:"seiscentos",
    700:"setecentos",
    800:"oitocentos",
    900:"novecentos",
}

numero_string = str(numero)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10

if numero < 0 or numero > 999:
    print("Informe um número a partir de 0 e menor ou igual a 999!")
else:
    if len(numero_string) == 1:
        print(unidade[numero])
    elif len(numero_string) == 2:
        if d == 1:
            print(dezena[numero])
        elif d != 1 and u == 0:
            print(dezena[numero])
        elif d != 1 and u != 0:
            mult_d = d * 10
            print(dezena[mult_d], "e", unidade[u])   
    elif len(numero_string) == 3:
        if c != 0 and d == 0 and u == 0:
            print(centena[numero])
        elif c == 1 and d == 0 and u != 0:
            mult_c = c * 100
            print("cento e", unidade[u])
        elif c == 1 and d != 0 and u == 0:
            mult_c = c * 100
            mult_d = d * 10
            print("cento e", dezena[mult_d])
        elif c == 1 and d == 1:
            mult_d = str(d) + str(u)
            print("cento e", dezena[int(mult_d)])
        elif c == 1 and d != 0 and d != 1:
            mult_d = d * 10
            print("cento e", dezena[mult_d], unidade[u])
        elif c != 0 and d == 0 and u == 0:
            print(centena[numero])
        elif c != 0 and c != 1 and d == 0 and u != 0:
            mult_c = c * 100
            print(centena[mult_c], "e", unidade[u])
        elif c != 0 and c != 1 and d != 0 and u == 0:
            mult_c = c * 100
            mult_d = d * 10
            print(centena[mult_c], "e", dezena[mult_d])
        elif c != 0 and c != 1 and d == 1:
            mult_c = c * 100
            mult_d = str(d) + str(u)
            print(centena[mult_c], "e", dezena[int(mult_d)])
        elif c != 0 and c != 1 and d != 0 and d != 1:
            mult_c = c * 100
            mult_d = d * 10
            print(centena[mult_c], "e", dezena[mult_d], "e",  unidade[u])