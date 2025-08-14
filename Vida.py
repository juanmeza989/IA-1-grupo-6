
import numpy as np
import matplotlib.pyplot as plt
import time

# Parámetros
filas, columnas = 50, 50
iteraciones = 200
velocidad = 0.1  # segundos entre pasos

# Estado inicial aleatorio
tablero = np.random.choice([0, 1], size=(filas, columnas))

# Configuración de gráfico
plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(tablero, cmap="binary")
ax.set_title("Juego de la Vida de Conway")

# Función para contar vecinos vivos
def contar_vecinos(tablero, x, y):
    vecinos = [
        tablero[(x-1) % filas, (y-1) % columnas],
        tablero[(x-1) % filas, y],
        tablero[(x-1) % filas, (y+1) % columnas],
        tablero[x, (y-1) % columnas],
        tablero[x, (y+1) % columnas],
        tablero[(x+1) % filas, (y-1) % columnas],
        tablero[(x+1) % filas, y],
        tablero[(x+1) % filas, (y+1) % columnas],
    ]
    return sum(vecinos)

# Simulación
for _ in range(iteraciones):
    nuevo_tablero = np.zeros((filas, columnas), dtype=int)
    for i in range(filas):
        for j in range(columnas):
            vivos = contar_vecinos(tablero, i, j)
            if tablero[i, j] == 1 and vivos in [2, 3]:
                nuevo_tablero[i, j] = 1
            elif tablero[i, j] == 0 and vivos == 3:
                nuevo_tablero[i, j] = 1
    tablero = nuevo_tablero

    img.set_data(tablero)
    plt.draw()
    plt.pause(velocidad)

plt.ioff()
plt.show()
