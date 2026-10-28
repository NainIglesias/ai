# IA clásica: inteligencia sin aprendizaje

Una profundización de [¿Qué es la inteligencia artificial?](../../background/what_is_ai.md): opcional, y nunca se evalúa.

El aprendizaje automático es una forma de hacer inteligente un programa: enséñale ejemplos con sus respuestas, y deja que encuentre las reglas. Durante sus primeras décadas, IA significaba el camino contrario: escribir el conocimiento, y hacer que el programa razone con él. Eso es la **IA simbólica** o **IA clásica**, a veces llamada *good old-fashioned AI* (GOFAI), junto con su sucesora probabilística, el razonamiento con incertidumbre. No es el *aprendizaje automático clásico*, nombre que se suele dar a los métodos de aprendizaje que no son redes neuronales, como los árboles de decisión: esos aprenden de los datos.

Nada en estos notebooks se entrena con datos, hasta que el último muestra dónde entra el aprendizaje; el razonamiento basado en casos, en el notebook 4, es lo que más se acerca, acumulando casos. Cada uno construye un pequeño ejemplo en Python puro, una idea por celda, sin nada que instalar aparte del propio Python.

## Itinerario

| # | Notebook | Contenido |
| --- | --- | --- |
| 1 | [Búsqueda](search.ipynb) | Búsqueda en anchura, en profundidad, de coste uniforme y A\* en mapas de carreteras; heurísticas admisibles; buscar contra un oponente |
| 2 | [Búsqueda local y optimización](local_search.ipynb) | Ascensión de colinas, reinicios aleatorios, recocido simulado y un algoritmo genético en el problema de las ocho reinas; la relación con el descenso del gradiente |
| 3 | [Satisfacción de restricciones](constraint_satisfaction.ipynb) | *Backtracking* con la heurística de mínimos valores restantes, en un mapa y un Sudoku |
| 4 | [Reglas y sistemas expertos](rules_and_expert_systems.ipynb) | Encadenamiento hacia delante y hacia atrás; MYCIN y XCON; por qué se apagaron los sistemas expertos, y dónde viven hoy las reglas; razonamiento basado en casos, resolver a partir de casos pasados en lugar de reglas |
| 5 | [Representación del conocimiento](knowledge_representation.ipynb) | Redes semánticas con herencia y excepciones; marcos (*frames*), y sus descendientes, las clases |
| 6 | [Lógica](logic.ipynb) | Lógica proposicional e implicación mediante comprobación de modelos, con respuestas que pueden ser *desconocido*; reglas de primer orden en Prolog, y las mismas reglas como consulta SQL recursiva |
| 7 | [Planificación](planning.ipynb) | STRIPS: estados y acciones descritos con hechos; el mundo de los bloques y la anomalía de Sussman; planificación a gran escala |
| 8 | [Razonamiento con incertidumbre](uncertainty.ipynb) | Una red bayesiana a mano, inferencia por enumeración, *explaining away*; y las mismas tablas aprendidas a partir de datos |

Los **juegos** son búsqueda contra un oponente: el notebook 1 explica minimax, y [Python tic-tac-toe](https://github.com/avidaldo/python-tic-tac-toe/tree/master/02_minimax) lo implementa, con un jugador que nunca pierde.

## El teorema de Bayes, aquí y en otros sitios

El razonamiento bayesiano aparece en tres sitios, cada uno con su papel: el propio **teorema**, con su derivación y una prueba diagnóstica, en la profundización [Probabilidad y teorema de Bayes](../probability/README.md); las **redes bayesianas escritas a mano**, en el notebook 8; y el **clasificador naive Bayes**, cuyas probabilidades se cuentan a partir de datos etiquetados, en una profundización de aprendizaje supervisado *(próximamente)*. No está a un lado de la línea entre IA clásica y aprendizaje automático: lo que decide el lado es de dónde vienen las probabilidades, de un experto o de los datos.

## Lo que no se trata aquí

- **Lógica difusa** (Lotfi Zadeh, 1965): la verdad como un grado entre 0 y 1 en lugar de verdadero o falso, usada en sistemas de control como lavadoras y frenos de trenes.
- **Procesamiento simbólico del lenguaje:** gramáticas y programas de reconocimiento de patrones como ELIZA (Joseph Weizenbaum, 1966), el primer chatbot.
- **Procesamiento de imágenes sin aprendizaje:** filtros, bordes y umbrales, en la primera parte de [visión por computador](https://github.com/avidaldo/computer-vision).
- **Decisiones a lo largo del tiempo:** utilidades y procesos de decisión de Markov, la base del aprendizaje por refuerzo (etapa 15).

## ¿Se sigue usando algo de esto?

Más de lo que sugiere el nombre *clásica*, pero de forma desigual. La búsqueda y la optimización están en todas partes: los planificadores de rutas ejecutan descendientes del algoritmo de Dijkstra y de A\*, y los horarios, las rutas de reparto y la planificación de la producción salen de resolvedores de restricciones y de búsqueda local. Las reglas sobreviven en los motores de reglas de negocio y en las salvaguardas alrededor de los modelos de lenguaje, pero los sistemas expertos construidos a mano son raros: donde hay datos, el aprendizaje automático lo hace mejor y es más barato de construir. La lógica sigue viva en los comprobadores de tipos, la verificación formal y las consultas SQL recursivas, mientras que Prolog en sí es un lenguaje de nicho. Las redes bayesianas se siguen usando en diagnóstico y evaluación de riesgos, cada vez más con probabilidades aprendidas de los datos. Y los sistemas más capaces mezclan los dos mundos: AlphaGo buscaba con evaluaciones aprendidas, y los agentes construidos sobre modelos de lenguaje planifican, llaman a herramientas y comprueban sus resultados con código.

Históricamente, la IA simbólica dominó desde el taller de Dartmouth de 1956 hasta finales de los 80, cuando los sistemas expertos resultaron caros de construir y frágiles en el uso; el aprendizaje automático se quedó entonces con los problemas cuyas reglas no se pueden escribir, como la visión, la voz y el lenguaje.
