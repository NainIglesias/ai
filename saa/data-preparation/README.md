# Preparación de datos para el aprendizaje automático

Antes de que un modelo pueda aprender nada, hay que entender los datos y hacerlos utilizables: explorarlos, revisarlos, limpiarlos, codificarlos y escalarlos. Esta carpeta explica esos pasos con un concepto por notebook, para que puedas volver al que necesites cada vez que uno de tus flujos de trabajo lo use. La mayoría de los notebooks empiezan con una tabla lo bastante pequeña para verla entera y luego pasan a un dataset real que tiene el problema.

Su itinerario es una visión general básica: cuatro notebooks sobre las decisiones que necesitan los datos de casi cualquier modelo (rellenar huecos, codificar categorías, escalar números) y sobre dónde va cada uno de esos pasos. Forman parte de la etapa de aprendizaje supervisado, y conviene leerlos después de la parte 3 de [Aprendizaje supervisado](../supervised-learning/README.md#itinerario), cuyos pipelines usan. Las profundizaciones van más allá, un concepto cada una. La carpeta da por sabido lo esencial de NumPy y pandas (cargar, seleccionar, agrupar, los problemas que puede tener una tabla), y no depende de ningún modelo concreto: cuando un paso tiene su sitio dentro del pipeline de un modelo, el notebook lo dice y muestra por qué.

## Antes de empezar

- **pandas:** [Lo esencial de Python para datos](../../pia/python-data-essentials/README.md). Su notebook *Encontrar los problemas de una tabla* encuentra valores ausentes, duplicados e imposibles, y arregla lo que puede arreglar una regla fija; esta carpeta empieza donde termina aquel, con las decisiones que dependen de los datos.
- **Los datos como arrays:** [Matrices y tensores en IA](https://github.com/avidaldo/compare-python-c-efficiency/blob/main/02_matrices_in_ai.ipynb): una fila como un vector, una tabla como una matriz, una imagen como un array.
- **Pipelines:** los notebooks muestran cada paso dentro de un `Pipeline` de scikit-learn cuando hay que ajustarlo con los datos de entrenamiento. Cómo funcionan los pipelines se explica en [Viviendas de California con pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb).

## Itinerario

Ninguno de los cuatro es un elemento básico (★): cuando los notebooks básicos de Aprendizaje supervisado usan uno de estos pasos, dicen lo que necesitas saber de él. Una sección cuyo título termina en *(profundización)* es opcional, como las profundizaciones de más abajo, y nunca se pregunta.

| # | Notebook | Contenido | Se aplica en |
| --- | --- | --- | --- |
| 1 | [Valores ausentes](missing_values.ipynb) | Por qué falta un valor cambia lo que puedes hacer con ello; eliminar, rellenar con un estadístico, marcar, rellenar a partir de filas parecidas o de las demás columnas, dejárselo al modelo; qué supone cada opción | [Viviendas de California con pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb), [Diabetes Pima](../supervised-learning/basic-workflows/pima_diabetes.ipynb), [Tiroides](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| 2 | [Codificar categorías](categorical_encoding.ipynb) | Codificación ordinal y *one-hot*, y cuándo es incorrecta cada una; categorías que solo aparecen en datos nuevos; categorías con muchos valores: agrupar las raras y la codificación por objetivo (*target encoding*) | [Viviendas de California con pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb), [XGBoost](../supervised-learning/algorithms/tree-based/xgboost.ipynb) |
| 3 | [Escalar variables numéricas](feature_scaling.ipynb) | Qué modelos necesitan escalado y por qué (distancias, gradientes, penalizaciones), y cuáles no (árboles); escalado min-max, estándar, robusto y max-abs comparados sobre la misma columna; escalar el objetivo | [k vecinos más cercanos](../supervised-learning/algorithms/neighbours/knn.ipynb), [Descenso de gradiente](../supervised-learning/ml-fundamentals/gradient_descent.ipynb), [Máquinas de vectores de soporte](../supervised-learning/deep-dives/svm.ipynb) |
| 4 | [Dónde termina la preparación de datos y empieza el modelado](where_preparation_ends.ipynb) | Los pasos que no aprenden nada de los datos se pueden hacer una vez, para todos, en el pipeline de datos (ETL); los que aprenden de ellos deben ajustarse solo con los datos de entrenamiento, dentro del pipeline del modelo; una fuga demostrada con una columna de puro ruido | [Diabetes Pima](../supervised-learning/basic-workflows/pima_diabetes.ipynb), [Fuga de datos](../supervised-learning/ml-fundamentals/data_leakage.ipynb) |

## Profundizaciones

Opcionales y nunca se evalúan. El itinerario nunca depende de ellas.

| Notebook | Amplía | Contenido | Se aplica en |
| --- | --- | --- | --- |
| [Tipos de variables](deep-dives/kinds_of_features.ipynb) | 1–4 | Qué son una fila, una variable (*feature*) y un objetivo (*target*); números, categorías (con y sin orden), fechas, texto, identificadores; por qué el tipo que pandas da a una columna no es su clase; columnas que no deben ser variables | [Diabetes Pima](../supervised-learning/basic-workflows/pima_diabetes.ipynb), [Progresión de la diabetes](../supervised-learning/basic-workflows/deep-dives/diabetes_progression.ipynb) |
| [Explorar un dataset](deep-dives/exploring_a_dataset.ipynb) | 1–4 | Las preguntas que hay que hacerle a una tabla nueva y el resumen o gráfico que responde a cada una; qué se puede mirar antes de la división y qué solo en el conjunto de entrenamiento; anotar lo que se encuentra en forma de decisiones | [King County, EDA](https://github.com/avidaldo/king-county/blob/master/01-eda.ipynb), [Tiroides, preparación de datos](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| [La correlación y lo que se le escapa](deep-dives/correlation.ipynb) | *Explorar un dataset* | El coeficiente de Pearson, calculado a mano y como matriz; relaciones que no puede ver; el coeficiente de Spearman; una correlación que se invierte dentro de cada grupo | [Viviendas de California, paso a paso](../supervised-learning/basic-workflows/california_by_hand.ipynb) |
| [Valores atípicos y valores topados](deep-dives/outliers.ipynb) | 1, 3 | Un error, un caso raro o una población distinta; reglas para encontrarlos y por qué la habitual se deja engañar por los propios atípicos; los valores topados, que no son atípicos; conservar, recortar, transformar o marcar | [Viviendas de California, paso a paso](../supervised-learning/basic-workflows/california_by_hand.ipynb), [Tiroides](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| [Distribuciones asimétricas y la transformación logarítmica](deep-dives/skewed_distributions.ipynb) | 3 | Colas largas a la derecha y por qué importan a unos modelos y a otros no; las transformaciones logarítmica, de potencia y de cuantiles; tomar el logaritmo del objetivo, y qué predice entonces el modelo | [King County, preprocesamiento](https://github.com/avidaldo/king-county/blob/master/04a-preprocessing-step-by-step.ipynb), [Tiroides](https://github.com/avidaldo/thyroid/blob/master/01_data_preparation.ipynb) |
| [Crear variables](deep-dives/creating_features.ipynb) | 2, 4 | Cocientes, partes de una fecha, tiempo transcurrido, valores cíclicos, intervalos y productos; variables calculadas solo a partir de cada fila, y variables aprendidas de los datos | [Viviendas de California con pipelines](../supervised-learning/basic-workflows/california_with_pipelines.ipynb), [King County, preprocesamiento](https://github.com/avidaldo/king-county/blob/master/04a-preprocessing-step-by-step.ipynb) |
| [Escalar imágenes](deep-dives/scaling_images.ipynb) | 3 | Por qué una tabla se escala columna a columna y una imagen con una media y una desviación por canal de color; imágenes aplanadas en filas | |

## De flujos de trabajo pequeños a uno grande

Los notebooks de arriba explican un paso cada uno. Para ver los pasos trabajando juntos, sigue flujos de trabajo completos del más pequeño al más grande:

1. Los flujos de trabajo básicos de [Aprendizaje supervisado](../supervised-learning/README.md#itinerario): viviendas de California paso a paso y con pipelines, progresión de la diabetes y diabetes Pima.
2. [Ventas de casas en King County](https://github.com/avidaldo/king-county) y [enfermedad de tiroides](https://github.com/avidaldo/thyroid): un dataset real cada uno, con sus propios problemas.
3. [Viviendas de California, de principio a fin](https://github.com/avidaldo/california_e2e): un proyecto completo, desde plantear el problema hasta un modelo ajustado.

## Ejecutar los notebooks

Instala los paquetes del [`requirements.txt`](../../requirements.txt) del repositorio del curso en el entorno que prefieras (uv, venv o conda) y ejecuta cada notebook desde su propia carpeta. Los datasets se descargan la primera vez que un notebook los necesita, en una carpeta `data/` junto a él, que git ignora.

## Relacionado

- [Aprendizaje supervisado](../supervised-learning/README.md): la división en entrenamiento y prueba, los pipelines y la fuga de datos, que esta carpeta aplica sin volver a explicarlos.
- Aprendizaje no supervisado *(próximamente)*: análisis de componentes principales, clústeres como variables y detección de anomalías.
