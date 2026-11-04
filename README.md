# Inteligencia Artificial 2026/27

> 🇪🇸 **Traducción al español** del repositorio original de [avidaldo/ai](https://github.com/avidaldo/ai) hasta el commit fae9459d03613f24446d444b49906f93b61fb26c, hecha por un alumno para ayudar a los compañeros. La versión de referencia es siempre la original en inglés: si algo no cuadra, consúltala.

Materiales de dos módulos del curso de especialización en Inteligencia Artificial y Big Data, impartidos juntos como un único itinerario:

- **SAA · Sistemas de Aprendizaje Automático**: cómo aprenden los modelos a partir de los datos, cómo se entrenan y cómo saber si de verdad funcionan.
- **PIA · Programación de Inteligencia Artificial**: construir software con IA: Python y sus herramientas, modelos de lenguaje, recuperación de información, agentes, despliegue y automatización.

## Cómo trabajar

1. **Sigue la [hoja de ruta](#hoja-de-ruta)** etapa tras etapa, desde la etapa 1, que prepara tus herramientas. Cada etapa tiene un tema: abre su README y recorre su itinerario en orden. Ejecuta `git pull` para recibir cada tema según se publica.
2. **Dedica unas 10 horas a la semana** a los dos módulos, la sesión semanal incluida; se alternan por bloques. Si tienes menos tiempo, haz primero los elementos básicos (★) y sigue los proyectos, construyéndolos o bien leyendo, ejecutando y modificando la solución del profesor; vuelve al resto cuando puedas. Los elementos sin marcar son el resto del itinerario, y el cuestionario también pregunta por ellos. Las profundizaciones son opcionales y nunca se evalúan.
3. **Practica.** Leer y ejecutar no basta: construye los proyectos de más abajo y prueba las tareas de práctica que proponen algunos temas y ejemplos resueltos. La práctica nunca se califica, y es la mejor preparación para los exámenes.

Solo las fechas de los exámenes están fijadas. Los materiales suelen publicarse mucho antes de que se necesiten, y siempre puedes adelantarte. El orden, el ritmo y los proyectos se adaptan a cómo avanza el grupo; cada cambio se anuncia en la sesión semanal y se hace en esta página.

## Los proyectos

Repositorios públicos de los que haces fork y que vas desarrollando a lo largo del curso, paso a paso. Pueden añadirse más según avance el año.

| Proyecto | Módulo | Qué construyes | Empieza |
| --- | --- | --- | --- |
| [numpy-mnist](https://github.com/avidaldo/numpy-mnist) | PIA | Imágenes como arrays de NumPy, con Git, tests e integración continua. Guarda tus soluciones: volverán más adelante en el curso | Haz fork en la etapa 1 y resuelve sus ejercicios en la etapa 4 |
| [Asistente de normativa](https://github.com/avidaldo/fp-regulations-assistant) | PIA | Un asistente que ayuda a un profesor a responder las preguntas del alumnado sobre la normativa de formación profesional, citando los artículos en vigor | Etapa 4 |
| [Valoración de viviendas](https://github.com/avidaldo/idealista18-avm) | SAA | Una estimación del precio de una vivienda a partir de anuncios reales, y de cuánto se puede confiar en cada estimación | Etapa 6 |

Los dos proyectos más grandes los construye todo el grupo, un paso cada vez:

- **Cada paso es una issue** en el repositorio del proyecto, con la comprobación que demuestra que está hecho. Haz allí tus preguntas.
- **Trabaja en tu fork**, y abre un pull request que enlace la issue del paso ([cómo](pia/setup/git_github.md#contribuir-con-un-pull-request)). Es tu entrega: recibe feedback y nunca se califica, aunque una vez aceptado cuenta como contribución.
- **La solución del profesor llega con la siguiente issue**, con los buenos pull requests fusionados en ella o en su lugar. Tráela a tu fork antes de empezar el siguiente paso ([cómo](pia/setup/git_github.md#mantener-tu-fork-al-día)).

La parte práctica de cada examen trabaja sobre estos repositorios.

## Hoja de ruta

El curso en quince etapas, en el orden en que las trabajamos. Cada etapa pertenece a un módulo: si solo cursas uno, sigue sus filas, más dos del otro. La etapa 5 de PIA necesita la nota de SAA [Los modelos de lenguaje vistos desde fuera](saa/concepts/background/language_models.md), de la etapa 2, y la etapa 11 de PIA necesita la etapa 10 de SAA. Los elementos marcados como *(próximamente)* se están escribiendo y se enlazarán cuando estén listos.

### Primer trimestre

| # | Etapa | Módulo | Tema | Ejemplos resueltos |
| ---: | --- | --- | --- | --- |
| 1 | Primeros pasos | PIA | [Preparar el entorno](pia/setup/README.md): tus herramientas, tu fork de numpy-mnist y tu usuario de GitHub en el aula virtual | |
| 2 | Qué son la IA y el aprendizaje automático | SAA | [El mapa del curso](saa/concepts/README.md): cada familia de modelos, vista desde fuera | |
| 3 | Python para IA | PIA | [Por qué Python domina la IA](pia/setup/why_python.md), aunque sea lento | [Tres en raya](https://github.com/avidaldo/python-tic-tac-toe), sobre la estructura de un programa, recomendado |
| 4 | Trabajar con datos | PIA | [Lo esencial de Python para datos](pia/python-data-essentials/README.md): NumPy y pandas, los problemas de una tabla, datos de APIs web | Los ejercicios de [numpy-mnist](https://github.com/avidaldo/numpy-mnist) |
| 5 | Construir con modelos de lenguaje | PIA | Modelos locales y remotos, prompts, salida estructurada, probar un componente que usa un modelo *(próximamente)* | [Un chatbot con salvaguardas](https://github.com/avidaldo/ai-chat-guardrails) |
| 6 | Aprendizaje supervisado | SAA | [Aprendizaje supervisado](saa/supervised-learning/README.md): regresión, clasificación y cómo saber si un modelo de verdad funciona; [Preparación de datos](saa/data-preparation/README.md) tras su parte 3 | [Ventas de casas en King County](https://github.com/avidaldo/king-county), [viviendas de California](https://github.com/avidaldo/california_e2e), [enfermedad de tiroides](https://github.com/avidaldo/thyroid) |
| 7 | Servir modelos | PIA | Un modelo detrás de una API web y una demo, en un contenedor, desplegado *(próximamente)* | [Un clasificador de imágenes servido con FastAPI](https://github.com/avidaldo/cifar-10-fastapi), y [el mismo como app de Gradio](https://huggingface.co/spaces/avidaldo/cifar-10-fastapi-gradio) |

### Segundo trimestre

| # | Etapa | Módulo | Tema | Ejemplos resueltos |
| ---: | --- | --- | --- | --- |
| 8 | Redes neuronales | SAA | Cómo aprende una red, redes para tablas, redes convolucionales, reutilizar una red preentrenada *(próximamente)* | |
| 9 | Agentes y MCP | PIA | Llamadas a herramientas (*tool calling*), agentes que usan herramientas de forma segura, y MCP, una forma estándar de conectar modelos con herramientas *(próximamente)* | |
| 10 | Cómo funcionan los modelos de lenguaje | SAA | De las palabras como recuentos a los *embeddings*, la atención y los *transformers* *(próximamente)* | |
| 11 | Generación aumentada por recuperación (RAG) | PIA | Respuestas de un modelo basadas en tus propios documentos, citando sus fuentes *(próximamente)* | |
| 12 | Automatización y negocio | PIA | Sistemas de IA que funcionan solos, y si merecen la pena *(próximamente)* | |
| 13 | Aprendizaje no supervisado | SAA | *Clustering*, reducción de dimensionalidad y detección de anomalías *(próximamente)* | |
| 14 | Visión y voz con modelos preentrenados | PIA | [Visión por computador](https://github.com/avidaldo/computer-vision): OpenCV, YOLO, *embeddings* CLIP y una app de autenticación facial. Voz: de voz a texto y de texto a voz *(próximamente)* | |
| 15 | Aprendizaje por refuerzo | SAA | [Aprender de las recompensas](saa/reinforcement-learning/README.md): agentes, entornos y Q-learning | [Tres en raya con Q-learning](https://github.com/avidaldo/tictactoe-qlearning) |

## Exámenes y tu nota

Cada módulo se califica por separado, a partir de exámenes presenciales. Febrero cubre el primer trimestre: es un ensayo obligatorio, y puede subir tu nota, nunca bajarla. Mayo cubre todo el curso y da tu nota, y junio es una segunda oportunidad. Cada examen tiene un cuestionario y una parte práctica sobre los proyectos. Las contribuciones aceptadas pueden sumar hasta 2 puntos a un módulo aprobado. Fechas y reglas: [Cómo se te evalúa](course/assessment.md).

## Mejorar los materiales

Si encuentras un error o algo poco claro, abre una issue; si puedes arreglarlo, envía un pull request. Cómo, y cómo cuentan las contribuciones: [Mejorar los materiales del curso](CONTRIBUTING.md).
