# Algoritmos de aprendizaje automático: una introducción histórica

## La evolución del aprendizaje automático

El aprendizaje automático, como campo, ha evolucionado a lo largo de varias décadas, con distintos algoritmos que fueron surgiendo para resolver tipos concretos de problemas. Entender el contexto histórico nos ayuda a ver por qué se desarrollaron ciertos algoritmos y cuándo usar cada uno.

El aprendizaje automático abarca tres paradigmas fundamentales:
- **Aprendizaje supervisado**: aprender de ejemplos etiquetados (pares entrada-salida)
- **Aprendizaje no supervisado**: descubrir patrones en datos sin etiquetar
- **Aprendizaje por refuerzo**: aprender mediante la interacción y el feedback

## Cronología de los algoritmos clave

### Regresión lineal (1805)

**Propósito:** predecir un valor continuo a partir de características de entrada.

**Historia:** el método de mínimos cuadrados, que la ajusta, lo publicaron Legendre en 1805 y Gauss en 1809.

**Por qué importa:** sentó las bases del aprendizaje supervisado, y se sigue usando mucho por su sencillez e interpretabilidad.

### Análisis de componentes principales (1901)

**Propósito:** reducción de dimensionalidad no supervisada: resumir muchas características correlacionadas con unas pocas nuevas.

**Historia:** lo introdujo Karl Pearson en 1901 y lo desarrolló Harold Hotelling en 1933.

**Por qué importa:** comprime los datos, elimina la redundancia y hace visibles en dos o tres dimensiones datos de alta dimensionalidad.

### Regresión logística (años 40–50)

**Propósito:** clasificación, en especial clasificación binaria (sí/no, verdadero/falso).

**Historia:** aplica la función logística (sigmoide), que Pierre-François Verhulst había usado en las décadas de 1830 y 1840 para modelar el crecimiento de poblaciones. Joseph Berkson acuñó el término *logit* en 1944, y David Cox desarrolló la regresión logística como método de regresión en 1958.

**Por qué importa:** a pesar de su nombre, es un algoritmo de clasificación: convierte una combinación lineal de las características en una probabilidad. Una neurona con activación sigmoide calcula exactamente esto.

### K vecinos más cercanos (1951–1967)

**Propósito:** tanto clasificación como regresión mediante aprendizaje basado en la similitud.

**Historia:** lo propusieron Evelyn Fix y Joseph Hodges en 1951, y lo analizaron Thomas Cover y Peter Hart en 1967.

**Por qué importa:** KNN introdujo el aprendizaje basado en instancias (aprendizaje perezoso): durante el entrenamiento no se construye ningún modelo explícito, y una predicción mira los ejemplos guardados más parecidos. Es intuitivo, pero predecir puede ser lento con datasets grandes.

### *Clustering* K-means (1957)

**Propósito:** aprendizaje no supervisado para agrupar puntos de datos parecidos en *clusters*.

**Historia:** Stuart Lloyd ideó el algoritmo estándar en 1957 (publicado solo en 1982), y James MacQueen lo llamó *k-means* en 1967.

**Por qué importa:** fue uno de los primeros algoritmos no supervisados de uso generalizado, y sigue siendo habitual para segmentar clientes, comprimir imágenes y explorar datos.

### El perceptrón (1958)

**Propósito:** clasificación binaria con una única neurona artificial que aprende sus pesos a partir de ejemplos.

**Historia:** Frank Rosenblatt, 1958.

**Por qué importa:** es el antepasado de todas las redes neuronales ([Las redes neuronales vistas desde fuera](neural_networks.md)).

### Naive Bayes (años 60)

**Propósito:** clasificación mediante el teorema de Bayes, suponiendo que las características son independientes entre sí dentro de cada clase.

**Historia:** se usó para clasificar texto desde principios de los años 60; se convirtió en el filtro de spam clásico a finales de los 90.

**Por qué importa:** se entrena en una sola pasada por los datos y funciona sorprendentemente bien con muchas características, como las palabras de un texto, aunque su suposición de independencia casi nunca es cierta.

### Árboles de decisión (años 60–90)

**Historia:** el concepto surgió en los años 60, pero los algoritmos modernos se desarrollaron después:
- **CART (Classification and Regression Trees)** (1984)
- **ID3** (1986)
- **C4.5** (1993), una mejora de ID3

**Propósito:** tanto clasificación como regresión mediante una toma de decisiones jerárquica.

**Por qué importa:** los árboles de decisión son muy interpretables y pueden captar relaciones no lineales. Se convirtieron en la base de potentes métodos de *ensemble* como Random Forests y Gradient Boosting.

### Q-Learning (1989)

**Propósito:** aprendizaje por refuerzo para la toma de decisiones secuenciales mediante prueba y error.

**Historia:** Christopher Watkins, 1989.

**Por qué importa:** a diferencia del aprendizaje supervisado (que aprende de ejemplos etiquetados) o del no supervisado (que encuentra patrones), el aprendizaje por refuerzo aprende interactuando con un entorno y recibiendo recompensas o penalizaciones. Este enfoque ha resultado crucial para la robótica, los juegos y los sistemas autónomos.

**Concepto clave:** el algoritmo construye una «tabla Q» que guarda la recompensa futura esperada de cada acción en cada estado, y va aprendiendo el comportamiento óptimo poco a poco con la experiencia.

### Máquinas de vectores de soporte (1992–1995)

**Propósito:** clasificación (y, con variantes, regresión) encontrando la frontera que separa las clases con el margen más amplio posible.

**Historia:** Bernhard Boser, Isabelle Guyon y Vladimir Vapnik añadieron el *kernel trick* en 1992, que permite que la frontera sea curva; Corinna Cortes y Vapnik permitieron algunos ejemplos en el lado equivocado, el *margen blando*, en 1995.

**Por qué importa:** durante una década estuvieron entre los clasificadores más precisos disponibles, y siguen funcionando bien con datasets pequeños y medianos.

### Boosting (1995–2001)

**Propósito:** método de *ensemble* que entrena muchos modelos débiles en secuencia, cada uno corrigiendo los errores de los anteriores.

**Historia:** AdaBoost de Yoav Freund y Robert Schapire (1995), y el *gradient boosting* de Jerome Friedman (2001), que generalizó la idea a cualquier función de pérdida diferenciable.

**Por qué importa:** los árboles con *gradient boosting* (XGBoost, LightGBM, CatBoost) son hoy los modelos de propósito general más potentes para datos tabulares.

### Random Forests (2001)

**Propósito:** método de *ensemble* para clasificación y regresión que mejora los árboles de decisión individuales.

**Historia:** Leo Breiman, 2001.

**Por qué importa:** un *random forest* promedia muchos árboles profundos, cada uno entrenado con una muestra aleatoria de los ejemplos y considerando un subconjunto aleatorio de las características en cada división. Cada árbol se sobreajusta a su manera, así que sus errores se compensan en parte: promediar reduce la varianza de un árbol individual. (Combinar modelos *débiles* es la idea del boosting, no de los random forests.)

## A qué paradigma pertenece cada algoritmo

| Paradigma | Algoritmos anteriores | Tareas |
| --- | --- | --- |
| Supervisado | Regresión lineal | Regresión |
| Supervisado | Regresión logística, perceptrón, naive Bayes | Clasificación |
| Supervisado | KNN, árboles de decisión, SVMs, random forests, boosting | Tanto clasificación como regresión |
| No supervisado | K-means | *Clustering* |
| No supervisado | PCA | Reducción de dimensionalidad |
| Refuerzo | Q-learning | Decisiones secuenciales a partir de recompensas |

Los paradigmas en sí, y cuándo usar cada uno, se explican en [Paradigmas del aprendizaje automático](machine_learning_paradigms.md).

## La era moderna

El panorama actual del aprendizaje automático ha evolucionado e incluye:
- **Aprendizaje profundo (desde 2012):** redes neuronales con muchas capas: redes convolucionales para imágenes, redes recurrentes y LSTMs para secuencias
- **Métodos de *ensemble* avanzados:** XGBoost (2014), LightGBM y CatBoost (2017)
- **Aprendizaje por transferencia:** reutilizar modelos preentrenados para resolver problemas nuevos
- ***Transformers* y grandes modelos de lenguaje:** la arquitectura *transformer* (2017), BERT y el primer GPT (2018), y los asistentes de chat construidos sobre grandes modelos de lenguaje (ChatGPT, 2022; Claude, Gemini y otros desde entonces)
- **Aprendizaje por refuerzo profundo:** DQN jugando a juegos de Atari (2013–2015), AlphaGo (2016), AlphaZero (2017), y el aprendizaje por refuerzo a partir de feedback humano en los asistentes de chat

Aun así, los algoritmos clásicos que estudiamos siguen siendo fundamentales porque:
- A menudo son la mejor opción para datasets pequeños y medianos
- Varios de ellos (modelos lineales, árboles de decisión pequeños) son interpretables y explicables, lo que importa en sectores regulados
- Sirven como piezas para construir métodos más complejos
- Son eficientes computacionalmente y a menudo necesitan menos datos que el aprendizaje profundo
- Son esenciales para entender los conceptos modernos de aprendizaje automático
- Muchas soluciones punteras siguen usando estos algoritmos (p. ej., XGBoost se basa en árboles de decisión)

## Elegir el algoritmo adecuado

La elección del algoritmo depende de varios factores:

| Factor | Ten en cuenta |
|--------|----------|
| **Tipo de problema** | ¿Clasificación, regresión, *clustering* o toma de decisiones secuenciales? |
| **Datos disponibles** | ¿Tienes datos etiquetados? ¿Sin etiquetar? ¿O puedes definir recompensas? |
| **Tamaño de los datos** | Los datasets pequeños favorecen modelos más sencillos; los grandes pueden aprovechar modelos complejos |
| **Interpretabilidad** | ¿Necesitas explicar las predicciones? (Usa modelos lineales, árboles de decisión) |
| **Velocidad** | Equilibrio entre tiempo de entrenamiento y tiempo de predicción |
| **Precisión necesaria** | Pueden bastar modelos sencillos; los problemas complejos pueden necesitar *ensembles* |
| **Propiedades de los datos** | Relaciones lineales o no lineales, presencia de valores atípicos, interacciones entre características |
| **Decisiones secuenciales** | Si las acciones afectan a estados futuros, plantéate el aprendizaje por refuerzo |

> [Scikit-learn: elegir el estimador adecuado](https://scikit-learn.org/stable/machine_learning_map.html) (en inglés)
