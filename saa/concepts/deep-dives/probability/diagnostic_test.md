# El teorema de Bayes aplicado a una prueba diagnóstica

En un grupo de población, el 0,02 % de las personas tiene cierto cáncer. Una prueba de cribado para detectarlo no siempre acierta: en las personas que tienen el cáncer da positivo el 85 % de las veces, y en las que no lo tienen, negativo el 95 % de las veces. Una persona da positivo. ¿Qué probabilidad hay de que tenga el cáncer?

## Los sucesos

- C: la persona tiene cáncer; ¬C: la persona no lo tiene.
- T: la prueba da positivo; ¬T: la prueba da negativo.

## Lo que sabemos

La probabilidad de tener el cáncer, antes de cualquier prueba, es la **prevalencia** de la enfermedad en la población, también llamada **tasa base**:

$$ P(C) = 0{,}0002 \qquad P(\neg C) = 1 - 0{,}0002 = 0{,}9998 $$

Una prueba puede fallar de dos formas, y cada una tiene una tasa que describe lo bien que la prueba la evita:

- Un **falso negativo**: la prueba da negativo aunque la persona tiene la enfermedad. La **sensibilidad** de la prueba, o tasa de verdaderos positivos, es la proporción de personas enfermas que detecta:

$$ \text{Sensibilidad} = P(T|C) = 0{,}85 \qquad P(\neg T|C) = 1 - 0{,}85 = 0{,}15 $$

- Un **falso positivo**: la prueba da positivo aunque la persona no tiene la enfermedad. La **especificidad** de la prueba, o tasa de verdaderos negativos, es la proporción de personas sanas que descarta correctamente, y la **tasa de falsos positivos** es su complementario:

$$ \text{Especificidad} = P(\neg T|\neg C) = 0{,}95 \qquad P(T|\neg C) = 1 - 0{,}95 = 0{,}05 $$

## La respuesta intuitiva, y por qué es errónea

La prueba detecta el 85 % de los cánceres, así que la intuición sugiere que un positivo significa un 85 % de probabilidad de cáncer. Eso es P(T|C), la probabilidad de un positivo *dado* el cáncer, y la pregunta pide lo contrario, P(C|T), la probabilidad de cáncer *dado* un positivo. Confundir las dos, y por tanto ignorar lo poco frecuente que es la enfermedad, tiene nombre: la **falacia de la tasa base**.

## Los cuatro resultados como un árbol

Cada persona tiene el cáncer o no, y después da positivo o negativo. La probabilidad de cada uno de los cuatro resultados es el producto de las probabilidades a lo largo de su camino:

![Árbol de probabilidad: cáncer o no, después una prueba positiva o negativa, con la probabilidad de cada uno de los cuatro resultados](img/cancer_test_tree.png)

Dos de los caminos terminan en una prueba positiva: un **verdadero positivo**, C ∩ T, y un **falso positivo**, ¬C ∩ T.

## El teorema de Bayes

El [teorema de Bayes](bayes_theorem.md) convierte la probabilidad que conocemos, P(T|C), en la que queremos, P(C|T):

$$ P(C|T) = \frac{P(T|C) \times P(C)}{P(T)} = \frac{0{,}85 \times 0{,}0002}{P(T)} $$

## ¿Con qué frecuencia da positivo la prueba?

El problema no da P(T), la proporción de todas las pruebas que salen positivas. Un positivo es o un verdadero positivo o un falso positivo, y cada una de estas probabilidades conjuntas es una probabilidad condicionada por la probabilidad de su condición, así que por la [ley de la probabilidad total](probability.md#la-ley-de-la-probabilidad-total):

$$ P(T) = P(T \cap C) + P(T \cap \neg C) = P(T|C) \times P(C) + P(T|\neg C) \times P(\neg C) $$

$$ P(T) = 0{,}85 \times 0{,}0002 + 0{,}05 \times 0{,}9998 = 0{,}00017 + 0{,}04999 = 0{,}05016 $$

## La respuesta

$$ P(C|T) = \frac{P(T|C) \times P(C)}{P(T|C) \times P(C) + P(T|\neg C) \times P(\neg C)} = \frac{0{,}00017}{0{,}05016} \approx 0{,}0034 $$

Después de un positivo, la probabilidad de tener el cáncer sube del 0,02 % a aproximadamente el 0,34 %: unas diecisiete veces más alta, y aun así muy improbable.

## El mismo cálculo en personas

La razón se ve más fácil con recuentos que con probabilidades. De cada 100.000 personas que se hacen la prueba:

| | Positivo | Negativo | Total |
| --- | ---: | ---: | ---: |
| Tienen el cáncer | 17 | 3 | 20 |
| No lo tienen | 4.999 | 94.981 | 99.980 |
| Total | 5.016 | 94.984 | 100.000 |

De las 5.016 personas que dan positivo, solo 17 tienen el cáncer: 17 / 5.016 ≈ 0,0034. La prueba es buena, pero las personas sanas son tantísimas más que su 5 % de falsos positivos supera con mucho a los verdaderos positivos.

Un negativo mueve la probabilidad en el otro sentido: de las 94.984 personas que dan negativo, 3 tienen el cáncer, así que P(C|¬T) = 3 / 94.984 ≈ 0,00003.

## Cuánto importa la prevalencia

Con la misma prueba, una prevalencia del 2 % en lugar del 0,02 % da:

$$ P(C|T) = \frac{0{,}85 \times 0{,}02}{0{,}85 \times 0{,}02 + 0{,}05 \times 0{,}98} \approx 0{,}26 $$

Un positivo significa ahora un 26 % de probabilidad de cáncer. Nada de la prueba ha cambiado, solo el grupo en el que se usó, y con él el significado de un positivo. Por eso los programas de cribado se dirigen a los grupos en los que una enfermedad es más frecuente, y por eso las predicciones de un modelo hay que leerlas teniendo en cuenta lo frecuente que es cada clase: lo mismo vale para un filtro de spam o un detector de fraude.

## Más recursos

- [3Blue1Brown: The medical test paradox, and redesigning Bayes' rule](https://www.youtube.com/watch?v=lG4VkPoG3ko) (en inglés)
- [Veritasium: The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg) ([doblado al español](https://www.youtube.com/watch?v=D7KKlC0LOyw))
- [Matemáticas con Juan: un problema parecido, resuelto](https://www.youtube.com/watch?v=n11NDXIIcLI) (en español)
- [Falacia de la tasa base](https://es.wikipedia.org/wiki/Falacia_de_la_tasa_base)
