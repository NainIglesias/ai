# Los modelos de lenguaje vistos desde fuera

Un **modelo de lenguaje** es una [red neuronal](neural_networks.md) entrenada para continuar texto. Los asistentes de chat, el [asistente de programación con IA](../../../pia/setup/ai_assisted_development.md) de tu editor y las aplicaciones con modelos de lenguaje que se construyen en PIA funcionan todos sobre uno. Visto desde fuera, hace una sola cosa una y otra vez: predice el siguiente trozo de texto. Casi todo lo que nota quien lo usa, lo bueno y lo malo, se deduce de eso y de cómo se entrenó el modelo. Cómo calcula sus predicciones por dentro, con *embeddings*, atención y el *transformer*, se explica en el tema sobre cómo funcionan los modelos de lenguaje *(próximamente)*.

<img src="img/ai_hierarchy_llms.png" width="300" alt="Círculos anidados: inteligencia artificial, aprendizaje automático, redes neuronales, aprendizaje profundo, IA generativa, grandes modelos de lenguaje">

*Una imagen habitual de dónde se sitúan los modelos de lenguaje. Simplifica: algunos modelos generativos no son redes profundas, y algunos modelos de lenguaje, como BERT, rellenan palabras ocultas en lugar de continuar texto, y no generan nada.*

## Un token cada vez

### Tokens

Un modelo de lenguaje no lee letras ni palabras, sino **tokens**: trozos de texto de un vocabulario fijo. Un programa llamado *tokenizador* construye ese vocabulario antes del entrenamiento, a partir de una muestra grande de texto: los trozos que aparecen más a menudo se convierten en tokens. Una palabra frecuente es un solo token, normalmente junto con el espacio que la precede, y una palabra rara se divide en varios. Aquí tienes la misma frase en tres idiomas, dividida por un tokenizador real (`o200k_base` de OpenAI, con unos 200.000 tokens):

```text
Tokenization is unbelievably useful.      Token|ization| is| unbelievably| useful|.          6 tokens
La tokenización es increíblemente útil.   La| token|ización| es| increíble|mente| útil|.     8 tokens
A tokenización é incriblemente útil.      A| token|ización| é| in|crib|lement|e| útil|.      10 tokens
```

El inglés necesita menos tokens porque el texto a partir del que se construyen los tokenizadores es mayoritariamente inglés. Esto importa porque los modelos están limitados, y se cobran, por tokens: el mismo contenido en español o en gallego cuesta más de ambas cosas.

### Predecir el siguiente token

Dado un texto, el modelo calcula, para cada token de su vocabulario, la probabilidad de que sea el siguiente. Se elige un token y se añade, y el texto más largo vuelve a entrar en el modelo para elegir el siguiente. Una respuesta es ese paso repetido, token tras token, hasta que el modelo elige un token especial que marca el final o se alcanza un límite de longitud. Con probabilidades inventadas:

```text
The cat sat on the       →   mat 0.41   floor 0.18   sofa 0.09   …
The cat sat on the mat   →   . 0.52   and 0.21   , 0.08   …
```

*(«El gato se sentó en la… alfombra / suelo / sofá».)*

Cada token se elige a partir del texto hasta ese momento, así que un error temprano pasa a formar parte del texto desde el que continúa el modelo: un modelo que empieza una respuesta equivocada puede seguir con ella, e incluso justificarla.

### Muestreo y temperatura

El modelo no siempre coge el token más probable: **muestrea**, eligiendo al azar con las probabilidades predichas, de modo que *floor* sale casi una de cada cinco veces. Por eso la misma pregunta puede recibir respuestas distintas. Un parámetro llamado **temperatura** controla cuánto varían. Una temperatura baja hace que los tokens probables lo sean todavía más, y las respuestas más repetibles; una alta aplana las probabilidades, y las respuestas varían más. A temperatura 0 el modelo siempre coge el token más probable, aunque un modelo servido por un proveedor puede seguir sin dar exactamente la misma respuesta cada vez.

## Cómo se construye un modelo de lenguaje

Los **parámetros** de un modelo son los números que se ajustan en el entrenamiento, y un **gran modelo de lenguaje** (LLM) tiene miles de millones. Los pequeños, con unos pocos miles de millones, funcionan en un portátil; los más grandes necesitan el hardware de un centro de datos. Un modelo de chat se entrena en tres pasos:

1. **Preentrenamiento**, [autosupervisado](machine_learning_paradigms.md#entre-el-supervisado-y-el-no-supervisado): el modelo aprende a predecir el siguiente token de texto real (páginas web, libros, código), billones de tokens. Este paso suele ser el más caro, semanas o meses en miles de GPUs, y es donde el modelo aprende la mayor parte de lo que sabe sobre el lenguaje y el mundo. El resultado es un **modelo base**, que continúa cualquier texto en el estilo del texto con el que se entrenó.
2. **Ajuste por instrucciones** (*instruction tuning*), supervisado: el modelo se sigue entrenando con conversaciones de ejemplo, cada una una instrucción con una buena respuesta, escritas por personas o generadas por otros modelos. Aprende el formato de una conversación y el papel de un asistente.
3. **Ajuste por preferencias**: personas, y cada vez más otros modelos, comparan respuestas a la misma pregunta, y el modelo se ajusta para dar el tipo de respuesta que se prefiere: más útil, más honesta, y rechazando las peticiones dañinas. Una forma es el [aprendizaje por refuerzo a partir de feedback humano](machine_learning_paradigms.md#aprendizaje-por-refuerzo) (RLHF); otros métodos aprenden directamente de las comparaciones, sin aprendizaje por refuerzo.

> [!NOTE]
> **El mismo texto, dos modelos**
>
> Ante *«¿Cuál es la capital de Francia?»*, un modelo base puede seguir con *«¿Cuál es la capital de Alemania? ¿Cuál es la capital de Italia?»*, como si estuviera completando una lista de preguntas de un concurso: en la web, a una pregunta a menudo le siguen más preguntas. Un modelo ajustado con conversaciones responde *«París.»*

Los **modelos de razonamiento** añaden un paso más: aprendizaje por refuerzo sobre problemas cuyas respuestas se pueden comprobar automáticamente, como las matemáticas y la programación, con una recompensa por una respuesta final correcta. Aprenden a escribir una larga cadena de pasos intermedios antes de responder. Esto los hace mejores en ese tipo de problemas, y más lentos y caros, ya que esos pasos también son tokens.

El modelo no guarda una copia de su texto de entrenamiento para consultarla: lo que aprendió está repartido entre sus parámetros, aunque puede repetir palabra por palabra un pasaje que vio muchas veces.

## Lo que se deduce de todo esto

### Fluido no es lo mismo que verdadero

El modelo se entrenó para producir texto probable, no texto verdadero. Cuando su texto de entrenamiento decía lo mismo muchas veces, la respuesta probable suele ser correcta. Cuando no, la continuación más probable sigue siendo una respuesta fluida y segura: una referencia a un artículo que no existe, un artículo de una ley con el número equivocado, una función que una biblioteca no tiene. Esto se llama **alucinación**. El entrenamiento puede hacerla menos frecuente, enseñando a los modelos a decir cuándo no saben, pero no la elimina, y una respuesta equivocada se lee exactamente igual que una correcta. Comprueba lo que importe, y diseña las aplicaciones para que sus respuestas se puedan comprobar.

### Su conocimiento se detiene en una fecha

Lo que sabe un modelo viene de texto recopilado hasta una fecha, su **fecha de corte del conocimiento**. Cualquier cosa posterior, como una versión nueva de una biblioteca o una ley modificada el mes pasado, no existe para el modelo a menos que se le ponga delante el texto.

### El contexto es todo lo que ve

En cada llamada, el modelo solo ve el texto que se le envía, su **contexto**: las instrucciones de la aplicación (el *system prompt*), la conversación hasta ese momento y los documentos que haya. Una conversación le llega como un único texto, con marcas para cada rol, y el modelo la continúa desde el turno del asistente. El contexto tiene una longitud máxima, la **ventana de contexto**, contada en tokens y compartida por la pregunta y la respuesta: desde unos pocos miles de tokens en los primeros modelos hasta cientos de miles, o más, hoy.

El modelo no tiene memoria entre llamadas. Una aplicación de chat vuelve a enviar toda la conversación con cada mensaje, y una función de *memoria* guarda notas y las vuelve a meter en el contexto. Un contexto más largo cuesta más y tarda más, y un detalle en mitad de uno muy largo se puede pasar por alto con más facilidad que uno al principio o al final.

### Ve tokens, no letras

Como el modelo lee tokens, las tareas sobre letras le resultan más difíciles de lo que parece. Arriba, *unbelievably* es un solo token: el modelo no ve sus letras, así que contarlas, o deletrear la palabra al revés, tiene que salir de lo que aprendió sobre ese token. La aritmética exacta con números largos también es propensa a errores. Un programa hace ambas cosas de forma fiable, y a un modelo se le puede dar uno como herramienta.

### Solo escribe texto

Un modelo no puede buscar en la web, ejecutar código, leer tus archivos ni enviar un email: solo produce texto. Una aplicación puede darle **herramientas**: el modelo escribe una petición en un formato acordado, una *llamada a herramienta* (*tool call*); la aplicación la ejecuta y mete el resultado en el contexto; y el modelo continúa. Un asistente de programación funciona así: leer un archivo o ejecutar un comando es una llamada a herramienta que lleva a cabo el programa del asistente, a menudo después de preguntarte. Los agentes, y MCP, una forma estándar de conectar modelos con herramientas, se explican en el tema sobre agentes y MCP *(próximamente)*.

### Respuestas basadas en documentos

Para responder sobre documentos que un modelo nunca vio, o que cambiaron después de su fecha de corte, una aplicación puede encontrar los pasajes que importan y ponerlos en el contexto, con la instrucción de responder solo a partir de ellos y de citarlos. Esto es la **generación aumentada por recuperación** (RAG), que se explica en su propio tema *(próximamente)*. Hace que las respuestas inventadas sean menos frecuentes, pero no las descarta: el modelo puede seguir leyendo mal un pasaje o citando el que no es, así que hay que comprobar las citas con la fuente.

## Más allá del texto

- **Modelos multimodales:** reciben imágenes, audio o vídeo como entrada, convertidos también en una secuencia de tokens, y algunos también los producen.
- ***Embeddings*:** un tipo de modelo relacionado convierte un texto entero en una lista de números, un vector, de forma que textos con significados parecidos tengan vectores cercanos entre sí. Así es como las aplicaciones buscan por significado, y a menudo como RAG encuentra sus pasajes. Cómo se aprenden los *embeddings* forma parte del tema sobre cómo funcionan los modelos de lenguaje *(próximamente)*.
- **Modelos de pesos abiertos y cerrados:** algunas empresas publican los pesos de un modelo, sus parámetros aprendidos, para que cualquiera pueda descargarlo y ejecutarlo en su propio ordenador, con una herramienta como Ollama, sin que sus datos salgan de él. Otros solo se pueden usar a través de la API de la empresa, pagando por token. Pesos abiertos no es lo mismo que código abierto: los datos y el código de entrenamiento normalmente no se publican, y la licencia puede restringir cómo se usa el modelo. Cómo llamar a ambos tipos se explica en el tema sobre construir con modelos de lenguaje *(próximamente)*.
