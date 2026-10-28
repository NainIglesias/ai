# Teorema de Bayes

El teorema de Bayes dice cómo actualizar la probabilidad de una hipótesis cuando llega evidencia nueva.

## El teorema

Para una hipótesis A y una evidencia B, con P(B) > 0:

$$ P(A|B) = \frac{P(B|A) \times P(A)}{P(B)} $$

Cada término tiene un nombre:

- **P(A)**, la probabilidad **a priori** (*prior*): lo probable que era la hipótesis antes de la evidencia.
- **P(B|A)**, la **verosimilitud** (*likelihood*): lo probable que es la evidencia si la hipótesis es cierta.
- **P(B)**, la **evidencia**: lo probable que es la evidencia en general, sea cierta la hipótesis o no. La [ley de la probabilidad total](probability.md#la-ley-de-la-probabilidad-total) la calcula como P(B|A) × P(A) + P(B|¬A) × P(¬A).
- **P(A|B)**, la probabilidad **a posteriori** (*posterior*): lo probable que es la hipótesis después de la evidencia.

En palabras: la probabilidad a posteriori es la a priori multiplicada por P(B|A) / P(B), cuántas veces más probable es la evidencia si la hipótesis es cierta que en general. Una evidencia mucho más probable bajo la hipótesis aumenta su probabilidad; una evidencia igual de probable en ambos casos la deja igual.

## De dónde sale

El teorema se deduce en dos líneas de la definición de [probabilidad condicionada](probability.md#probabilidad-condicionada). La probabilidad de que ocurran tanto A como B se puede escribir de dos formas:

$$ P(A \cap B) = P(A|B) \times P(B) \qquad P(A \cap B) = P(B|A) \times P(A) $$

Los dos lados derechos son iguales, así que dividiendo entre P(B):

$$ P(A|B) \times P(B) = P(B|A) \times P(A) \quad\Rightarrow\quad P(A|B) = \frac{P(B|A) \times P(A)}{P(B)} $$

Un ejemplo resuelto con números: [una prueba diagnóstica](diagnostic_test.md).

## El teorema de Bayes en la inteligencia artificial

El teorema es la base de dos ideas en IA, que se diferencian en de dónde vienen las probabilidades:

- Las **redes bayesianas** razonan con probabilidades que escribe un experto, y las actualizan con el teorema a medida que llega la evidencia: por ejemplo, la probabilidad de un robo cuando salta una alarma. Un ejemplo completo: [razonamiento con incertidumbre](../classical-ai/uncertainty.ipynb).
- El clasificador **naive Bayes** estima esas probabilidades contando en datos etiquetados, así que es aprendizaje supervisado. Su aplicación clásica es el filtro de spam: la probabilidad de que un email sea spam dadas las palabras que contiene. Es una profundización de aprendizaje supervisado *(próximamente)*.

## Más recursos

- [3Blue1Brown: Bayes' theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) (en inglés)
- [Jesús Conde: teoría de la probabilidad y teorema de Bayes para machine learning](https://www.youtube.com/watch?v=foBVe1MuT5s) (en español)
- [Matemáticas profe Alex: teorema de Bayes](https://www.youtube.com/watch?v=bDfCURXoKkU&list=PLeySRPnY35dH7Pnamtm2xxaCuT6jxt1vn&index=28) (en español)
