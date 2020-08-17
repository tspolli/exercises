'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no 
seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa 
saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. 
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, 
chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve 
criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
'''

print("*** SERVIDOR DE ARQUIVOS ***")

dicionario = {}
lista_usuarios = open("usuarios.txt", "r")

contador = 0
total_uso = 0
percentual_uso = 0
for linha in lista_usuarios:
    contador = contador + 1
    usuario = linha[:16]
    espaco_utilizado = linha[16:].strip("\n")
    espaco_utilizado_mb = (int(espaco_utilizado)/1024)/1024
    dicionario[usuario] = espaco_utilizado_mb
    total_uso = total_uso + espaco_utilizado_mb

lista_usuarios.close()

espaco_medio_ocupado = total_uso/contador

relatorio = open("relatório.txt", "w", encoding='utf8')
relatorio.write("ACME Inc.                      Uso do espaço em disco pelos usuários    \n")
relatorio.write("------------------------------------------------------------------------\n")
relatorio.write("Nr.         Usuário        Espaço utilizado     % do uso \n \n")

contador = 0
for usuario in dicionario:    
    contador = contador + 1
    percentual_uso = (dicionario[usuario]/total_uso)*100
    linha = str(contador).ljust(12) + usuario.ljust(16) + str("{0:.2f} MB".format(dicionario[usuario])).ljust(21) + str("{0:.2f}%".format(percentual_uso)) + "\n"
    relatorio.write(linha)

relatorio.write("\n\nEspaço total ocupado: {0:.2f} MB\n".format(total_uso))
relatorio.write("Espaço médio ocupado: {0:.2f} MB\n".format(espaco_medio_ocupado))
relatorio.close()