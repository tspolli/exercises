'''
Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto 
e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

from random import choice
print("*** JOGO DA FORCA ***")
palavras = open("palavras_jogo_forca.txt", "r")
palavras = palavras.read().split("\n")
palavra_escolhida = choice(palavras)
letras_separadas = list(palavra_escolhida)
tamanho = len(letras_separadas)
lista_letras_encontradas = [0]*tamanho
print("A palavra é: ", tamanho * "_ ")
print("\nDigite uma letra: ")
letra_digitada = str(input())
contador_erro = 0

#https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/#:~:text=Check%20if%20element%20exist%20in%20list%20using%20list.&text=count(element)%20function%20returns%20the,given%20element%20exists%20in%20list.
while contador_erro < 6 and lista_letras_encontradas.count(0) >= 1:
    letra_encontrada = False    
    contador = 0
    
    for letra in letras_separadas:
        if letra_digitada == letra:
            letra_encontrada = True
            lista_letras_encontradas[contador] = 1    
        contador += 1        
    
    linha = ""    
    if letra_encontrada == False:
        contador_erro = contador_erro + 1
        print("Você errou pela", contador_erro, "ª vez. Tente de novo!")
    
        if contador_erro < 6:        
            for i in range(len(lista_letras_encontradas)):
                if lista_letras_encontradas[i] == 0:
                    linha = linha + "_ "
                else:
                    linha = linha + letras_separadas[i] + " "
            print(linha) 
            print("Digite uma letra: ")
            letra_digitada = str(input())
        else:
            print("Você foi enforcado!")
    else:
        for i in range(len(lista_letras_encontradas)):
            if lista_letras_encontradas[i] == 0:
                linha = linha + "_ "
            else:
                linha = linha + letras_separadas[i] + " "
        print(linha)
        if 0 in lista_letras_encontradas:
            print("Digite uma letra: ")
            letra_digitada = str(input())