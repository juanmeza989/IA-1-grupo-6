Tabla REAS (Representación, Entorno, Actuadores, Sensores)

Elemento	Descripción
R (Representación interna)	El sistema mantiene una matriz (o lista de listas) que representa el tablero, donde cada celda está en estado 0 = muerta o 1 = viva.
E (Entorno)	Un tablero bidimensional finito (o toroidal si se conecta en los bordes). Discreto en espacio y tiempo, determinista, estático entre actualizaciones (el estado cambia solo en cada iteración).
A (Actuadores)	Actualizar el estado de todas las celdas según las reglas: nacer, morir o vivir.
S (Sensores)	Contar el número de células vivas vecinas (8 posibles alrededor).


Propiedades del entorno

Accesibilidad: Totalmente accesible (el estado de todas las celdas es conocido).

Determinista: Sí, las reglas siempre producen el mismo resultado para el mismo estado inicial.

Episódico: No, cada estado depende del anterior.

Estático/Dinámico: Estático entre pasos de simulación.

Discreto/Continuo: Discreto.

Número de agentes: Puede interpretarse como un sistema sin un agente único, sino como un autómata celular donde cada celda sigue reglas locales.