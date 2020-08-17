'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área
'''

class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def alterar_lado(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def area_quadrado(self):
        area = self.tamanho_lado * self.tamanho_lado
        return area

    def valor_lado(self):
        return self.tamanho_lado


print("*** CALCULO QUADRADO ***")
quadrado = Quadrado(10)
quadrado.alterar_lado(15)
area = quadrado.area_quadrado()
tamanho_lado = quadrado.valor_lado()
print("A área é: ", area)
print("O novo tamanho do lado é: ", tamanho_lado)