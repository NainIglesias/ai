# Convenciones de la traducción

La rama `traduccion-es` traduce [avidaldo/ai](https://github.com/avidaldo/ai). El README indica el último commit traducido (`hasta el commit <sha>`).

## Qué se traduce

- **Markdown** (`.md` y celdas markdown de los notebooks): todo el texto.
- **Código**: solo los comentarios (`# ...`) y los docstrings.
- **Ficheros `.py` auxiliares**: docstrings y comentarios.

## Qué NO se traduce

- El código, los nombres de variables y funciones, y las cadenas de texto dentro del código.
- Las **salidas** de las celdas. El notebook no se vuelve a ejecutar.
- Los **nombres de ficheros y carpetas**. Los enlaces siguen apuntando a `foo.ipynb`.
- `requirements.txt`, `.gitignore` y la configuración.
- Las URLs externas.
- Las citas bibliográficas (títulos de artículos y libros).

## Palabras que se dejan en inglés

notebook, dataset, pipeline, gradient boosting, ensemble, scikit-learn, pandas, NumPy, XGBoost, *underflow*, *weight decay*.

Si el término inglés ayuda a buscar más información, se añade en cursiva entre paréntesis la primera vez: «variable (*feature*)», «codificación por objetivo (*target encoding*)».

## Términos

| Inglés | Español |
| --- | --- |
| feature | variable |
| target | objetivo |
| deep dive | profundización |
| (coming) | (próximamente) |
| Path (sección del README) | Itinerario |
| worked examples | ejemplos resueltos |
| accuracy | exactitud |
| precision | precisión |
| recall | exhaustividad |
| missing value | valor ausente |
| outlier | valor atípico |
| capped (valor) | topado |
| fold | pliegue |
| train / validation / test set | conjunto de entrenamiento / validación / prueba |
| overfitting / underfitting | sobreajuste / subajuste |
| leakage | fuga de datos |
| scaling | escalado |
| encoding | codificación |
| tuning / hyperparameter search | ajuste / búsqueda de hiperparámetros |
| greedy | voraz |
| random forest | bosque aleatorio |
| k-nearest neighbours | k vecinos más cercanos |
| support vector machine | máquina de vectores de soporte |

## Estilo

- **Números**: la coma es el separador decimal y el espacio fino separa los miles: `0,48`, `20 640`, `12 400 $`. **Dentro de LaTeX y de código no se tocan**: `$\alpha = 0.001$` se queda igual.
- **Títulos de notebooks citados en el texto**: se traducen y van en cursiva, igual que en el original (*El filtro de spam con scikit-learn*).
- **Tono**: el mismo que el original, de tú al lector, frases directas y sin añadidos.

## Anclajes

GitHub genera el anclaje a partir del encabezado:
- lo pasa a minúsculas;
- quita la puntuación;
- convierte los espacios en guiones;
- **conserva las tildes**.

Al traducir un encabezado hay que actualizar todos los enlaces que apuntan a él, también los de otros ficheros. Por ejemplo, `#why-scaling-matters` pasa a ser `#por-qué-importa-el-escalado`. `check.py` detecta los anclajes rotos.

## Herramientas

- `nbtr.py extract NB.ipynb segs.txt`: extrae lo traducible de un notebook en segmentos `@@ <celda>` (celda markdown entera) o `@@ <celda>:<línea>` (comentario de una línea de código).
- `nbtr.py apply NB.ipynb segs.txt`: escribe los segmentos traducidos en el notebook sin tocar nada más. Falla si sobran o faltan segmentos.
- `check.py`: comprueba que el código (sin comentarios ni docstrings) y las salidas son idénticos a upstream, y que no hay enlaces ni anclajes rotos.
- `pendiente.sh`: lista lo que ha cambiado en upstream desde el commit del README.
