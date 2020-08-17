'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer. 

'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.envelhecer_com_valor(1)
       
    def envelhecer_com_valor(self, soma_idade):
        self.idade = self.idade + soma_idade

    def engordar(self, novos_kg):
        self.peso = self.peso + novos_kg

    def emagrecer(self, novos_kg):
        self.peso = self.peso - novos_kg

    def crescer(self, tamanho):
        self.altura = self.altura + tamanho

print("*** ALTERAÇÕES NA VIDA DE UMA PESSOA ***")
pessoa = Pessoa("Tabata", 31, 58, 1.63)
pessoa.envelhecer()
pessoa.envelhecer_com_valor(10)
pessoa.engordar(2)
pessoa.emagrecer(3)
pessoa.crescer(0.05)

print(pessoa.nome)
print(pessoa.idade)
print(pessoa.peso)
print(pessoa.altura)