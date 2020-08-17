'''
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data 
com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973.
'''

print("*** CALENDARIO ***")
print("Informe a data de nascimento (dd/mm/aaaa): ")
data_nascimento = str(input())
dt_nasc_separado = data_nascimento.split("/")

if dt_nasc_separado[1] == "01":
    print("Você nasceu em ", dt_nasc_separado[0], " de Janeiro de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "02":
    print("Você nasceu em ", dt_nasc_separado[0], " de Fevereiro de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "03":
    print("Você nasceu em ", dt_nasc_separado[0], " de Março de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "04":
    print("Você nasceu em ", dt_nasc_separado[0], " de Abril de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "05":
    print("Você nasceu em ", dt_nasc_separado[0], " de Maio de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "06":
    print("Você nasceu em ", dt_nasc_separado[0], " de Junho de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "07":
    print("Você nasceu em ", dt_nasc_separado[0], " de Julho de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "08":
    print("Você nasceu em ", dt_nasc_separado[0], " de Agosto de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "09":
    print("Você nasceu em ", dt_nasc_separado[0], " de Setembro de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "10":
    print("Você nasceu em ", dt_nasc_separado[0], " de Outubro de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "11":
    print("Você nasceu em ", dt_nasc_separado[0], " de Novembro de", dt_nasc_separado[2])
elif dt_nasc_separado[1] == "12":
    print("Você nasceu em ", dt_nasc_separado[0], " de Dezembro de", dt_nasc_separado[2])