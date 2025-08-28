1️⃣ Caracterización del agente con tabla REAS

REAS → Representación, Entorno, Actuadores y Sensores.

Elemento	Descripción
R (Representación interna)	La hormiga conoce su orientación (N, S, E, O) y el estado de la celda actual (blanca o negra). Representaremos el plano como una matriz o diccionario donde cada coordenada tiene un color (0 = blanco, 1 = negro).
E (Entorno)	Infinito (o lo suficientemente grande para la simulación), discreto, determinista, parcialmente observable (la hormiga solo percibe la celda actual), estático (no cambia por sí mismo, solo cambia por acción del agente).
A (Actuadores)	Cambiar color de la celda, girar 90° (izquierda/derecha), avanzar una celda en la dirección actual.
S (Sensores)	Detectar el color de la celda actual (blanco o negro).


2️⃣ Propiedades del entorno

Accesibilidad: Parcialmente accesible (solo percibe el estado de la celda actual).

Determinista: Sí (las acciones siempre producen el mismo resultado).

Episódico: No, el estado actual depende del historial.

Estático/Dinámico: Estático (el entorno no cambia sin intervención).

Discreto/Continuo: Discreto (rejilla de celdas).

Número de agentes: Un solo agenteeee