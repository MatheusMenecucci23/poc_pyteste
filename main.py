from dataclasses import dataclass

@dataclass()
class Produto:

    id: int
    nome: str
    preco: float
    estoque: int

    def aumentar_estoque(self, estoque_adicional: int):
        self.verificar_numero_positivo(estoque_adicional)
        self.estoque: int = self.estoque + estoque_adicional
    
    def diminuir_estoque(self, estoque_a_reduzir):
        self.verificar_numero_positivo(estoque_a_reduzir)
        novo_estoque = self.estoque - estoque_a_reduzir
        self.verificar_estoque_negativo(novo_estoque)
        self.estoque = self.estoque - estoque_a_reduzir


    def diminuir_preco(self, valor_a_diminuir):
        self.verificar_numero_positivo(valor_a_diminuir)
        novo_preco = self.preco - valor_a_diminuir
        self.verificar_numero_positivo(novo_preco)
        self.preco -= valor_a_diminuir



    def verificar_numero_positivo(self, valor):
        if valor <= 0:
            raise Exception("O número deve ser positivo")

    def verificar_estoque_negativo(self, valor):
        if valor < 0:
            raise Exception("O estoque deve ser maior ou igual a 0")
