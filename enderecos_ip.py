'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP 
e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4
[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''

print("*** LEITURA/VALIDAÇÃO ARQUIVOS ENDEREÇOS IP ***")
ips_invalidos = [] 
ips_validos = []
arquivo_todos_ips = open("endereco_ip.txt", "r")
for linha in arquivo_todos_ips:
    print(linha)

    blocos = linha.split(".")
    contador_invalidos = 0
    for bloco in blocos:
        if int(bloco) < 0 or int(bloco) > 255:
            contador_invalidos = contador_invalidos + 1
    
    if contador_invalidos > 0:
        ips_invalidos.append(linha)
    else:
        ips_validos.append(linha)

arquivo_ips_validados = open("enderecos_ip_validados.txt", "w")
arquivo_ips_validados.write("[Endereços válidos:] \n")
for ip in ips_validos:
    arquivo_ips_validados.write(ip)

arquivo_ips_validados.write("[Endereços inválidos:] \n")
for ip in ips_invalidos:
    arquivo_ips_validados.write(ip)

arquivo_ips_validados.close()  
arquivo_todos_ips.close()