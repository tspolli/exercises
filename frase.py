'''
 Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

-Quantos espaços em branco existem na frase.
-Quantas vezes aparecem as vogais a, e, i, o, u.
'''

import unicodedata

def remove_non_ascii_normalized(string: str) -> str:
    normalized = unicodedata.normalize("NFD", frase)
    return normalized.encode("ascii", "ignore").decode("utf8").casefold()

print("*** CONTANDO CARACTERES EM UMA FRASE ***")
print("Informe uma frase: ")
frase = str(input())
frase_sem_acento = remove_non_ascii_normalized(frase)

print(len(frase))
print("Aparece a vogal a", frase_sem_acento.count("a"), "vezes")
print("Aparece a vogal e", frase_sem_acento.count("e"), "vezes")
print("Aparece a vogal i", frase_sem_acento.count("i"), "vezes")
print("Aparece a vogal o", frase_sem_acento.count("o"), "vezes")
print("Aparece a vogal u", frase_sem_acento.count("u"), "vezes")
print("Existem", frase_sem_acento.count(" "), "espaços em banco na frase")    
