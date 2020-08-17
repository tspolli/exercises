'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento      Conceito
  Entre 9.0 e 10.0               A
  Entre 7.5 e 9.0                B
  Entre 6.0 e 7.5                C
  Entre 4.0 e 6.0                D
  Entre 4.0 e zero               E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

print("*** BOLETIM ESCOLAR ***")

print("Informe nota parcial: ")
nota_parcial = float(input())
print("Informe nota parcial: ")
nota_parcial2 = float(input())

media_aproveitamento = (nota_parcial + nota_parcial2)/2    
print("Nota parcial: ", nota_parcial)
print("Nota parcial: ", nota_parcial2)
print(media_aproveitamento)

if media_aproveitamento >= 9.0 and media_aproveitamento <= 10.0:
    print("Conceito A")
    print("Aprovado")
elif media_aproveitamento >= 7.5 and media_aproveitamento <= 8.9:
    print("Conceito B")
    print("Aprovado")
elif media_aproveitamento >= 6.0 and media_aproveitamento <= 7.4:
    print("Conceito C")
    print("Aprovado")
elif media_aproveitamento >= 4.0 and media_aproveitamento <= 5.9:
    print("Conceito D")
    print("Reprovado")
elif media_aproveitamento >= 3.9 and media_aproveitamento <= 0.0:
    print("Conceito E")
    print("Reprovado")