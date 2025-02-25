#complejidad temporal O(2^n)
#complejidad espacial O(2^n)


def generar_subconjuntos(arr):
    """Genera todos los subconjuntos de un conjunto dado de manera iterativa."""
    subconjuntos = [[]]  # Comenzamos con el subconjunto vacío

    for num in arr:
        # Generamos nuevos subconjuntos agregando el número actual a los existentes
        nuevos_subconjuntos = [sub + [num] for sub in subconjuntos]
        subconjuntos.extend(nuevos_subconjuntos)

    return subconjuntos

def subset_sum_divide_and_conquer(arr, M):
    if not arr:
        return []
    
    # Dividimos el conjunto en dos mitades
    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]
    
    # Generamos todos los subconjuntos posibles de cada mitad
    left_subsets = generar_subconjuntos(left_part)
    right_subsets = generar_subconjuntos(right_part)
    
    # Filtramos los subconjuntos cuya suma sea exactamente M
    valid_subsets = [list(subset) for subset in left_subsets + right_subsets if sum(subset) == M]
    
    # Combinamos subconjuntos de la izquierda con los de la derecha y verificamos si suman M
    for left in left_subsets:
        for right in right_subsets:
            combined = left + right
            if sum(combined) == M:
                valid_subsets.append(list(combined))
    
    return valid_subsets

# Ejemplo de uso
arr = [1, 3, 5, 6, 7]
M = 15
solutions = subset_sum_divide_and_conquer(arr, M)
print(solutions)
