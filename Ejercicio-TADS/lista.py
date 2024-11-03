articulos=3
sucursales=4

precios=[
    [10,12,11,9],
    [20,22,21,19],
    [30,32,31,29]
]

cantidades_vendidas=[
    [5,3,6,4],
    [7,2,8,3],
    [9,4,5,6]
]

ventas_totales_articulo=[0]*articulos
ventas_totales_sucursal=[0]*sucursales

for i in range(articulos):
    for j in range(sucursales):
        venta=precios[i][j]*cantidades_vendidas[i][j]
        ventas_totales_articulo[i]+=venta
        ventas_totales_sucursal[j]+=venta
for i in range(articulos):
    print(f"Articulo {i+1}:{ventas_totales_articulo[i]}")
for j in range(sucursales):
    print(f"Sucursal:{j+1}:{ventas_totales_sucursal[j]}")