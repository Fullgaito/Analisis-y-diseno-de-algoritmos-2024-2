#Divide y Venceras

def caminos(i, j, p, q, n, camino=[]):
    if i == p and j == q:
        return [camino + [(i, j)]]

    if i > n or j > n or i < 0 or j < 0 :
        return []

    todos_los_caminos = []

    if i + 1 <= n:
        todos_los_caminos.extend(caminos(i + 1, j, p, q, n, camino + [(i, j)]))

    if j + 1 <= n:
        todos_los_caminos.extend(caminos(i, j + 1, p, q, n, camino + [(i, j)]))

    if i - 1 >= 0 and j + 1 <= n:
        todos_los_caminos.extend(caminos(i - 1, j + 1, p, q, n, camino + [(i, j)]))

    return todos_los_caminos

# Ejemplo de uso
n = 5
p, q = 1, 3


resultados = caminos(0, 0, p, q, n, [])


print(f"El número de caminos desde <0,0> hasta <{p,q}> son {len(resultados)}")
for camino in resultados:
    print(camino)
print(f"De esta forma para llegar desde <0,0> hasta <{p,q}> hay {len(resultados)} caminos")