import matplotlib.pyplot as plt
from collections import deque

# Definición de movimientos: N, E, S, O
movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Estado inicial
x, y = 0, 0
direccion = 0  # 0=N, 1=E, 2=S, 3=O
celdas = {}    # Diccionario: (x, y) -> 0 (blanco) o 1 (negro)

# Parámetros de simulación
iteraciones = 20000
limite = 50
velocidad = 0.00001

# Para detección de patrón
historial = deque(maxlen=208)  # 2 ciclos de 104 pasos
inicio_patron = None

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

    # Guardar estado para detección de patrón
    color = celdas.get((x, y), 0)
    historial.append((x, y, direccion, color))

    if len(historial) == historial.maxlen:
        mitad = len(historial) // 2
        if list(historial)[:mitad] == list(historial)[mitad:]:
            inicio_patron = paso - mitad
            print(f"Patrón repetitivo detectado a partir de la iteración {inicio_patron}")
            break

    # Reglas de la hormiga
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

    # Actualizar puntos negros y hormiga
    puntos_negros.set_offsets(list(zip(negros_x, negros_y)))
    hormiga_plot.set_data([x], [y])

    plt.pause(velocidad)

plt.ioff()
plt.show()

if inicio_patron:
    print(f"La hormiga entró en el patrón a partir de la iteración {inicio_patron}")
else:
    print("No se detectó patrón repetitivo en el rango simulado.")
