# Lo esencial de Python para datos: NumPy y pandas

Las dos bibliotecas en las que se apoya casi cualquier proyecto de IA en Python: NumPy para arrays numéricos y pandas para tablas. Esta carpeta cubre lo que necesitas para cargar, inspeccionar, seleccionar, remodelar y combinar los datos de tus proyectos, para encontrar los problemas que tiene una tabla y para obtener datos de la web. La preparación de datos más a fondo para el aprendizaje automático (explorar un dataset, valores ausentes, valores atípicos, codificación, escalado) es la profundización *Preparación de datos* *(próximamente)*, un notebook por paso: empieza donde termina *Encontrar los problemas de una tabla*, con las decisiones que dependen de los datos.

## Itinerario

★ marca los elementos básicos: el mínimo, si tienes poco tiempo esta semana.

| # | Notebook | Contenido |
| --- | --- | --- |
| ★ 1 | [NumPy](numpy/numpy1.ipynb) | Arrays y sus tipos de datos, crear arrays, indexación y *slicing*, cambiar la forma, números aleatorios |
| 2 | [NumPy para operaciones algebraicas](numpy/numpy2_algebra.ipynb) | Matriz identidad y traspuesta, operaciones con matrices, `@` y `np.dot` |
| ★ 3 | [pandas: Series y DataFrame](pandas/pandas_structures.ipynb) | Las dos estructuras de pandas y su relación con los arrays de NumPy |
| ★ 4 | [Operaciones con DataFrames](pandas/pandas_dataframe_op.ipynb) | Gestionar columnas y filas, seleccionar y hacer *slicing*, filtrar, ordenar, agregaciones básicas |
| ★ 5 | [Transformaciones y remodelado de DataFrames](pandas/pandas_transformations.ipynb) | `map`, `apply` y `transform`, agrupar, `assign`, remodelar con `melt` y `pivot` |
| ★ 6 | Encontrar los problemas de una tabla *(próximamente)* | Valores ausentes de dos tipos (vacíos y de relleno), duplicados, valores imposibles, tipos incorrectos, la misma cosa escrita de dos formas; inspeccionar antes de decidir, y dejar la decisión por escrito |
| ★ 7 | Texto y fechas *(próximamente)* | Los métodos `.str`, expresiones regulares para los casos habituales, tildes y codificaciones rotas, marcas de tiempo escritas en dos formatos, zonas horarias |
| ★ 8 | Datos de la web: APIs, JSON y XML *(próximamente)* | Llamar a una API web con parámetros y paginación, guardar las respuestas en bruto, ser educado con el servidor; JSON y JSON Lines a un DataFrame; leer XML con la biblioteca estándar |

## Ejercicios

[Las imágenes son arrays: MNIST con NumPy](https://github.com/avidaldo/numpy-mnist) es un repositorio propio: un par de docenas de ejercicios sobre dígitos manuscritos como un array de 60.000×28×28 (cambiar la forma, tipos de datos y desbordamiento, codificación one-hot, normalización sin fuga de datos, bucles frente a vectorización, aumento de datos a mano), con tests que comprueban tus respuestas, integración continua en tu fork y una solución. Si una imagen de 7×7 como matriz te resulta nueva, empieza por el notebook [Matrices y tensores en IA](https://github.com/avidaldo/compare-python-c-efficiency/blob/main/02_matrices_in_ai.ipynb) del repositorio compare-python-c-efficiency.

## Profundizaciones

Opcionales y nunca se evalúan. El itinerario nunca depende de ellas.

| Notebook | Amplía | Contenido |
| --- | --- | --- |
| [Listas frente a arrays de NumPy: ejercicios](numpy/deep-dives/lists_nd_arrays_examples.ipynb) | 1 | Funciones pequeñas resueltas con listas normales y con NumPy |
| [Un DataFrame a partir de distintas estructuras](pandas/deep-dives/df_from_structures.ipynb) | 3 | Construir un mismo DataFrame a partir de listas, diccionarios y arrays |

## Referencias

- [NumPy: lo más básico para principiantes](https://numpy.org/doc/stable/user/absolute_beginners.html) (en inglés)
- [Chuleta de pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) (oficial, en inglés)
