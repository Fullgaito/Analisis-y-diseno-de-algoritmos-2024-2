from collections import deque
import time

def caminos_iterativo(i, j, p, q, n):
    # Matriz para almacenar los caminos posibles
    dp = [[[] for _ in range(n+1)] for _ in range(n+1)]
    
    if p > n or q > n:
        return []
    # Cola para el recorrido
    cola = deque([(i, j, [(i, j)])])

    while cola:
        x, y, camino = cola.popleft()

        # Si alcanzamos el punto objetivo, almacenamos el camino
        if (x, y) == (p, q):
            dp[x][y].append(camino)
        
        if x < 0 or y < 0 or x > n or y > n:
            continue

        # Movimientos posibles
        if x + 1 <= n:  # Movimiento hacia abajo
            cola.append((x + 1, y, camino + [(x + 1, y)]))
        if y + 1 <= n:  # Movimiento hacia la derecha
            cola.append((x, y + 1, camino + [(x, y + 1)]))
        if x - 1 >= 0 and y + 1 <= n:  # Movimiento diagonal
            cola.append((x - 1, y + 1, camino + [(x - 1, y + 1)]))

    return dp[p][q]

# Ejemplo de uso
n = 5
p, q = 1, 3

camino_resultado = caminos_iterativo(0, 0, p, q, n)

for k in camino_resultado:
    print(k)
print(f"El numero total de caminos es de {len(camino_resultado)} caminos")