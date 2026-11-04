# Naive Bayes, del teorema a un filtro de spam

Con dos clases, naive Bayes es un clasificador de la misma forma que la [regresión logística](../../algorithms/linear-models/logistic_regression.ipynb), pero fija sus pesos contando las palabras de cada clase en lugar de minimizando un error.

Un filtro de spam construido tres veces, cada vez con menos código y más comprensión: primero el teorema de Bayes con una sola palabra, contado a mano; después un clasificador naive Bayes completo en unas pocas líneas de Python, comprobado con el de scikit-learn; por último el filtro como un pipeline de scikit-learn, comparado con la regresión logística, ajustado según lo que cuesta cada error, y examinado mensaje a mensaje.

Los datos son la SMS Spam Collection: 5574 mensajes de texto reales etiquetados como spam o ham (legítimos), que se descargan la primera vez que se usan desde el [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)); no se guardan con los notebooks.

## Notebooks

| # | Notebook | Contenido |
| --- | --- | --- |
| 1 | [El teorema de Bayes, palabra a palabra](one_word.ipynb) | Probabilidad a priori, verosimilitudes y probabilidad a posteriori, contadas en los mensajes para una palabra; por qué la probabilidad a posteriori coincide con contar directamente, y por qué la a priori importa tanto como la palabra |
| 2 | [Un clasificador naive Bayes a mano](naive_bayes_by_hand.ipynb) | Por qué se eliminan los mensajes repetidos antes de dividir; la suposición ingenua, medida; recuentos de palabras por clase; suavizado para palabras que una clase nunca ha visto; logaritmos contra el *underflow*; el clasificador como una clase con las convenciones de scikit-learn, idéntico a `MultinomialNB` |
| 3 | [El filtro de spam con scikit-learn](spam_filter_scikit_learn.ipynb) | Recuentos, presencia, TF-IDF y pares de palabras, frente a una regresión logística, por validación cruzada; un umbral según lo que cuesta cada error; los mensajes en los que se equivoca; las palabras que más pesan, y lo que revelan sobre cómo se recogieron los datos; dónde está hoy naive Bayes |

Los notebooks explican la probabilidad que usan; la deducción del teorema está en la profundización [Probabilidad y teorema de Bayes](../../../concepts/deep-dives/probability/README.md). El notebook 3 usa los pipelines, la validación cruzada y las métricas de clasificación del itinerario de Aprendizaje supervisado.

## Configuración

Los paquetes son los del `requirements.txt` del repositorio del curso. Abre los notebooks desde esta carpeta, para que `from sms_spam import load_sms_spam` encuentre el cargador; la primera ejecución descarga los datos (unos 200 KB) en `data/`.

## Para ir más allá

- Sustituye los marcadores `&lt;#&gt;` y `&lt;URL&gt;`, y las formas coloquiales que solo usa una clase, antes de vectorizar, y mide cuánta de la exactitud del filtro venía de ellos.
- Entrena el filtro con parte de los mensajes y actualízalo con el resto usando `MultinomialNB.partial_fit`, un lote cada vez, como haría un filtro en un móvil. `partial_fit` no puede aprender palabras que nunca ha visto, así que el vocabulario tiene que fijarse de antemano: `HashingVectorizer(alternate_sign=False)` en lugar de `CountVectorizer`.
- Calibra las probabilidades con `CalibratedClassifierCV` y compara su histograma con el de *El filtro de spam con scikit-learn*.

## Origen de los datos

Almeida, T. A., Gómez Hidalgo, J. M. y Yamakami, A. (2011). Contributions to the study of SMS spam filtering: new collection and results. *Proceedings of the 11th ACM Symposium on Document Engineering*, 259–262. La colección está en el [UCI Machine Learning Repository](https://doi.org/10.24432/C5CC84) y en [la página de sus autores](http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/).
