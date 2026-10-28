# Por qué Python domina la IA

## El enigma

Python es uno de los lenguajes populares más lentos. Es interpretado: cada línea se traduce mientras el programa se ejecuta, así que un bucle va decenas de veces más lento que el mismo bucle compilado desde C. Y la IA es, sobre todo, multiplicación de matrices, repetida billones de veces: cada capa de una red neuronal y cada paso de la atención de un *transformer* multiplica matrices. Entonces, ¿cómo puede ser Python el lenguaje principal de la IA?

## La respuesta: Python describe, el código compilado calcula

En la práctica, Python casi nunca hace el cálculo pesado de un programa de IA. **Describe** qué hay que calcular y **llama** a bibliotecas que lo hacen, y esas bibliotecas están escritas en lenguajes compilados y se ejecutan en hardware diseñado para esa tarea:

```text
┌──────────────────────────────────────────────────────────────┐
│ Python: notebooks, scripts de entrenamiento, prep. de datos  │  ← donde trabajan los desarrolladores de IA
├──────────────────────────────────────────────────────────────┤
│ Bibliotecas: NumPy, pandas, scikit-learn, PyTorch, TensorFlow│  ← interfaz en Python, núcleo compilado
├──────────────────────────────────────────────────────────────┤
│ Motores compilados: BLAS (C, Fortran), cuBLAS (CUDA), C++    │  ← código ajustado por expertos
├──────────────────────────────────────────────────────────────┤
│ Hardware: núcleos de CPU, GPU con miles de núcleos           │
└──────────────────────────────────────────────────────────────┘
```

Esto es lo que significa decir que Python es un **lenguaje pegamento**: conecta componentes rápidos escritos en otros lenguajes. La lentitud de su intérprete cuesta un poco en cada llamada, pero nada en los miles de millones de operaciones que se hacen dentro de cada llamada.

Un lenguaje pegamento es un tipo de **lenguaje de scripting**: uno pensado para escribir programas rápidamente, que se ejecutan al momento, sin paso de compilación, y que manejan otro software. Los puntos fuertes de Python son los de un buen lenguaje de scripting, y son la razón por la que los desarrolladores de IA trabajan en Python y no en C:

- **Es fácil de leer y escribir.** Su código se parece al pseudocódigo, así que científicos, analistas y estudiantes que no son programadores profesionales pueden usarlo, y los programas son cortos: no hay tipos que declarar ni memoria que gestionar.
- **Es interactivo.** Los notebooks y el intérprete ejecutan un trozo de código y muestran el resultado al instante, que es lo que exige explorar datos y probar ideas.
- **Se conecta fácilmente con código compilado.** Las bibliotecas escritas en C, C++ o Fortran se pueden llamar desde Python, mediante su interfaz de C y herramientas como Cython, ctypes y pybind11. Esto es lo que le permite ser el pegamento.
- **Tiene el ecosistema y la comunidad.** NumPy, pandas, scikit-learn, PyTorch y Hugging Face se usan todos desde Python, y los nuevos modelos, tutoriales y código de investigación se publican primero en Python. Como todo el mundo lo usa, la mayoría de cursos, respuestas y ejemplos están en Python, lo que atrae todavía a más usuarios.

## El recorrido en cifras

La misma multiplicación de dos matrices grandes, medida en un mismo ordenador. Otros ordenadores dan otras cifras, pero proporciones parecidas.

| Cómo se multiplicaron las matrices | GFLOPS (miles de millones de operaciones por segundo) | Comparado con Python puro |
|---|---|---|
| Python puro, tres bucles anidados | 0,11 | 1× |
| C, los mismos tres bucles | 2,4 | unas 20× |
| C, bucles reordenados para leer la memoria en orden | 35 | unas 300× |
| NumPy (BLAS, todos los núcleos de la CPU) | 500 | unas 5.000× |
| Un kernel de CUDA escrito a mano en la GPU (números de 32 bits) | 1.500 | unas 15.000× |
| cuBLAS en la GPU (números de 32 bits) | 17.000 | unas 150.000× |
| cuBLAS en la GPU (números de 16 bits, *tensor cores*) | 49.000 | unas 450.000× |

De la primera fila a la última, la misma operación va casi medio millón de veces más rápido. Y cada fila de NumPy hacia abajo se lanza con una sola línea de Python.

## Qué pasa en un flujo de trabajo real de IA

Piensa en un paso del entrenamiento de una red neuronal con PyTorch. En Python, quien programa escribe algo como «coge este lote de ejemplos, pásalo por el modelo, mide el error, ajusta los pesos». Cada una de esas frases es una o unas pocas llamadas de Python. Detrás de ellas, el núcleo en C++ de PyTorch decide qué hacer, y cuBLAS y otras bibliotecas de CUDA hacen miles de millones de multiplicaciones en la GPU. La parte de Python de cada paso tarda microsegundos; la parte de la GPU tarda milisegundos. La lentitud de Python simplemente no es donde se va el tiempo.

Lo mismo ocurre fuera del aprendizaje profundo: pandas ejecuta sus operaciones con tablas en C, y scikit-learn entrena sus modelos en Cython, C y C++.

## Por qué funciona la combinación

- **Cada lenguaje hace lo que mejor sabe hacer.** Python para escribir y probar ideas rápidamente; C, C++ y CUDA para calcular a la velocidad del hardware.
- **Los expertos optimizan una vez y todos se benefician.** Un puñado de especialistas ajusta BLAS y cuBLAS para cada nuevo procesador, y todo programa de Python que multiplica matrices se vuelve más rápido sin cambiar una línea.
- **El hardware sigue mejorando por debajo.** Cuando llega una GPU nueva, las bibliotecas se actualizan para usarla, y el código de Python escrito años antes funciona en ella sin cambios.

## El límite: cuando el propio pegamento es lento

La combinación falla cuando un programa hace su trabajo pesado en bucles de Python en lugar de en llamadas a bibliotecas: por ejemplo, procesar un dataset valor a valor en un bucle `for`. Entonces el intérprete vuelve a estar en el camino del trabajo. La solución casi siempre es la misma: expresar el trabajo como operaciones sobre arrays o tablas completos (**vectorización**, que [Lo esencial de Python para datos](../python-data-essentials/README.md) practica con NumPy y pandas) o, cuando ninguna función de biblioteca encaja, compilar esa parte con una herramienta como Numba.

## Python se está volviendo más rápido, y eso no cambia el panorama

El propio CPython se está acelerando. Python 3.13 trajo una build experimental *free-threaded* sin el bloqueo global del intérprete (GIL), para que los hilos puedan ejecutar código de Python en varios núcleos a la vez, y un compilador *just-in-time* experimental; en la 3.14 la build *free-threaded* pasó a tener soporte oficial, aunque sigue siendo opcional ([PEP 779](https://peps.python.org/pep-0779/)). Esto ayuda a los programas cuyo tiempo se va en el propio código de Python. No cambia el reparto de trabajo anterior: el cálculo pesado de la IA sigue ejecutándose en bibliotecas compiladas.

## Mídelo tú mismo

[compare-python-c-efficiency](https://github.com/avidaldo/compare-python-c-efficiency) construye cada fila de la tabla anterior en notebooks que puedes ejecutar: la misma multiplicación en Python y en C, NumPy llamando a BLAS, y CUDA en una GPU, con notebooks opcionales sobre memoria, compiladores y rendimiento de GPU. Necesita un compilador de C, y una GPU de NVIDIA o Google Colab para la parte de GPU.
