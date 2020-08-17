'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e função que:
No mínimo esses atributos:
    tipoCombustivel.
    valorLitro
    quantidadeCombustivel
Possua no mínimo essas funções:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de 
litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o 
valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível 
total na bomba.
'''

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        total = valor / self.valorLitro
        self.quantidadeCombustivel = self.quantidadeCombustivel - total
        return total

    def abastecerPorLitro(self, qtd_litros):
        total = self.valorLitro * qtd_litros
        self.quantidadeCombustivel = self.quantidadeCombustivel - qtd_litros
        return total

    def alterarValor(self, novoValorLitro):
        self.valorLitro = novoValorLitro

    def alterarCombustivel(self, novoTipoCombustivel):
        self.tipoCombustivel = novoTipoCombustivel
    
    def alterarQuantidadeCombustivel(self, novaQuantidadeCombustivel):
        self.quantidadeCombustivel = self.quantidadeCombustivel - novaQuantidadeCombustivel
    
print("*** BOMBA DE COMBUSTIVEL ***")
bombaCombustivel = BombaCombustivel("Gasolina", 4.15, 1000)
bombaCombustivel.alterarCombustivel("Etanol")
bombaCombustivel.alterarValor(4.10)
quantidadeCombustivel = bombaCombustivel.abastecerPorValor(20.00)
total = bombaCombustivel.abastecerPorLitro(15)

print("A quantidade de litros de combustível colocado no carro foi de: ", "{0:.2f}".format(quantidadeCombustivel))
print("O valor a ser pago é de: R$", "{0:.2f}".format(total))
print("A quantidade de combustível restante na bomba é de: ", "{0:.2f}".format(bombaCombustivel.quantidadeCombustivel))