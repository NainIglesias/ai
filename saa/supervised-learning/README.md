# Aprendizaje supervisado

Aprender a partir de ejemplos etiquetados: regresión y clasificación con los algoritmos clásicos, y cómo saber si un modelo funcionará con datos que no ha visto. Aquí la evaluación no es un paso final; se enseña junto a los modelos desde el principio.

## Cómo está organizada esta carpeta

Los notebooks se agrupan por lo que enseñan, para que cada idea se explique en un solo sitio:

| Carpeta | Qué enseña |
| --- | --- |
| [`algorithms/`](algorithms/) | Cómo aprende y predice cada modelo, para regresión y para clasificación cuando hace las dos cosas: [modelos lineales](algorithms/linear-models/), [modelos basados en árboles](algorithms/tree-based/), [vecinos](algorithms/neighbours/) |
| [`ml-fundamentals/`](ml-fundamentals/) | Las ideas que comparten todos los modelos, sea cual sea su algoritmo: cómo se ajustan minimizando un error (descenso de gradiente); con qué datos se juzgan, y por qué (sobreajuste, la división en entrenamiento y prueba, validación, validación cruzada, fugas); controlar la complejidad |
| [`evaluation/`](evaluation/) | Qué medimos y cómo leemos los errores: errores de regresión, métricas de clasificadores, clases raras, análisis de errores |
| [`basic-workflows/`](basic-workflows/) | Ejemplos pequeños de principio a fin con distintos datasets. Aplican las otras carpetas sin volver a explicarlas, y enlazan a donde se explica cada paso |

El itinerario de abajo recorre las carpetas en el orden en que se necesitan las ideas; síguelo a él y no a las carpetas.

## Itinerario

★ marca los elementos básicos: el mínimo, si tienes poco tiempo esta semana. Una sección cuyo título termina en *(profundización)* es opcional, como las profundizaciones de más abajo, y nunca se pregunta.

### Parte 1 · Regresión, de principio a fin

| # | Notebook | Contenido |
| --- | --- | --- |
| ★ 1 | [Regresión lineal](algorithms/linear-models/linear_regression.ipynb) | Un primer modelo: ajustar una recta minimizando un error, predicción, regresión múltiple |
| ★ 2 | [Árboles de decisión](algorithms/tree-based/decision_trees.ipynb) | Árboles para clasificación y regresión; un modelo lo bastante flexible para ajustarse demasiado bien a sus datos de entrenamiento |
| ★ 3 | [El sobreajuste y la división en entrenamiento y prueba](ml-fundamentals/overfitting_and_the_split.ipynb) | Por qué un modelo debe juzgarse con datos que no vio; subajuste y sobreajuste; divisiones aleatorias y estratificadas; el conjunto de prueba representa los datos que el modelo encontrará en producción |
| ★ 4 | [Viviendas de California, paso a paso](basic-workflows/california_by_hand.ipynb) | Un primer flujo de trabajo completo, con cada paso escrito a mano: dividir, escalar, entrenar, predecir, evaluar; estimadores, transformadores y predictores |
| 5 | [Bosques aleatorios](algorithms/tree-based/random_forests.ipynb) | Ensembles: promediar muchos árboles que ven cada uno datos distintos |
| ★ 6 | [Gradient boosting](algorithms/tree-based/gradient_boosting.ipynb) | Árboles añadidos de uno en uno, cada uno corrigiendo los errores de los anteriores; tasa de aprendizaje y número de árboles; por qué es el primer modelo fuerte habitual con una tabla |
| ★ 7 | [XGBoost](algorithms/tree-based/xgboost.ipynb) | La biblioteca que usan la mayoría de los equipos para el gradient boosting: un objetivo regularizado, valores ausentes tratados de forma nativa, parada temprana con un conjunto de validación; LightGBM y CatBoost |
| ★ 8 | [Medir el error de un modelo de regresión](evaluation/regression_metrics.ipynb) | MAE, RMSE, R², errores porcentuales (MAPE) y la proporción de predicciones dentro del 10 %; una referencia (*baseline*) con la que comparar; qué medida responde a qué pregunta |

Después, con datos reales: ★ [Dividir por tiempo](https://github.com/avidaldo/king-county/blob/master/03-temporal_leakage.ipynb), en el ejemplo resuelto de King County. Con ventas de casas que abarcan año y medio, una división aleatoria deja que el modelo aprenda de ventas posteriores a aquellas con las que se le prueba; dividir por fecha mide lo que de verdad hará.

### Parte 2 · Vecinos y errores

| # | Notebook | Contenido |
| --- | --- | --- |
| ★ 9 | [k vecinos más cercanos](algorithms/neighbours/knn.ipynb) | Un modelo que guarda ejemplos en lugar de aprender parámetros, y predice a partir de los más parecidos; por qué importa el escalado; elegir *k* |
| ★ 10 | [Análisis de errores: dónde falla un modelo](evaluation/error_analysis.ipynb) | Mirar los errores en lugar de su media: por grupo, en un mapa, a lo largo del tiempo, en cada dirección; convertir lo que encuentres en la siguiente variable o el siguiente modelo |

### Parte 3 · Elegir un modelo con honestidad

| # | Notebook | Contenido |
| --- | --- | --- |
| ★ 11 | [Validación y selección de modelos](ml-fundamentals/validation_and_model_selection.ipynb) | Por qué elegir con el conjunto de prueba es una fuga; una división en tres partes; comparar modelos con el conjunto de validación y probar una sola vez |
| ★ 12 | [Viviendas de California con pipelines](basic-workflows/california_with_pipelines.ipynb) | El flujo de trabajo del 4 con los datos en bruto, como un pipeline: `Pipeline`, `ColumnTransformer`, `FunctionTransformer`; preprocesamiento ajustado solo con los datos de entrenamiento; cuatro modelos comparados con un conjunto de validación |
| 13 | [Controlar la complejidad: regularización](ml-fundamentals/regularization.ipynb) | La profundidad de un árbol, *k* y una penalización como el mismo tipo de ajuste; Ridge (L2) y Lasso (L1) frente a una curva sobreajustada |
| ★ 14 | [Validación cruzada y búsqueda de hiperparámetros](ml-fundamentals/cross_validation_and_search.ipynb) | Validación cruzada k-fold y ordenada en el tiempo; búsqueda en rejilla y aleatoria; por qué la prueba final se sigue haciendo una sola vez |
| ★ 15 | [Fuga de datos](ml-fundamentals/data_leakage.ipynb) | Cuatro demostraciones breves de una puntuación mejor por una evaluación peor: preprocesar antes de dividir, una variable que contiene el objetivo, el mismo ejemplo a ambos lados, información del futuro |

Después, el itinerario de [Preparación de datos](../data-preparation/README.md#itinerario): cuatro notebooks sobre valores ausentes, codificar categorías, escalado, y dónde termina la preparación de datos y empieza el modelado, cada paso dentro de los pipelines de esta parte.

Y si tienes tiempo: [Viviendas de California, de principio a fin](https://github.com/avidaldo/california_e2e), un proyecto completo que recorre las partes 1 y 3 con un mismo dataset ([Ejemplos resueltos](#ejemplos-resueltos) explica cómo se relaciona con los dos notebooks de California de arriba).

### Parte 4 · Clasificación

| # | Notebook | Contenido |
| --- | --- | --- |
| ★ 16 | [Descenso de gradiente](ml-fundamentals/gradient_descent.ipynb) | Ajustar un modelo bajando cuesta abajo por su error: la tasa de aprendizaje, por qué importa el escalado, pasos por lotes, estocásticos y por minilotes; comprobado con la solución exacta de la regresión lineal, y necesario después para la regresión logística, que no la tiene, y para toda red neuronal |
| ★ 17 | [Regresión logística](algorithms/linear-models/logistic_regression.ipynb) | La clasificación como una probabilidad: la sigmoide, una y varias variables, la frontera de decisión, más de dos clases |
| ★ 18 | [Evaluar un clasificador](evaluation/classification_metrics.ipynb) | Exactitud (*accuracy*), precisión, exhaustividad (*recall*), F1, la matriz de confusión, ROC y AUC; elegir una métrica |
| 19 | [Cuando una clase es rara](evaluation/imbalanced_classes.ipynb) | Regiones de mamografías, el 2 % con una calcificación: la exactitud que obtiene un modelo que siempre predice «no», una referencia, curvas de precisión-exhaustividad, mover el umbral, pesos de clase |
| 20 | [Diabetes Pima](basic-workflows/pima_diabetes.ipynb) | Un flujo de trabajo de clasificación con datos reales: ceros que representan valores ausentes, rellenados dentro del pipeline; un umbral elegido para el cribado; por qué hay que leer un dataset antes de escribir un pipeline |

Después, con datos reales: [Enfermedad de tiroides](https://github.com/avidaldo/thyroid), un ejemplo resuelto de clasificación con tres clases desequilibradas: métricas, referencias y boosting.

## Ejemplos resueltos

Proyectos más largos que aplican este tema a datos reales, cada uno en su propio repositorio. El itinerario de arriba indica cuándo leer cada uno.

- [Ventas de casas en King County](https://github.com/avidaldo/king-county): duplicados y fuga temporal. Su notebook sobre dividir por tiempo es básico, después de la parte 1; el resto del repositorio es opcional, y es el notebook al que volver con cualquier dato que cambie con el tiempo.
- [Viviendas de California](https://github.com/avidaldo/california_e2e): un proyecto de regresión de principio a fin, desde plantear el problema hasta un modelo ajustado, opcional. Usa los mismos 20 640 distritos que los dos notebooks de California del itinerario, en la versión de [Viviendas de California con pipelines](basic-workflows/california_with_pipelines.ipynb), que conserva los recuentos de cada distrito y una columna de texto, con algunos valores ausentes. Esos dos notebooks ensayan sus pasos a pequeña escala, cada paso explicado en esta carpeta; el repositorio es el proyecto completo, y su carpeta `notes/` vuelve a explicar cada paso, para que pueda leerse sin esta carpeta.
- [Enfermedad de tiroides](https://github.com/avidaldo/thyroid): clasificación con clases desequilibradas, métricas, referencias y boosting, después de la parte 4.

## Práctica

Opcional, y nunca se califica.

**¿Sobrevive a un desplazamiento?** Entrena un clasificador, como [k vecinos más cercanos](algorithms/neighbours/knn.ipynb) o [regresión logística](algorithms/linear-models/logistic_regression.ipynb), con 10 000 imágenes aplanadas de entrenamiento de MNIST. Mide su exactitud en el conjunto de prueba, y después con las mismas imágenes de prueba desplazadas 3 píxeles con la `shift_image` que escribiste en [numpy-mnist](https://github.com/avidaldo/numpy-mnist). Entrena otra vez añadiendo copias desplazadas al conjunto de entrenamiento, y vuelve a medir. ¿Qué dice la diferencia sobre los conjuntos de prueba y las condiciones reales?

## Profundizaciones

Opcionales y nunca se evalúan. El itinerario nunca depende de ellas.

| Profundización | Amplía | Contenido |
| --- | --- | --- |
| [Ensembles más allá de los árboles](algorithms/tree-based/deep-dives/ensembles_beyond_trees.ipynb) | 5, 6 | Votación, *stacking* y *bagging* de cualquier modelo, con el conjunto de validación de la parte 3: mejor leerla después de ella |
| [Pesos uniformes y por distancia](algorithms/neighbours/deep-dives/knn_weights.ipynb) | 9 | Cómo cambia la frontera de decisión al ponderar los vecinos por su distancia, y por qué eso deja sin sentido la exactitud de entrenamiento |
| [Naive Bayes, del teorema a un filtro de spam](deep-dives/naive-bayes/README.md) | 17 | Un clasificador que aprende contando, de la misma forma que la regresión logística, en tres notebooks: el teorema de Bayes con una palabra, contado a mano; un clasificador naive Bayes escrito en unas pocas líneas, idéntico al de scikit-learn; un filtro de spam comparado con la regresión logística, con un umbral según lo que cuesta cada error |
| [Un clasificador a fondo (MNIST)](evaluation/deep-dives/mnist_classifier_in_depth.ipynb) | 18 | Un detector de dígitos entrenado con descenso de gradiente estocástico, medido con validación cruzada; un clasificador para diez clases: uno contra el resto frente a uno contra uno |
| [Máquinas de vectores de soporte](deep-dives/svm.ipynb) | 9, 17 | El margen más amplio entre clases, vectores de soporte, márgenes blandos y `C`; kernels para fronteras que no son rectas; SVM para regresión |
| [Progresión de la diabetes](basic-workflows/deep-dives/diabetes_progression.ipynb) | 12, 14 | Un flujo de trabajo de regresión con los datos de diabetes de scikit-learn: lo que dice la documentación sobre variables que llegan ya escaladas |
| [Iris: un flujo de trabajo multiclase](basic-workflows/deep-dives/iris_multiclass.ipynb) | 17, 18 | Un flujo de trabajo de clasificación con tres clases: cuatro clasificadores comparados por validación cruzada, el elegido probado una sola vez; la matriz de confusión y el informe para tres clases; lo que no puede mostrar un dataset pequeño y fácil |
| scikit-learn desde cero *(próximamente)* | 12 | Construye una pequeña copia de scikit-learn, un principio de diseño cada vez, para ver por qué su API es como es: estimadores, transformadores, `get_params` y `clone`, `Pipeline`, búsqueda en rejilla |

## Temas relacionados

- [Preparación de datos](../data-preparation/README.md): su itinerario, después de la parte 3, cubre valores ausentes, codificación, escalado, y dónde termina la preparación de datos y empieza el modelado; sus profundizaciones van más allá, un notebook por paso (tipos de variables, exploración, correlación, valores atípicos, distribuciones asimétricas, variables nuevas); los flujos de trabajo básicos enlazan el paso que aplican
