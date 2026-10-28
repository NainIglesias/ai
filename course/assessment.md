# Cómo se te evalúa

SAA y PIA dan cada uno su propia nota, y los dos se evalúan de la misma forma: **tu nota sale de exámenes presenciales**, y las contribuciones aceptadas a los repositorios del curso pueden sumar hasta 2 puntos.

## Los exámenes

| Examen | SAA | PIA | Qué abarca |
| --- | --- | --- | --- |
| Febrero | mar 2 feb | jue 4 feb | Primer trimestre (etapas 1–7). **Es el ensayo de mayo:** obligatorio y calificado, y puede subir tu nota (ver abajo) |
| Mayo | lun 24 may | mié 26 may | **Todo el curso.** Da tu nota |
| Junio | jue 10 jun | lun 14 jun | Lo mismo que mayo, como segunda oportunidad: cuenta el mejor resultado |

Los dos temas que empiezan el segundo trimestre en la semana de los exámenes de febrero (redes neuronales parte 1, y llamadas a herramientas) no entran en el examen de febrero.

Los exámenes son presenciales, sin red y sin ninguna herramienta de IA: no se puede tener instalado ni siquiera un modelo local en tu cuenta. Puedes usar cualquier material del ordenador, incluido el material de clase. Cada examen tiene dos partes con el mismo peso:

| Parte | Qué se pide |
| --- | --- |
| 1. Cuestionario | Preguntas tipo test en Moodle, sobre todas las etapas que abarca el examen, incluidas las que no tienen trabajo de proyecto: conceptos; casos (un problema descrito: qué enfoque, qué división, qué métrica); números (leer una matriz de confusión, estimar un coste o una fiabilidad); y decisiones de diseño (qué arquitectura encaja con un presupuesto, qué test detectaría un bug, qué instrucción a un agente de IA es mejor) |
| 2. Los proyectos | Respuestas escritas sobre repositorios en los que has trabajado durante el curso, instalados sin conexión, con un cambio hecho para esa convocatoria (un bug introducido, un requisito nuevo, otro dataset, otra variable objetivo): predecir el efecto de un cambio y luego ejecutar el código para comprobarlo; diagnosticar un problema; escribir las instrucciones que le darías a un agente de IA para un cambio, y el test que demostraría que está hecho; criticar la evaluación. No se te pedirá escribir código desde cero |

## Tu nota

Cada examen, febrero, mayo y junio, es la media de sus dos partes:

$$E = \frac{\text{cuestionario} + \text{proyectos}}{2}$$

Cada parte debe llegar a 4: con una parte por debajo de 4, el examen cuenta como máximo un 4. Un examen al que no te presentas cuenta 0.

Mayo da tu nota, y febrero puede subirla, nunca bajarla: mayo cuenta por sí solo o promediado con febrero, lo que sea mayor. Junio funciona igual, como segunda oportunidad:

$$G_\text{mayo} = \max\left(E_\text{mayo},\ \frac{E_\text{feb} + E_\text{mayo}}{2}\right) \qquad G_\text{junio} = \max\left(E_\text{junio},\ \frac{E_\text{feb} + E_\text{junio}}{2}\right)$$

La media con febrero solo cuenta cuando las dos partes de ese examen llegan a 4; si no, su $G$ es su $E$, como máximo 4.

Cuenta la mejor entre mayo y junio, y se aprueba con un 5. Una vez aprobado, las contribuciones aceptadas suman $C$, de 0 a 2 puntos ([ver abajo](#contribuciones)), nunca por encima de 10:

$$\text{nota} = \min\left(10,\ \max(G_\text{mayo},\ G_\text{junio}) + C\right)$$

La nota se redondea al entero más cercano, las mitades hacia arriba; una nota por debajo de 5 nunca se redondea hasta el aprobado.

## Los proyectos

A lo largo del curso trabajas en [proyectos](working-plan.md#los-proyectos): repositorios públicos de los que haces fork y que vas desarrollando paso a paso. Tus pull requests son tus entregas: reciben feedback y nunca se califican, salvo como [contribuciones](#contribuciones). Los exámenes te piden trabajar sobre su código, así que la mejor preparación es haberlos construido o, al menos, haberlos seguido de cerca.

La parte práctica de cada examen trabaja sobre algunos de estos repositorios, y posiblemente sobre los ejemplos resueltos. **Cuáles, y la versión (tag) de cada uno que hay que estudiar, se anuncian al menos dos semanas antes del examen.** Cada versión es el repositorio tal como estaba una semana antes del examen o antes: solo se examina lo que se había publicado para entonces, nunca el material complementario de la carpeta `docs/` de un repositorio. Las preguntas tratan sobre un cambio que no has visto, así que recitar el código no te servirá; entenderlo, sí. Todo se ejecuta sin conexión, sin modelo de lenguaje.

**Se espera que uses herramientas de IA.** Lo que se evalúa es tu comprensión: las herramientas de IA pueden escribir la mayor parte del código por ti, pero no pueden entenderlo por ti, y eso es lo que comprueba el examen. Asegúrate de que puedes explicar, probar y modificar el código de los proyectos, y de que sabrías dirigir bien a un agente de IA para modificarlo.

## Contribuciones

Las contribuciones son voluntarias, y puedes sacar un 10 sin ellas. Las issues útiles (un problema bien identificado, aunque no traiga solución) y los pull requests a cualquier repositorio del curso, una vez aceptados, pueden sumar hasta 2 puntos a la nota de un módulo cuyo examen hayas aprobado, nunca por encima de 10. Cómo se valoran se describe en la programación. Registra tu usuario de GitHub en el aula virtual para que se puedan contar. Cómo participar: [Mejorar los materiales del curso](../CONTRIBUTING.md).

## Todo lo demás

- Los **elementos básicos** (★ en el README de cada tema) son el itinerario mínimo. La parte de proyectos de cada examen solo necesita esos elementos y los repositorios que usa, y unas dos terceras partes del cuestionario tratan sobre ellos; el resto del cuestionario trata sobre los elementos **estándar**: el resto del itinerario y los ejemplos resueltos.
- Las **profundizaciones** nunca se evalúan.
- Los **ejemplos resueltos** (los repositorios que aplican cada etapa a datos reales) se estudian, y el cuestionario puede preguntar por ellos. Algunos temas, como la clasificación, solo se practican ahí.
- Las **tareas de práctica** (propuestas por los temas y los ejemplos resueltos) nunca se califican. Son la mejor preparación para el examen, y puedes pedir feedback sobre cualquiera de ellas.
