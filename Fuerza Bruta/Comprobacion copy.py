from itertools import permutations
import time

def is_valid(board):
    if any(queen < 0 for queen in board):  # Verificar si hay índices negativos
        raise ValueError("Negative indices are invalid")

    n = len(board)
    # Validación de las reinas (verificar diagonales, filas, etc.)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def solve_eight_queens():
    """Encuentra todas las soluciones posibles al problema estándar de 8 reinas."""
    n = 8
    solutions = []
    total = 0
    for perm in permutations(range(n)):
        total += 1
        if is_valid(perm):
            solutions.append(perm)
    return solutions, total

def backtracking_eight_queens():
    """Resuelve el problema de las ocho reinas utilizando backtracking."""
    n = 8
    solutions = []
    total_checked = 0

    def valida(tabla, fila, columna):
        """Valida si es seguro colocar una reina en tabla[fila][columna]."""
        for i in range(fila):
            if tabla[i] == columna or abs(tabla[i] - columna) == abs(i - fila):
                return False
        return True

    def reinas(tabla, fila):
        """Encuentra todas las soluciones del problema de las N reinas."""
        nonlocal total_checked
        if fila == n:
            solutions.append(tabla[:]) 
            return
        for columna in range(n):
            total_checked += 1
            if valida(tabla, fila, columna):
                tabla[fila] = columna
                reinas(tabla, fila + 1)
                tabla[fila] = -1

    # Inicialización
    tabla = [-1] * n
    reinas(tabla, 0)

    return solutions, total_checked


start_time = time.time()
brute_force_solutions, brute_force_checked = solve_eight_queens()
brute_force_time = time.time() - start_time


start_time = time.time()
backtracking_solutions, backtracking_checked = backtracking_eight_queens()
backtracking_time = time.time() - start_time


print("Fuerza Bruta:")
print(f"Soluciones encontradas: {len(brute_force_solutions)}")
print(f"Configuraciones posibles: {brute_force_checked}")
print(f"Tiempo tomado: {brute_force_time:.6f} seconds")

print()
print("Backtracking:")
print(f"Soluciones encontradas: {len(backtracking_solutions)}")
print(f"Configuraciones posibles: {backtracking_checked}")
print(f"Tiempo tomado: {backtracking_time:.6f} seconds")
