# La vida de un proyecto de aprendizaje automático

Entrenar un modelo es una parte pequeña de un proyecto de aprendizaje automático. La mayor parte del trabajo se va en plantear el problema, conseguir unos datos correctos y comprobar que el modelo de verdad funciona. Los pasos forman un ciclo, porque lo que aprendes en un paso a menudo te devuelve a uno anterior:

```text
plantear el problema → obtener y explorar los datos → preparar los datos → entrenar y ajustar → evaluar → desplegar y monitorizar
```

## Los pasos

### Plantear el problema

- **Qué se predice exactamente,** para quién, y qué decisión cambia la predicción.
- **Cómo se mide el éxito:** una medida que importe a quienes usan el modelo, como menos préstamos impagados, y una métrica del modelo que la siga, elegida antes de entrenar ningún modelo.
- **Una referencia (*baseline*):** la respuesta más sencilla posible, como el precio medio de todas las casas, o la clase más frecuente. Un modelo solo vale lo que cuesta si la supera claramente.
- **Si hace falta aprendizaje automático:** si unas pocas reglas claras resuelven el problema, escribe las reglas ([reglas y sistemas expertos](../deep-dives/classical-ai/rules_and_expert_systems.ipynb)).

### Obtener y explorar los datos

- De dónde vienen los datos, qué significa cada columna y cómo se midió, y cuántos hay.
- **Exploración** (*análisis exploratorio de datos*, EDA): la distribución de cada columna, las relaciones entre columnas, y los problemas: valores ausentes, errores, duplicados, valores extremos. Las herramientas son las de [Lo esencial de Python para datos](../../../pia/python-data-essentials/README.md).
- *Garbage in, garbage out* (si entra basura, sale basura): ningún modelo puede encontrar una respuesta que los datos no contienen.

### Preparar los datos

- **Aparta primero el conjunto de test,** antes de decidir nada a partir de los datos (consulta la [generalización](#generalización-el-problema-central) más abajo).
- Limpia los datos, codifica las categorías como números, escala, y crea las características que ayudan al modelo (*feature engineering*), decidiendo cada paso solo con los datos de entrenamiento. La profundización sobre preparación de datos *(próximamente)* recorre cada uno de ellos.

### Entrenar y ajustar

- Elige unos pocos algoritmos candidatos que encajen con la tarea y los datos ([elegir el algoritmo adecuado](ml_algorithms_history.md#elegir-el-algoritmo-adecuado)).
- Entrena cada uno y ajusta sus hiperparámetros con datos de validación, nunca con el conjunto de test.

### Evaluar

- Mide el modelo elegido en el conjunto de test, una sola vez, con la métrica elegida al principio, y compáralo con la referencia.
- Lee los errores: qué ejemplos fallan y por qué. Comprueba que el modelo funciona igual de bien para los distintos grupos de personas a los que afecta.
- Si no es lo bastante bueno, vuelve atrás: más datos o mejores, otras características, otro modelo.

### Desplegar y monitorizar

- **Pon el modelo donde se usa:** predicciones por lotes (cada noche, para cada cliente), bajo demanda detrás de una API web (cada vez que se envía un formulario), o en un dispositivo como un móvil. Este es el tema sobre servir modelos *(próximamente)*.
- **Vigílalo mientras se usa.** El mundo cambia, y un modelo entrenado con los datos del año pasado empeora poco a poco: esto se llama *deriva* (*drift*). Sigue su rendimiento, y vuelve a entrenarlo con datos recientes cuando baje.

## Generalización: el problema central

El objetivo no es ajustarse a los datos de entrenamiento, sino predecir bien para ejemplos que el modelo nunca ha visto: **generalizar**. Un modelo puede ser perfecto con sus datos de entrenamiento memorizándolos y aun así fallar con datos nuevos, así que su puntuación con los datos de entrenamiento no demuestra nada. Tres modelos que predicen el precio de una casa a partir de su superficie:

| Modelo | Error con sus datos de entrenamiento | Error con datos nuevos | Diagnóstico |
| --- | --- | --- | --- |
| Una línea recta, cuando el precio crece más rápido que la superficie | Alto | Alto | **Subajuste** (*underfitting*): demasiado sencillo para captar el patrón |
| Un modelo de la complejidad adecuada | Bajo | Bajo, algo más alto | Un buen ajuste |
| Un árbol que crece hasta que cada hoja contiene una sola casa | Casi cero | Alto | **Sobreajuste** (*overfitting*): aprendió el ruido de sus ejemplos, no solo el patrón |

Por eso los datos se dividen en tres conjuntos:

- el **conjunto de entrenamiento**, para ajustar los parámetros del modelo;
- el **conjunto de validación**, para elegir entre modelos e hiperparámetros; la *validación cruzada* hace lo mismo turnándose con partes del conjunto de entrenamiento;
- el **conjunto de test**, guardado aparte y usado una sola vez, al final. Un conjunto de test que se ha usado para elegir un modelo ya no mide datos nuevos, y da una puntuación optimista.

La **fuga de datos** (*data leakage*) es el mismo error disfrazado: se cuela en el entrenamiento información que el modelo no tendrá cuando prediga. Dos ejemplos: escalar los datos con la media de todos ellos, incluido el conjunto de test; o predecir si se devolverá un préstamo con una característica que solo se conoce después, como la fecha en que se dio por incobrable. Una puntuación que parece demasiado buena para ser verdad normalmente lo es.

Cómo medir todo esto, y cómo evitar estos errores, es el núcleo del aprendizaje supervisado *(próximamente)*.
