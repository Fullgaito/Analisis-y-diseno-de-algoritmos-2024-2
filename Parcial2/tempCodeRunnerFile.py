def caminos_tab(n, p, q):
    # Crear una tabla de tamaño (n+1) x (n+1) para almacenar los caminos
    tabla = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    
    # El destino (p, q) es un caso base: el único camino es el propio destino
    tabla[p][q] = [[(p, q)]]
    
    # Llenar la tabla desde el destino hacia el origen
    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            if (i, j) == (p, q):  # Ya hemos establecido el destino
                continue

            # Almacenar los caminos posibles desde (i, j)
            caminos_posibles = []
            
            # Mover hacia abajo
            if i + 1 <= n:
                for camino in tabla[i + 1][j]:
                    caminos_posibles.append([(i, j)] + camino)
            
            # Mover hacia la derecha
            if j + 1 <= n:
                for camino in tabla[i][j + 1]:
                    caminos_posibles.append([(i, j)] + camino)
            
            # Mover hacia la diagonal (abajo-izquierda)
            if i - 1 >= 0 and j + 1 <= n:
                for camino in tabla[i - 1][j + 1]:
                    caminos_posibles.append([(i, j)] + camino)

            # Asignar los caminos posibles a la celda
            tabla[i][j] = caminos_posibles

    return tabla[0][0]  # Devolver los caminos desde (0, 0) hasta (p, q)

# Ejemplo de uso
n = 5
p, q = 1, 3
caminos_resultado = caminos_tab(n, p, q)
for camino in caminos_resultado:
    print(camino)
print(len(caminos_resultado))