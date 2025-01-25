import time

def caminos(i, j, p, q, n, memo):
    # Verificamos si ya se calculó el valor para esta celda
    if (i, j) in memo:
        return memo[(i, j)]

    # Caso base: si hemos llegado al destino
    if i == p and j == q:
        return [[(i, j)]]

    # Si estamos fuera del rango, no hay caminos posibles
    if i > n or j > n or i < 0 or j < 0:
        return []

    # Si estamos en una celda ya visitada, no calculamos nuevamente
    todos_los_caminos = []

    # Explorar las direcciones disponibles
    if i + 1 <= n:
        todos_los_caminos.extend(caminos(i + 1, j, p, q, n, memo))

    if j + 1 <= n:
        todos_los_caminos.extend(caminos(i, j + 1, p, q, n, memo))

    if i - 1 >= 0 and j + 1 <= n:
        todos_los_caminos.extend(caminos(i - 1, j + 1, p, q, n, memo))

    # Guardar el resultado en el memo y devolverlo
    memo[(i, j)] = [[(i, j)] + camino for camino in todos_los_caminos]
    
    return memo[(i, j)]

# Ejemplo de uso
n = 5
p, q = 1, 3
memo = {}

start_time = time.time()
resultados = caminos(0, 0, p, q, n, memo)
tiempo_ejecucion = time.time() - start_time

print(f"El número de caminos desde <0,0> hasta <{p, q}> son {len(resultados)}")
for camino in resultados:
    print(camino)
print(f"De esta forma para llegar desde <0,0> hasta <{p, q}> hay {len(resultados)} caminos en {tiempo_ejecucion}")
