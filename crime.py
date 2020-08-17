'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
como "Inocente".
'''

print("*** CRIME ***")
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas_verdadeiras = 0

for pergunta in perguntas:
    print(pergunta)
    print("Informe sua resposta: [Y/N]")
    resposta = input()
    if resposta == 'Y':
        respostas_verdadeiras = respostas_verdadeiras + 1
else:
    print("Sem mais perguntas!")
    
if respostas_verdadeiras == 2:
    print("Suspeito")
elif respostas_verdadeiras >=3 and respostas_verdadeiras <= 4:
    print("Cumplice")
elif respostas_verdadeiras >= 5:
    print("Assassino")
else:
    print("Inocente")
