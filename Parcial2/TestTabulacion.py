import pytest
from Tabulacion import caminos_iterativo

def test_caminos_iterativo_base():
    "Test para cuando se inicia en (0,0) y se desea llegar a (0,0)"
    resultado = caminos_iterativo(0, 0, 0, 0, 3)
    assert len(resultado) == 1 

def test_caminos_iterativo_fuera_de_limites():
    "Test para cuando se pretende evaluar estando fuera de los limites"
    resultado = caminos_iterativo(-1, 0, 2, 2, 3)
    assert len(resultado) == 0

def test_caminos_iterativo_no_llega():
    "Test para cuando el valor de n es menor al camino donde se desea llegar"
    resultado = caminos_iterativo(0, 0, 5, 5, 3)
    assert len(resultado) == 0

def test_caminos_iterativo_validos():
    "Test para evaluar que se llega a un camino valido"
    resultado = caminos_iterativo(0, 0, 1, 3, 5)
    # Verificamos que hay al menos un camino que lleva de (0, 0) a (1, 3)
    assert len(resultado) > 0
    # Verificamos que los caminos contienen el punto final (1, 3)
    assert all((1, 3) in camino for camino in resultado)