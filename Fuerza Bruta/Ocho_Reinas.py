
def valida(tabla, fila, columna,m):
    """Valida si es seguro colocar una reina en tabla[fila][columna]."""
    for i in range(fila):
        if tabla[i] == columna or abs(tabla[i] - columna) == abs(i - fila):
            return False
    return True

def mostrar(tabla, m):
    """Construye una representación de la solución."""
    solucion = []
    for j in range(m):
        fila = ["."] * m
        fila[tabla[j]] = "Q"
        solucion.append("".join(fila))
    return solucion

def reinas(tabla, n, m):
    """Encuentra todas las soluciones del problema de las N reinas."""
    if m==0:
        return []
    soluciones = []
    if n == m:
        soluciones.append(mostrar(tabla, m))  # Agrega la solución actual
    else:
        for x in range(m):
            tabla[n] = x
            if valida(tabla, n, x, m):
                soluciones.extend(reinas(tabla, n + 1, m))
            tabla[n] = None
    return soluciones
  

# Ejecución del algoritmo
m = 8
tabla = [None] * m
soluciones = reinas(tabla, 0, m)

# Imprime las soluciones
for i, solucion in enumerate(soluciones, 1):
    print(f"Solución {i}:")
    for fila in solucion:
        print(fila)
    print()
