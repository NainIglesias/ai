# Preparación de datos para el aprendizaje automático

Antes de que un modelo pueda aprender nada, hay que entender los datos y hacerlos utilizables: explorarlos, revisarlos, limpiarlos, codificarlos y escalarlos. Cada notebook explica un paso, partiendo de una tabla lo bastante pequeña para verla entera y pasando a un dataset real que tiene el problema, para que puedas volver al que necesites.

El itinerario es una visión general básica de los pasos que casi cualquier modelo necesita, que se lee después de la parte 3 de [Aprendizaje supervisado](../supervised-learning/README.md#itinerario), cuyos pipelines usa. Empieza donde termina el pandas de [Lo esencial de Python para datos](../../pia/python-data-essentials/README.md), con las decisiones que dependen de los datos.

## Itinerario

| # | Nivel | Elemento | Contenido |
| --- | --- | --- | --- |
| 1 | estándar | [Valores ausentes](missing_values.ipynb) | Por qué falta un valor cambia lo que puedes hacer con ello; eliminar, rellenar con un estadístico, marcar, rellenar a partir de filas parecidas o de las demás columnas, dejárselo al modelo; qué supone cada opción |
| 2 | estándar | [Codificar categorías](categorical_encoding.ipynb) | Codificación ordinal y *one-hot*, y cuándo es incorrecta cada una; categorías que solo aparecen en datos nuevos; categorías con muchos valores: agrupar las raras y la codificación por objetivo (*target encoding*) |
| 3 | estándar | [Escalar variables numéricas](feature_scaling.ipynb) | Qué modelos necesitan escalado y por qué (distancias, gradientes, penalizaciones), y cuáles no (árboles); escalado min-max, estándar, robusto y max-abs comparados sobre la misma columna; escalar el objetivo |
| | profundización | [Valores atípicos y valores topados](complementary/outliers.ipynb) | Un error, un caso raro o una población distinta; reglas para encontrarlos y por qué la habitual se deja engañar por los propios atípicos; los valores topados, que no son atípicos; conservar, recortar, transformar o marcar |
| | profundización | [Distribuciones asimétricas y la transformación logarítmica](complementary/skewed_distributions.ipynb) | Colas largas a la derecha y por qué importan a unos modelos y a otros no; las transformaciones logarítmica, de potencia y de cuantiles; tomar el logaritmo del objetivo, y qué predice entonces el modelo |
| | profundización | [Distribuciones asimétricas y la transformación logarítmica](complementary/skewed_distributions.ipynb) | Colas largas a la derecha y por qué importan a unos modelos y a otros no; las transformaciones logarítmica, de potencia y de cuantiles; tomar el logaritmo del objetivo, y qué predice entonces el modelo |
| 4 | estándar | [Dónde termina la preparación de datos y empieza el modelado](where_preparation_ends.ipynb) | Los pasos que no aprenden nada de los datos se pueden hacer una vez, para todos, en el pipeline de datos (ETL); los que aprenden de ellos deben ajustarse solo con los datos de entrenamiento, dentro del pipeline del modelo; una fuga demostrada con una columna de puro ruido |
| | profundización | [Tipos de variables](complementary/kinds_of_features.ipynb) | Qué son una fila, una variable (*feature*) y un objetivo (*target*); números, categorías (con y sin orden), fechas, texto, identificadores; por qué el tipo que pandas da a una columna no es su clase; columnas que no deben ser variables |
| | profundización | [Explorar un dataset](complementary/exploring_a_dataset.ipynb) | Las preguntas que hay que hacerle a una tabla nueva y el resumen o gráfico que responde a cada una; qué se puede mirar antes de la división y qué solo en el conjunto de entrenamiento; anotar lo que se encuentra en forma de decisiones |
| | profundización | [La correlación y lo que se le escapa](complementary/correlation.ipynb) | El coeficiente de Pearson, calculado a mano y como matriz; relaciones que no puede ver; el coeficiente de Spearman; una correlación que se invierte dentro de cada grupo |
| | profundización | [Crear variables](complementary/creating_features.ipynb) | Cocientes, partes de una fecha, tiempo transcurrido, valores cíclicos, intervalos y productos; variables calculadas solo a partir de cada fila, y variables aprendidas de los datos |

Siguiente: volver a [Aprendizaje supervisado, parte 4](../supervised-learning/README.md#parte-4--clasificación).
