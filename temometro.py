'''
Faça um Programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''

print("** CALCULO DE FARENHEIT PARA CELSIUS **")
print("Informe a temperatura em graus Farenheit: ")
graus_farenheit = int(input())
graus_celsius = 5*(graus_farenheit-32)/9
print("Graus Celsius: ", graus_celsius)
print("Pressione enter para finalizar...")
enter = str(input())

