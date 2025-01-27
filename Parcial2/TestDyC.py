import pytest
from DivideVenceras import caminos

def test_caminos_base():
    "Test para cuando se inicia en (0,0) y se desea llegar a (0,0)"
    resultado = caminos(0, 0, 0, 0, 3)
    assert len(resultado) == 1 

def test_caminos_fuera_de_limites():
    "Test para cuando se pretende evaluar estando fuera de los limites"
    resultado = caminos(-1, 0, 2, 2, 3)
    assert len(resultado) == 0

def test_caminos_no_llega():
    "Test para cuando el valor de n es menor al camino donde se desea llegar"
    resultado = caminos(0, 0, 5, 5, 3)
    assert len(resultado) == 0

def test_caminos_validos():
    "Test para evaluar que se llega a un camino valido"
    resultado = caminos(0, 0, 2, 2, 3)
    # Verificamos que hay al menos un camino que lleva de (0, 0) a (2, 2)
    assert len(resultado) > 0
    # Verificamos que los caminos contienen el punto final (2, 2)
    assert all((2, 2) in camino for camino in resultado)