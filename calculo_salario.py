'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
11% para o Imposto de Renda
8% para o INSS
5% para o sindicato, faça um programa que nos dê:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

print("*** CALCULO SALARIO ***")
print("Informe o valor da hora trabalhada: ")
horas_trabalhadas = float(input())
print("Informe o numero de horas trabalhadas no mês")
qtde_horas_trabalhadas = float(input())

salario_bruto = horas_trabalhadas*qtde_horas_trabalhadas
imposto_renda = (salario_bruto*11)/100
inss = (salario_bruto*8)/100
sindicato = (salario_bruto*5)/100
salario_liquido = salario_bruto-(imposto_renda+inss+sindicato)

print("Salário bruto: R$ ", salario_bruto)
print("Imposto de renda: R$ ", imposto_renda)
print("Salário INSS: R$ ", inss)
print("Salário sindicato: R$ ", sindicato)
print("Salário liquido: R$ ", salario_liquido)