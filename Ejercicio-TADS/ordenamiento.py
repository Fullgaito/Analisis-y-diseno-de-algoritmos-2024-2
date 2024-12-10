"""Una cadena de almacenes tiene sucursales en cuatro ciudades diferentes y un total de N empleados.El registro preparado para cada empleado
tiene los siguientes campos:nombre,ciudad,código.Los datos de los clientes están en vectores paralelos.
Diseñar un algoritmo que ordene todos los datos de los empleados de modo que se pueda visualizar,por sucursal,la lista de los empleados en orden alfabético creciente."""

def burbuja(nombres, indices):
    n = len(indices)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nombres[indices[j]] > nombres[indices[j + 1]]:
                indices[j], indices[j + 1] = indices[j + 1], indices[j]
    return indices


nombres = ["Carlos", "Ana", "Luis", "Maria", "Andres", "Clara"]
ciudades = ["Bogota", "Medellin", "Bogota", "Cali", "Medellin", "Cali"]
codigos = [101, 102, 103, 104, 105, 106]


empleados_por_ciudad = {}
for i, ciudad in enumerate(ciudades):
    if ciudad not in empleados_por_ciudad:
        empleados_por_ciudad[ciudad] = []
    empleados_por_ciudad[ciudad].append(i)


for ciudad, indices in empleados_por_ciudad.items():
    empleados_por_ciudad[ciudad] = burbuja(nombres, indices)


for ciudad in sorted(empleados_por_ciudad.keys()):
    print(f"Empleados en {ciudad}:")
    for i in empleados_por_ciudad[ciudad]:
        print(f"Nombre: {nombres[i]}, Código: {codigos[i]}")
    print()  
