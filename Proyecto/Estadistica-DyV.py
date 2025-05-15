import time
import random
import numpy as np
import matplotlib.pyplot as plt

# 🔹 Algoritmo Divide y Vencerás
def subsetSum(arr, index, current_subset, comb_list, sum_list):
    if index == len(arr):
        comb_list.append(current_subset[:])
        sum_list.append(sum(current_subset))
        return

    current_subset.append(arr[index])
    subsetSum(arr, index + 1, current_subset, comb_list, sum_list)

    current_subset.pop()
    subsetSum(arr, index + 1, current_subset, comb_list, sum_list)

def calcSubsets(n, arr, x):
    arr1, arr2 = arr[:n // 2], arr[n // 2:]

    comb1, sums1 = [], []
    subsetSum(arr1, 0, [], comb1, sums1)

    comb2, sums2 = [], []
    subsetSum(arr2, 0, [], comb2, sums2)

    for i in range(len(sums1)):
        for j in range(len(sums2)):
            if sums1[i] + sums2[j] == x:
                pass  # Se omite print para no afectar tiempos

# 🔹 Prueba de rendimiento
def test_performance():
    sizes = list(range(2, 22, 2))  # Tamaños de prueba (de 2 a 20 en pasos de 2)
    num_trials = 10  # Más mediciones para mayor precisión
    stats = {}  # Guardará los resultados estadísticos
    all_times = []  # Lista para almacenar todos los tiempos por tamaño

    for size in sizes:
        times = []

        for _ in range(num_trials):
            arr = [random.randint(1, 20) for _ in range(size)]
            x = random.randint(5, 40)

            start_time = time.perf_counter()
            calcSubsets(size, arr, x)
            elapsed_time = (time.perf_counter() - start_time) * 1e6  # Convertimos a µs
            times.append(elapsed_time)

        # 📌 Cálculo de estadísticas
        mean_time = np.mean(times)
        variance_time = np.var(times)
        std_dev_time = np.std(times)

        stats[size] = {"mean": mean_time, "variance": variance_time, "std_dev": std_dev_time}
        all_times.append(times)  # Agregamos los tiempos de este tamaño

        print(f"Tamaño {size}: Promedio = {mean_time:.2f} µs, Varianza = {variance_time:.2f}, Desviación Estándar = {std_dev_time:.2f}")

    return stats, all_times, sizes

# 🔹 Graficar diagrama de cajas y bigotes con mejora en el eje Y
def plot_boxplot(all_times, sizes):
    """
    Genera un diagrama de cajas y bigotes para los tiempos de ejecución con mejor organización del eje Y.
    """
    plt.figure(figsize=(10, 6))

    # 📊 Diagrama de cajas y bigotes
    plt.boxplot(all_times, labels=sizes)

    plt.xlabel("Tamaño del Conjunto (n)")
    plt.ylabel("Tiempo de Ejecución (µs)")
    plt.yscale("log")  # 📌 Escala logarítmica para mejor organización en Y
    plt.title("Diagrama de Cajas y Bigotes: Tiempo vs Tamaño del Conjunto")
    plt.grid(True, linestyle="--", linewidth=0.5)

    # 📌 Rotamos etiquetas del eje X para mejor legibilidad
    plt.xticks(rotation=45)

    plt.show()

# 🔹 Ejecutar prueba y graficar
if __name__ == "__main__":
    stats, all_times, sizes = test_performance()
    plot_boxplot(all_times, sizes)
