from validacao import validar_produto

CATEGORIAS = {1, 2, 3}  # ids de categorias válidos

# testar um preço válido
dados, erros =validar_produto(
    {"nome":"Produto A", "preco": "10.0", "estoque": "5", "id_categoria": "1"},
    CATEGORIAS,
)
assert erros == {}, "Não deveria haver erros"
assert dados == {"nome": "Produto A", "preco": 10.0, "estoque": 5, "id_categoria": 1}


# Testar com preço negativo
dados, erros = validar_produto(
    {"nome":"Produto B", "preco": "-5.0", "estoque": "10", "id_categoria": "2"},
    CATEGORIAS,
)
assert dados is None
assert "preco" in erros

# Testar com nome vazio
dados, erros = validar_produto(
    {"nome":"", "preco": "10.0", "estoque": "5", "id_categoria": "1"},
    CATEGORIAS,
)
assert dados is None
assert "nome" in erros

print("Todos os testes passaram com sucesso!")
