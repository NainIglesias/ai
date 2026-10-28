# Plan de trabajo

Cómo organizarte durante el curso; las etapas en sí, en orden, están en la [hoja de ruta](../README.md#hoja-de-ruta) de la página principal. Ninguna de las dos páginas es un contrato: el orden, el ritmo y los proyectos se adaptan a cómo avanza el grupo. Cada cambio se anuncia en la sesión semanal y se hace en estas páginas, cuyo historial en GitHub lo muestra.

## Cómo trabajarlo

- **Unas 10 horas a la semana** para los dos módulos, incluida la sesión semanal. SAA y PIA se alternan por bloques, así que es normal que una semana solo haya uno de ellos. Solo las fechas de examen son fijas: los materiales suelen publicarse bastante antes de que se necesiten, y siempre puedes adelantarte.
- **Cada etapa tiene un tema:** una carpeta de este repositorio o, cuando se trata de software que construyes y ejecutas, un repositorio propio. Un tema tiene un itinerario ordenado, después ejemplos resueltos que lo aplican a datos reales, y después profundizaciones. Clona este repositorio una vez y haz pull para obtener cada tema a medida que se publica.
- **Tres niveles,** marcados en el README de cada tema. Los elementos **básicos** (★) son el mínimo: lo que necesitan los proyectos y las ideas clave de cada etapa; el examen pregunta sobre todo por ellos. Los elementos **estándar**, sin marcar, son el resto del itinerario; el cuestionario también pregunta por ellos. Las **profundizaciones** van más allá: son opcionales, nunca se evalúan y nada del itinerario depende de ellas.
- **¿Tienes menos tiempo?** Haz los elementos básicos y sigue los proyectos, construyéndolos o leyendo, ejecutando y modificando la solución del profesor. Vuelve a los elementos estándar cuando puedas.

## Los proyectos

A lo largo del curso trabajas en proyectos: repositorios públicos de los que haces fork y que vas desarrollando paso a paso. Pueden añadirse más durante el año. Por ahora son:

- [numpy-mnist](https://github.com/avidaldo/numpy-mnist), la primera tarea de PIA: imágenes como arrays de NumPy, con Git, tests e integración continua. Haz fork en la semana 1 siguiendo su README, y resuelve sus ejercicios con la etapa 4. Comunica al profesor tu usuario de GitHub a través del aula virtual.
- [Proyecto PIA · Asistente de normativa](https://github.com/avidaldo/fp-regulations-assistant): un asistente que ayuda a un profesor a responder las dudas del alumnado sobre la normativa de formación profesional, citando los artículos en vigor.
- [Proyecto SAA · Valoración de inmuebles](https://github.com/avidaldo/idealista18-avm): estimar el precio de una vivienda a partir de anuncios reales, y hasta qué punto se puede confiar en cada estimación.

Los proyectos más grandes los construye todo el grupo, paso a paso:

- **Cada paso es una issue** en el repositorio del proyecto, con la comprobación que demuestra que está hecho. Pregunta tus dudas ahí.
- **Trabaja en tu fork,** y envía un pull request que enlace la issue del paso cuando tengas una solución ([cómo](../pia/setup/git_github.md#contribuir-con-un-pull-request)).
- **La solución del profesor de un paso llega con la siguiente issue,** con los buenos pull requests fusionados en ella o en su lugar. Incorpórala a tu fork antes de empezar el siguiente paso ([cómo](../pia/setup/git_github.md#mantener-tu-fork-al-día)).
- **Tu pull request es tu entrega.** Recibe feedback y nunca se califica: solo cuenta como contribución, una vez aceptado. Todo lo que necesita un paso se publica antes de que se abra.

La parte práctica de cada examen trabaja sobre estos repositorios: consulta [cómo se te evalúa](assessment.md#los-proyectos).

## Cómo practicar

Leer y ejecutar los materiales no basta: se aprende haciendo cosas con ellos. Los temas y los ejemplos resueltos proponen tareas de práctica y experimentos. La práctica es opcional y nunca se califica, pero es la mejor preparación para los proyectos y para el examen.

### Dónde trabajas

- **Trabaja en repositorios propios,** en GitHub o en otra plataforma (GitLab, Codeberg…): uno para tus tareas de práctica, y forks de este repositorio, de los proyectos y de los ejemplos resueltos en los que trabajes. Tu historial de commits es el registro de tu trabajo.
- Todo repositorio con código lista sus dependencias en `requirements.txt`, y algunos tienen además un `pyproject.toml`. Instálalas con uv o, si lo prefieres, con conda: consulta [Preparar el entorno](../pia/setup/setup.md#entornos-virtuales).
- **Guarda tus soluciones.** Lo que escribas en numpy-mnist vuelve a aparecer más adelante en el curso: consérvalo en tu fork.

### Experimentos y contribuciones

- La mayoría de los ejemplos resueltos terminan su README con ideas para ampliarlos. Prueba cualquiera de ellas en tu fork.
- Ayuda a mejorar los materiales: abre una issue cuando algo esté mal, no se entienda o falte, y envía un pull request cuando puedas arreglarlo tú. Consulta [Mejorar los materiales del curso](../CONTRIBUTING.md). De vez en cuando se etiqueta una issue como `practice`: una mejora esperando a que alguien la haga.

### Pedir feedback

Un pull request es la forma de entregar tu trabajo, tanto en los proyectos como en las tareas de práctica. Recibe feedback y nunca se califica: solo cuenta como contribución, una vez aceptado.

1. Haz el trabajo en una rama de tu fork.
2. Abre un pull request: hacia el repositorio original para un paso de un proyecto o una tarea como numpy-mnist; hacia tu propio repositorio para cualquier otra práctica (un *merge request*, en otras plataformas).
3. Para un pull request en tu propio repositorio, abre una issue en este repositorio que lo enlace y diga sobre qué te gustaría recibir feedback.

El feedback llega según el tiempo disponible, por orden de llegada, como comentarios en tu pull request. [Registra tu usuario de GitHub en el aula virtual para que se pueda encontrar tu trabajo y contar tus contribuciones](https://fpadistancia.edu.xunta.gal/mod/feedback/view.php?id=2318916).
