

# testar preço válido
import pytest

from validacao import validar_produto

CATEGORIAS = {1, 2, 3}  # ids de categorias válidos

def campos_validos(**alteracoes):
    campos = {
        "nome": "Mouse sem fio",
        "preco": "49,90",
        "estoque": "20",
        "id_categoria": "1"        
    }
    campos.update(alteracoes)
    return campos

@pytest.mark.parametrize(
    "campo, valor",
    [
        ("preco", "-5"),
        ("preco", "-0.01"),
        ("preco", "abc"),
        ("estoque", "-1"),
        ("estoque", "abc"),
        ("nome", ""),
        ("nome", "a" * 101),
        ("id_categoria", "999"),  # categoria inválida
    ],
)
def test_entradas_invalidas_sao_recusadas(campo, valor):
    dados, erros = validar_produto(campos_validos(**{campo: valor}), CATEGORIAS)

    assert dados is None
    assert campo in erros
