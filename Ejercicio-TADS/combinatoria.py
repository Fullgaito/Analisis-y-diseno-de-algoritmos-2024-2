"""A partir de una lista de 13 candidatos a entrar a una empresa,se elegirán únicamente
5 de ellos para formar un equipo de trabajo ¿Cuántos equipos se pueden formar?"""


candidatos = ['Sergio', 'Andres', 'Valentina', 'Camila', 
              'Mariana', 'Daniel', 'Carlos', 'Jairo']
def generar_combinaciones(candidatos, k):
    n = len(candidatos)
    indices = list(range(k))
    while True:
        combinacion = [candidatos[i] for i in indices]
        cont=1
        print(combinacion)
        for i in reversed(range(k)):
            if indices[i] != i + n - k:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1
print("Equipos posibles de 5 candidatos:")
generar_combinaciones(candidatos, 5)

