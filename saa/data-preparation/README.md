# Preparación de datos para el aprendizaje automático

Antes de que un modelo pueda aprender nada, hay que entender los datos y hacerlos utilizables: explorarlos, revisarlos, limpiarlos, codificarlos y escalarlos. Cada notebook explica un paso, partiendo de una tabla lo bastante pequeña para verla entera y pasando a un dataset real que tiene el problema, para que puedas volver al que necesites.

El itinerario es una visión general básica de los pasos que casi cualquier modelo necesita, que se lee después de la parte 3 de [Aprendizaje supervisado](../supervised-learning/README.md#itinerario), cuyos pipelines usa. Empieza donde termina el pandas de [Lo esencial de Python para datos](../../pia/python-data-essentials/README.md), con las decisiones que dependen de los datos. Las profundizaciones van más lejos, un paso cada una.

## Itinerario

Ninguno de los cuatro es un elemento básico (★): cuando un notebook básico de Aprendizaje supervisado usa uno de estos pasos, dice lo que necesitas saber de él. Una sección cuyo título termina en *(profundización)* es opcional, como las profundizaciones de más abajo, y nunca se pregunta.

| # | Notebook | Contenido |
| --- | --- | --- |
| 1 | [Valores ausentes](missing_values.ipynb) | Por qué falta un valor cambia lo que puedes hacer con ello; eliminar, rellenar con un estadístico, marcar, rellenar a partir de filas parecidas o de las demás columnas, dejárselo al modelo; qué supone cada opción |
| 2 | [Codificar categorías](categorical_encoding.ipynb) | Codificación ordinal y *one-hot*, y cuándo es incorrecta cada una; categorías que solo aparecen en datos nuevos; categorías con muchos valores: agrupar las raras y la codificación por objetivo (*target encoding*) |
| 3 | [Escalar variables numéricas](feature_scaling.ipynb) | Qué modelos necesitan escalado y por qué (distancias, gradientes, penalizaciones), y cuáles no (árboles); escalado min-max, estándar, robusto y max-abs comparados sobre la misma columna; escalar el objetivo |
| 4 | [Dónde termina la preparación de datos y empieza el modelado](where_preparation_ends.ipynb) | Los pasos que no aprenden nada de los datos se pueden hacer una vez, para todos, en el pipeline de datos (ETL); los que aprenden de ellos deben ajustarse solo con los datos de entrenamiento, dentro del pipeline del modelo; una fuga demostrada con una columna de puro ruido |

## Profundizaciones

Opcionales y nunca se evalúan. El itinerario nunca depende de ellas.

| Profundización | Amplía | Contenido |
| --- | --- | --- |
| [Tipos de variables](deep-dives/kinds_of_features.ipynb) | 1–4 | Qué son una fila, una variable (*feature*) y un objetivo (*target*); números, categorías (con y sin orden), fechas, texto, identificadores; por qué el tipo que pandas da a una columna no es su clase; columnas que no deben ser variables |
| [Explorar un dataset](deep-dives/exploring_a_dataset.ipynb) | 1–4 | Las preguntas que hay que hacerle a una tabla nueva y el resumen o gráfico que responde a cada una; qué se puede mirar antes de la división y qué solo en el conjunto de entrenamiento; anotar lo que se encuentra en forma de decisiones |
| [La correlación y lo que se le escapa](deep-dives/correlation.ipynb) | *Explorar un dataset* | El coeficiente de Pearson, calculado a mano y como matriz; relaciones que no puede ver; el coeficiente de Spearman; una correlación que se invierte dentro de cada grupo |
| [Valores atípicos y valores topados](deep-dives/outliers.ipynb) | 1, 3 | Un error, un caso raro o una población distinta; reglas para encontrarlos y por qué la habitual se deja engañar por los propios atípicos; los valores topados, que no son atípicos; conservar, recortar, transformar o marcar |
| [Distribuciones asimétricas y la transformación logarítmica](deep-dives/skewed_distributions.ipynb) | 3 | Colas largas a la derecha y por qué importan a unos modelos y a otros no; las transformaciones logarítmica, de potencia y de cuantiles; tomar el logaritmo del objetivo, y qué predice entonces el modelo |
| [Crear variables](deep-dives/creating_features.ipynb) | 2, 4 | Cocientes, partes de una fecha, tiempo transcurrido, valores cíclicos, intervalos y productos; variables calculadas solo a partir de cada fila, y variables aprendidas de los datos |
| [Escalar imágenes](deep-dives/scaling_images.ipynb) | 3 |
