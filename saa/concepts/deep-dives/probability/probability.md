# Probabilidad

La **probabilidad** mide lo seguro que es un suceso, como un número entre 0 (imposible) y 1 (seguro), a menudo escrito como porcentaje. Si la probabilidad de un suceso A es P(A), la probabilidad de que no ocurra es P(¬A) = 1 − P(A).

## La interpretación frecuentista

Para un frecuentista, la probabilidad de un suceso es la proporción de veces que ocurre cuando un experimento se repite muchas veces. Un dado no trucado saca un 6 con probabilidad 1/6 porque, a lo largo de muchas tiradas, aproximadamente una de cada seis es un 6. La probabilidad es una propiedad del experimento repetible, no del conocimiento de nadie.

El aprendizaje automático usa esta visión siempre que estima una probabilidad contando: la proporción de spam entre los emails de un conjunto de entrenamiento, o la tasa de error de un modelo en un conjunto de test. La estadística clásica, con sus contrastes de hipótesis e intervalos de confianza, se basa en ella.

## La interpretación bayesiana

Para un bayesiano, una probabilidad es un **grado de creencia** sobre algo incierto, que no tiene por qué ser repetible: la probabilidad de que llueva mañana, o de que un paciente concreto tenga una enfermedad. Una creencia empieza como probabilidad **a priori** y se actualiza a una probabilidad **a posteriori** a medida que llega la evidencia, con el [teorema de Bayes](bayes_theorem.md). Una previsión de lluvia para mañana, por ejemplo, combina lo a menudo que llueve en esta época del año con las mediciones de presión y humedad de hoy.

Esta visión es la base de las redes bayesianas que se usan en diagnóstico ([razonamiento con incertidumbre](../classical-ai/uncertainty.ipynb)), de los filtros de spam que actualizan sus creencias con cada email nuevo, y de los métodos que informan de lo incierta que es una predicción, no solo de la predicción.

Las dos visiones usan las mismas matemáticas. Se diferencian en lo que significa una probabilidad.

## Probabilidad condicionada

La probabilidad de un suceso A **dado** que ha ocurrido un suceso B se escribe P(A|B): por ejemplo, la probabilidad de que un paciente tenga una enfermedad dado que una prueba da positivo.

Saber que ocurrió B reduce el mundo de posibilidades, el **espacio muestral** Ω, a los resultados que hay en B. Dentro de él, A solo ocurre donde ocurren los dos, en A ∩ B:

![Dos sucesos A y B que se solapan en el espacio muestral Ω](img/conditional_probability.png)

$$ P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad \text{con } P(B) > 0 $$

Reordenada, da la probabilidad de que ocurran los dos sucesos:

$$ P(A \cap B) = P(A|B) \times P(B) $$

## La ley de la probabilidad total

Un suceso B ocurre o junto con A o junto con ¬A, nunca con los dos. Su probabilidad es por tanto la suma de los dos casos:

$$ P(B) = P(B \cap A) + P(B \cap \neg A) = P(B|A) \times P(A) + P(B|\neg A) \times P(\neg A) $$

La [prueba diagnóstica](diagnostic_test.md) la usa para calcular con qué frecuencia da positivo una prueba en general.

## Fuentes

- [What is probability? (Machine Learning Mastery)](https://machinelearningmastery.com/what-is-probability/) (en inglés)
- [Conditional probability, University of Washington CSE 312](https://courses.cs.washington.edu/courses/cse312/18wi/312A/lecture7.pdf) (en inglés)
- [Probabilidad condicionada explicada visualmente](https://setosa.io/ev/conditional-probability/) (en inglés)
