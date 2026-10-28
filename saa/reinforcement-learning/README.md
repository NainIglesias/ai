# Aprendizaje por refuerzo: Q-learning

Aprender de recompensas en lugar de etiquetas: un agente actúa en un entorno, recibe recompensas y aprende qué acción merece la pena tomar en cada situación.

## Itinerario

★ marca los elementos básicos: el mínimo, si tienes poco tiempo esta semana.

| # | Notebook | Contenido |
| --- | --- | --- |
| ★ 1 | [Aprendizaje por refuerzo y Q-learning](qlearning.ipynb) | Agente, entorno, recompensa y política; una visión intuitiva del Q-learning, entrenado desde cero en un pequeño mundo de cuadrícula |
| 2 | [La ecuación de Bellman](bellman_equation.ipynb) | De dónde sale la regla de actualización del Q-learning, calculada a mano paso a paso y después en código |
| 3 | [Q-learning en FrozenLake](frozen_lake.ipynb) | Entrenar y evaluar un agente de Q-learning en un entorno de [Gymnasium](https://gymnasium.farama.org/) |

La misma idea, aprender de una recompensa, es uno de los pasos para convertir un modelo de lenguaje en un asistente de chat (RLHF): consulta *Cómo se construye un modelo de lenguaje* en la nota de la etapa 2 [Los modelos de lenguaje vistos desde fuera](../concepts/background/language_models.md#cómo-se-construye-un-modelo-de-lenguaje).

## Ejemplo resuelto

[Tres en raya con Q-learning](https://github.com/avidaldo/tictactoe-qlearning) es un repositorio propio: mejora un agente paso a paso, desde la versión más sencilla hasta una que nunca pierde contra un jugador perfecto. Su README propone más experimentos, y sus notebooks tienen ejercicios: simetrías del tablero, un currículo, un torneo.

## Práctica

**Haz que el lago resbale.** En [Q-learning en FrozenLake](frozen_lake.ipynb), crea el entorno con `is_slippery=True`: ahora cada movimiento va en la dirección prevista solo una de cada tres veces, y el resto resbala hacia un lado o hacia el otro.

1. Evalúa con 1.000 episodios en lugar de 100, y entrena tres o cuatro veces, volviendo a crear la tabla Q antes de cada ejecución (si no, el entrenamiento continúa desde la última tabla). ¿Con qué frecuencia llega el agente a la meta, y cuánto cambia eso de una ejecución a otra?
2. Ninguna política llega a la meta siempre en este lago: la mejor posible lo consigue alrededor del 74 % de las veces dentro del límite de 99 pasos. Cambia la tasa de aprendizaje, gamma y el número de episodios, primero de uno en uno y después a la vez, hasta que todas las ejecuciones se acerquen al 74 %. ¿Qué cambios importan, y por qué importan aquí cuando no importaban en el lago determinista?
3. Mira la acción que elige tu mejor agente en el estado inicial. ¿Por qué esa?

Una [solución](practice/slippery_lake_solution.ipynb), para leer cuando lo hayas intentado.

## Referencias

- El notebook 3 está adaptado de la Unidad 2 del [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit2/introduction) (licencia Apache 2.0), que sigue con el *deep Q-learning* y los métodos de gradiente de política.
- Richard S. Sutton y Andrew G. Barto, [*Reinforcement Learning: An Introduction*](http://incompleteideas.net/book/the-book-2nd.html), 2.ª edición (2018), gratis en línea: el libro de texto de referencia. El capítulo 6 presenta el Q-learning.
