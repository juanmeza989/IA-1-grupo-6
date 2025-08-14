import matplotlib.pyplot as plt

# Definición de movimientos: N, E, S, O
movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Estado inicial
x, y = 0, 0
direccion = 0  # 0=N, 1=E, 2=S, 3=O
celdas = {}    # Diccionario: (x, y) -> 0 (blanco) o 1 (negro)

# Guardar trayectoria
trayectoria_x = [x]
trayectoria_y = [y]

# Configuración del gráfico interactivo
plt.ion()
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)

iteraciones = 12000  # pasos para mostrar

for paso in range(iteraciones):
    color = celdas.get((x, y), 0)

    if color == 0:  # Blanco → gira derecha, pone negro
        direccion = (direccion + 1) % 4
        celdas[(x, y)] = 1
    else:  # Negro → gira izquierda, pone blanco
        direccion = (direccion - 1) % 4
        celdas[(x, y)] = 0

    # Avanzar
    dx, dy = movs[direccion]
    x += dx
    y += dy

    trayectoria_x.append(x)
    trayectoria_y.append(y)

    # Limpiar y dibujar
    ax.clear()
    ax.set_aspect("equal")
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)

    # Dibujar celdas negras
    negros_x = [px for (px, py), col in celdas.items() if col == 1]
    negros_y = [py for (px, py), col in celdas.items() if col == 1]
    ax.scatter(negros_x, negros_y, c="black", s=10)

    # Dibujar hormiga
    ax.plot(x, y, "ro")

    plt.draw()
    plt.pause(0.000001)  # control de velocidad

plt.ioff()
plt.show()
