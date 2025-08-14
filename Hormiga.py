import matplotlib.pyplot as plt

# Definición de movimientos: N, E, S, O
movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Estado inicial
x, y = 0, 0
direccion = 0  # 0=N, 1=E, 2=S, 3=O
celdas = {}    # Diccionario: (x, y) -> 0 (blanco) o 1 (negro)

# Parámetros de simulación
iteraciones = 2000
limite = 50
velocidad = 0.001

# Configuración gráfica
plt.ion()
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.set_xlim(-limite, limite)
ax.set_ylim(-limite, limite)
ax.set_title("Hormiga de Langton")

# Lista de puntos negros
negros_x = []
negros_y = []

# Dibujar los puntos negros iniciales
puntos_negros = ax.scatter(negros_x, negros_y, c="black", s=10)
hormiga_plot, = ax.plot([x], [y], "ro")  # listas, no enteros

for paso in range(iteraciones):
    if not plt.fignum_exists(fig.number):  # si cerraste la ventana
        break

    color = celdas.get((x, y), 0)

    if color == 0:  # blanco → gira derecha, pinta negro
        direccion = (direccion + 1) % 4
        celdas[(x, y)] = 1
        negros_x.append(x)
        negros_y.append(y)
    else:  # negro → gira izquierda, pinta blanco
        direccion = (direccion - 1) % 4
        celdas[(x, y)] = 0
        if (x, y) in zip(negros_x, negros_y):
            idx = list(zip(negros_x, negros_y)).index((x, y))
            negros_x.pop(idx)
            negros_y.pop(idx)

    # Avanzar
    dx, dy = movs[direccion]
    x += dx
    y += dy

    # Actualizar puntos negros
    puntos_negros.set_offsets(list(zip(negros_x, negros_y)))

    # Actualizar hormiga (en listas para evitar error)
    hormiga_plot.set_data([x], [y])

    plt.pause(velocidad)

plt.ioff()
plt.show()
