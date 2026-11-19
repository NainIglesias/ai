# Lo esencial de Python para datos: NumPy y pandas

Las dos bibliotecas en las que se apoya casi cualquier proyecto de IA en Python: NumPy para arrays numéricos y pandas para tablas. Esta carpeta cubre lo que necesitas para cargar, inspeccionar, seleccionar, remodelar y combinar los datos de tus proyectos.

## Itinerario

| # | Nivel | Elemento | Contenido |
| --- | --- | --- | --- |
| 1 | ★ básico | [NumPy](numpy/numpy1.ipynb) | Arrays y sus tipos de datos, crear arrays, indexación y *slicing*, cambiar la forma, números aleatorios |
| | apoyo | [Listas frente a arrays de NumPy: ejercicios](numpy/complementary/lists_nd_arrays_examples.ipynb) | Funciones pequeñas resueltas con listas normales y con NumPy |
| 2 | estándar | [NumPy para operaciones algebraicas](numpy/numpy2_algebra.ipynb) | Matriz identidad y traspuesta, operaciones con matrices, `@` y `np.dot` |
| | apoyo | [Matrices y tensores en IA](https://github.com/avidaldo/compare-python-c-efficiency/blob/main/02_matrices_in_ai.ipynb) | De los números sueltos a los tensores; el producto escalar y la multiplicación de matrices, y por qué la IA es sobre todo eso. Antes de los ejercicios, si una imagen de 7×7 como matriz te resulta nueva |
| | proyecto | [numpy-mnist](https://github.com/avidaldo/numpy-mnist), el repositorio del que hiciste fork en la etapa 1 | Un par de docenas de ejercicios sobre dígitos manuscritos como un array de 60.000×28×28, con tests que comprueban tus respuestas |
| | apoyo | [Indexación avanzada (*fancy indexing*), paso a paso](numpy/complementary/fancy_indexing_step_by_step.ipynb) | Indexar con arrays de índices y *broadcasting* sobre arrays lo bastante pequeños para imprimirlos, hasta tres arrays de índices que recortan una ventana distinta de cada imagen |
| | profundización | [Desplazar todas las imágenes sin un bucle](https://github.com/avidaldo/numpy-mnist/blob/main/vectorised_shift.ipynb), en numpy-mnist | El desplazamiento del ejercicio 22 vectorizado, comprobado contra el bucle y cronometrado por partes |
| 3 | ★ básico | [pandas: Series y DataFrame](pandas/pandas_structures.ipynb) | Las dos estructuras de pandas y su relación con los arrays de NumPy |
| | apoyo | [Un DataFrame a partir de distintas estructuras](pandas/complementary/df_from_structures.ipynb) | Construir un mismo DataFrame a partir de listas, diccionarios y arrays |
| 4 | ★ básico | [Operaciones con DataFrames](pandas/pandas_dataframe_op.ipynb) | Gestionar columnas y filas, seleccionar y hacer *slicing*, filtrar, ordenar, agregaciones básicas |
| 5 | ★ básico | [Transformaciones y remodelado de DataFrames](pandas/pandas_transformations.ipynb) | `map`, `apply` y `transform`, agrupar, `assign`, remodelar con `melt` y `pivot` |
| | proyecto | [Asistente de normativa](https://github.com/avidaldo/fp-regulations-assistant), el proyecto de PIA | Haz fork y lee su README. Desde el final de esta etapa, el grupo lo mejora paso a paso a lo largo del curso, cada paso anunciado en el foro |
| | profundización | Las profundizaciones de [Preparación de datos](../../saa/data-preparation/README.md#itinerario) | Un paso de la preparación de datos para un modelo por notebook: explorar un dataset, correlación, valores atípicos, distribuciones asimétricas…, cada uno en ese itinerario después del paso que amplía. El itinerario de Preparación de datos llega más adelante, con el aprendizaje supervisado |

## Referencias

- [NumPy: lo más básico para principiantes](https://numpy.org/doc/stable/user/absolute_beginners.html) (en inglés)
- [Chuleta de pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) (oficial, en inglés)
