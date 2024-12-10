def dijkstra(L):
    n=len(L)
    C=list(range(1,n))
    P=[-1]*n
    D=[-1]*n
    for x in range(n):
        D[x]=L[0][x]
    for veces in range(n-2):
        v=minimiza(C,D)
        C.remove(v)
        for w in C:
            if D[w]>D[v]+L[v][w]:
                D[w]=D[v]+L[v][w]
                P[w]=v
    return D
def minimiza(C,D):
    min=float("inf")
    pos=-1
    for x in C:
        if D[x]<min:
            min=D[x]
            pos=x
    return pos

L = [
    [0, 3, 5, 6, float('inf'), float('inf'), float('inf'), float('inf')],
    [3, 0, 1, float('inf'), 5, float('inf'), float('inf'), float('inf')],
    [5, 1, 0, 2, 2, 1, float('inf'), float('inf')],
    [6, float('inf'), 2, 0, float('inf'), 2, 2, float('inf')],
    [float('inf'), 5, 2, float('inf'), 0, 1, 4, 3],
    [float('inf'), float('inf'), 1, 2, 1, 0, 2, 8],
    [float('inf'), float('inf'), float('inf'), 2, 4, 2, 0, 1],
    [float('inf'), float('inf'), float('inf'), float('inf'), 3, 8, 1, 0]
]


distancias = dijkstra(L)


print("Distancias desde el nodo central a:", distancias)
