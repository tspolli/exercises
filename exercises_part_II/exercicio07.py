'''
Faça um programa que leia e crie um terceiro arquivo.

O primeiro arquivo contem o código do cliente, nome e cpf, ex:
123;Raquel Sara Fernandes;767.712.384-82
456;Luiz Caio Viana074.943.930-05
789;Benjamin Joaquim Antonio Santos483.911.114-66

O segundo arquivo contem o código do cliente, endereço e telefone, ex:
789;Quadra SQN 209 Bloco H, Brasília - DF; (61) 2928-7715
123;Alameda Maria Doralice, 619, Fortaleza - CE;(85) 2564-7844
456;Beco Luiz Simões, 148, Rio de Janeiro - RJ;(21) 99427-2234

O arquivo de saída deverá juntar as informações do mesmo cliente em uma unica linha, ex:
123;Raquel Sara Fernandes;767.712.384-82;Alameda Maria Doralice, 619, Fortaleza - CE;(85) 2564-7844
456;Luiz Caio Viana074.943.930-05;Beco Luiz Simões, 148, Rio de Janeiro - RJ;(21) 99427-2234
789;Benjamin Joaquim Antonio Santos483.911.114-66;Quadra SQN 209 Bloco H, Brasília - DF; (61) 2928-7715
'''

arquivo_1 = open("dados_cliente.txt", "r")
linhas_arq1 = arquivo_1.read()
print(linhas_arq1)
arquivo_2 = open("dados_cliente_2.txt", "r")
linhas_arq2 = arquivo_2.read()
print(linhas_arq2)
linhas_arq1_separada = linhas_arq1.split("\n")
linhas_arq2_separada = linhas_arq2.split("\n")
cod_cliente_arq1 = []
cod_cliente_arq2 = []

for i in linhas_arq1_separada:
    cod_cliente_arq1.append(i[:3])
    
    
for i in linhas_arq2_separada:
    cod_cliente_arq2.append(i[:3])

while cod_cliente_arq1 != 1 or cod_cliente_arq2:
    if cod_cliente_arq1 == cod_cliente_arq2:
        arquivo_3 = open("dados_cliente_consolidade.txt", "w", encoding= "utf8")
        arquivo_3.write("" 

