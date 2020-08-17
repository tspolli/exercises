'''
Uma frutaria está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) 
de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

print("*** FEIRA DE FRUTAS ***")
print("Informe a quantidade de kgs de morangos")
qtde_morangos = float(input())
print("Informe a quantidade de kgs de maçãs")
qtde_macas = float(input())
qtde_total_compra = qtde_morangos + qtde_macas
print("Quantidade da compra em kgs foi de: ", qtde_total_compra)

if qtde_morangos >= 5.0:
    valor_kg_morangos = 2.20
    valor_morangos = qtde_morangos * valor_kg_morangos
else:
    valor_kg_morangos = 2.50
    valor_morangos = qtde_morangos * valor_kg_morangos

if qtde_macas >= 5.0:
    valor_kg_macas = 1.50
    valor_macas = qtde_macas * valor_kg_macas
else:
    valor_kg_macas = 1.80
    valor_macas = qtde_macas * valor_kg_macas

valor_total_compra = valor_macas + valor_morangos

if qtde_total_compra > 8.0 or valor_total_compra > 25.00:
    valor_com_desconto = valor_total_compra- ((valor_total_compra*10)/100)
    print("O valor total da compra com desconto será de R$: ", valor_com_desconto)
else:
    print("O valor total da compra é de R$: ", valor_total_compra)