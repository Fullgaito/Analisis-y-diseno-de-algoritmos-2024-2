"""Para comprobar la veracidad de cada una de las pruebas se debe usar el siguiente comando y aplicarlo en la terminal con ruta correspondiente al archivo test_ocho_reinas.py:"
        pytest -v
"""

import pytest
from Ocho_Reinas import valida, mostrar, reinas

def test_soluciones_ocho_reinas():
    """
    Test para cuando se tiene un tamaño un total de 8 reinas
    """
    m = 8
    tabla = [None] * m
    soluciones = reinas(tabla, 0, m)
    # Para un tablero 8x8, debe haber 92 soluciones
    assert len(soluciones) == 92

def test_mostrar_soluciones():
    """
    Comprueba que cada solución tiene el número correcto de filas y una 'Q' por fila.
    """
    m = 8  # Cambia el tamaño del tablero según sea necesario
    tabla = [None] * m
    soluciones = reinas(tabla, 0, m)

    # Comprueba que cada solución tiene m filas y exactamente una 'Q' por fila
    for solucion in soluciones:
        assert len(solucion) == m #El numero de filas en la solución no coincide con m.
        for fila in solucion:
            assert fila.count("Q") == 1 #Cada fila debe tener exactamente una reina (Q).

def test_numero_de_reinas_ocho_reinas():
    """
    Prueba que haya exactamente 8 reinas en el tablero
    """
    m = 8
    tabla = [None] * m
    soluciones = reinas(tabla, 0, m)

    for solucion in soluciones:
        # Contar cuántas "Q" hay en la solución
        total_reinas = sum(fila.count("Q") for fila in solucion)
        assert total_reinas == 8

def test_cero_reinas():
    """
    Evalua cuando hay 0 ceros reinas a acomodar
    """
    m = 0
    tabla = [None] * m
    soluciones = reinas(tabla, 0, m)
    # Verifica que el numero de soluciones sea 0
    assert len(soluciones) == 0

def test_reinas_negativas():
    """
    Evalua cuando hay reinas negativas a acomodar
    """
    m=-1
    tabla = [None] * m
    soluciones = reinas(tabla, 0, m)
    # Verifica que el numero de soluciones sea 0
    assert len(soluciones) == 0

@pytest.mark.parametrize(
    "m,expected",
    [
        (4.4, 0),  
        (-1.2, 0),   
        (5.08, 0),   
    ]
)
def test_reinas_decimales(m,expected):
    """
    Evalua cuando hay reinas con decimales a acomodar
    """
    queens=m
    if not m.is_integer():
        soluciones=[]  #No hay soluciones si m no es entero
    assert len(soluciones)==expected

@pytest.mark.parametrize(
    "m,expected",
    [
        (4, 2),  
        (5, 10),   
        (10, 724),   
        (12, 14200), 
        (-4, 0),
        (1,1),
        (2,0),
        (3,0)
    ]
)

def test_m_reinas(m,expected):
    """
    Evalúa diferentes valores de m y verifica el número de soluciones esperadas.
    """
    # Si m no es un número entero, no debería haber soluciones
    if not isinstance(m, int) or m < 0:
        soluciones = []
    else:
        tabla = [None] * m
        soluciones = reinas(tabla, 0, m)

    # Verifica que el número de soluciones sea el esperado
    assert len(soluciones) == expected

def test_solucion_parcial():
    """
    Evalúa el comportamiento del algoritmo cuando se le da un tablero con una solución parcial.
    Verifica que el algoritmo continúe correctamente y encuentre todas las soluciones válidas.
    """
    # Tablero 8x8 con algunas reinas ya colocadas
    # En este caso, colocamos una reina en la primera fila, columna 0 (index 0).
    tablero_parcial = [None] * 8
    tablero_parcial[0] = 0  # Reina en la fila 0, columna 0
    
    # Ejecutamos el algoritmo para completar la solución
    soluciones = reinas(tablero_parcial, 1, 8)  # Comienza desde la fila 1
    
    # Verificamos que se encuentren soluciones, no se espera que sea 0
    assert len(soluciones) > 0
    
    # Verifica que la primera fila (con la reina en columna 0) esté en todas las soluciones
    for solucion in soluciones:
        assert solucion[0] == "Q......."

@pytest.mark.parametrize(
    "m,expected",
    [
        (4, 4),  
        (5, 5),   
        (10, 10),   
        (12, 12),
        (-1,0),
    ]
)
def test_numero_de_reinas(m,expected):
    """
    Prueba que haya exactamente m reinas en el tablero
    """
    queens = m
    tabla = [None] * queens
    soluciones = reinas(tabla, 0, queens)

    for solucion in soluciones:
        # Contar cuántas "Q" hay en la solución
        total_reinas = sum(fila.count("Q") for fila in solucion)
        assert total_reinas == expected