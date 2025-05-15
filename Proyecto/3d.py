import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# 🔹 Función de Programación Dinámica
def ProgramacionDP(n, m):
    dp = [[] for _ in range(m + 1)]
    dp[0] = [[]]

    for num in n:
        for j in range(m, num - 1, -1):
            for prev in dp[j - num]:
                dp[j].append(prev + [num])

    return dp[m]

# 🔹 Función para medir el tiempo de ejecución
def medir_tiempo(n, m):
    inicio = time.time()
    ProgramacionDP(n, m)
    fin = time.time()
    return fin - inicio

# 🔹 Generar datos
n_values = np.arange(1, 20)  # Tamaño del conjunto (n)
m_values = np.arange(1, 50, 2)  # Sumas objetivo (m)
tiempos = np.zeros((len(n_values), len(m_values)))  # Matriz para almacenar tiempos

for i, n in enumerate(n_values):
    for j, m in enumerate(m_values):
        conjunto_n = np.random.randint(1, 10, size=n)  # Generar conjunto aleatorio
        tiempos[i, j] = medir_tiempo(conjunto_n, m)  # Medir tiempo

# 🔹 Crear gráfica 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 📌 Crear malla para `n` y `m`
n_mesh, m_mesh = np.meshgrid(n_values, m_values)

# 📌 Graficar superficie 3D en lugar de puntos
ax.plot_surface(n_mesh, m_mesh, tiempos.T, cmap="viridis", alpha=0.8)

# 📌 Etiquetas
ax.set_xlabel('Tamaño del conjunto (n)')
ax.set_ylabel('Suma objetivo (m)')
ax.set_zlabel('Tiempo de ejecución (s)')
ax.set_title('Superficie 3D: Tiempo de Ejecución vs n y m')

plt.show()
