from main import Produto;
from dataclasses import is_dataclass
import pytest

@pytest.fixture
def produto():
    return Produto(1,"teste",15.0,10)

#teste para classe construtor
def teste_constructor(produto):

    assert produto.id == 1
    assert produto.nome == "teste"
    assert produto.preco == 15.0
    assert produto.estoque == 10

#testando a função de verificação do número positivo
def teste_verificar_numero_positivo(produto):
    with pytest.raises(Exception) as assert_error:
        produto.verificar_numero_positivo(-1)
    assert assert_error.value.args[0] == "O número deve ser positivo"

#testando o aumento de estoque
def teste_aumentar_estoque(produto):
    produto.aumentar_estoque(10)
    assert produto.estoque == 20

#testando diminuição do estoque
def teste_diminua_estoque(produto):
    produto.diminuir_estoque(8)
    assert produto.estoque == 2

#testando a diminuição do preço
def teste_atualizando_preço(produto):
    produto.diminuir_preco(5)
    assert produto.preco == 10

def teste_verificar_estoque_negativo(produto):
    with pytest.raises(Exception) as assert_error:
        produto.diminuir_estoque(11)
    assert assert_error.value.args[0] == "O estoque deve ser maior ou igual a 0"
