'''
Dados dois strings (um contendo uma frase e outro contendo uma palavra), determine o número de vezes que a palavra ocorre na frase.

Exemplo:
Para a palavra: ANA 
e a frase : ANA E MARIANA GOSTAM DE BANANA
Temos que a palavra ocorre 4 vezes na frase. (ANA e mariANA gostam de bANANA)
'''

print("*** FRASE VS. PALAVRA ***")
print("Digite uma frase: ")
frase = str(input())
print("Digite uma palavra que deseja saber quantas vezes ocorre na frase: ")
palavra = str(input())
contador = 0
index = 0
retorno = 0

while retorno != -1:
    retorno = frase.find(palavra, index, len(frase))
    index = retorno + 1
    if retorno != -1:
        contador = contador + 1
print("Temos que a palavra ocorre", contador, "vez(es) na frase.")
