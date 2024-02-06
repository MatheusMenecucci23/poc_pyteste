## Engenharia de Software 1 - POC PYTEST
Esse reposítório foi criado para os estudos de teste em python na disciplina de Engenharia de Software 1

Para conseguir rodar os testes instale:
```
pip install pytest
```
Para rodar os teste utilize o comando:
```
 pytest main_teste.py
```
Em caso de falha utilize:
```
python -m pytest main_teste.py
``` 
Fiz uma classe de produtos, onde existe a possibilidade de diminuir o estoque, aumentar
estoque, diminuir preço, verifica um número positivo e verificar se o estoque está negativo.
Nos testes:
1. teste_constructor(produto):
 * Objetivo: Verificar se o construtor da classe Produto está atribuindo
corretamente os valores aos atributos.
 * Método: Compara os valores do objeto produto criado pelo fixture com os
valores esperados.
2. teste_verificar_numero_positivo(produto):
* Objetivo: Testar a função verificar_numero_positivo para garantir que ela
levanta uma exceção se um número não positivo for fornecido.
* Método: Chama verificar_numero_positivo com um número negativo e
verifica se a exceção esperada é levantada.
3. teste_aumentar_estoque(produto):
* Objetivo: Testar se o método aumentar_estoque aumenta corretamente a
quantidade em estoque.
* Método: Chama aumentar_estoque com um valor específico e verifica se o
estoque é ajustado conforme esperado.
4. teste_diminua_estoque(produto):
* Objetivo: Testar se o método diminuir_estoque diminui corretamente a
quantidade em estoque.
* Método: Chama diminuir_estoque com um valor específico e verifica se o
estoque é ajustado conforme esperado.
5. teste_atualizando_preço(produto):
* Objetivo: Testar se o método diminuir_preco atualiza corretamente o preço do
produto.
* Método: Chama diminuir_preco com um valor específico e verifica se o preço
é ajustado conforme esperado.
6. teste_verificar_estoque_negativo(produto):
* Objetivo: Testar se o método diminuir_estoque levanta uma exceção quando
a quantidade a ser diminuída é maior que o estoque.
* Método: Chama diminuir_estoque com uma quantidade maior que o estoque
atual e verifica se a exceção esperada é levantada.


Todos os testes passaram!
