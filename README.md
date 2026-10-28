# Inteligencia Artificial 2026/27

> 🇪🇸 **Traducción al español** del repositorio original de [avidaldo/ai](https://github.com/avidaldo/ai), hecha por un alumno para ayudar a los compañeros. La versión de referencia es siempre la original en inglés: si algo no cuadra, consúltala.

Materiales de dos módulos del curso de especialización en Inteligencia Artificial y Big Data, impartidos juntos como un único itinerario:

- **SAA · Sistemas de Aprendizaje Automático**: cómo aprenden los modelos a partir de los datos, cómo se entrenan y cómo saber si de verdad funcionan.
- **PIA · Programación de Inteligencia Artificial**: construir software con IA: Python y sus herramientas, modelos de lenguaje, recuperación de información, agentes, despliegue y automatización.

## Empieza aquí

1. **[Plan de trabajo](course/working-plan.md)**: cómo organizarte durante el curso, los tres niveles de cada tema, los proyectos que haces fork y desarrollas, y cómo practicar.
2. **[Cómo se te evalúa](course/assessment.md)**: los exámenes, cómo se calcula tu nota y cómo cuentan las contribuciones.
3. **[Mejorar los materiales](CONTRIBUTING.md)**: informa de errores, pide explicaciones más claras o arregla cosas tú mismo.

## Hoja de ruta

El curso en quince etapas, en el orden en que las trabajamos; se adapta a medida que avanza el año. Cada etapa pertenece a un módulo: si solo cursas uno, sigue sus filas. Dos etapas se apoyan en el otro módulo: construir con modelos de lenguaje (5, PIA) se apoya en la nota sobre modelos de lenguaje de la etapa 2 (SAA), y RAG (11, PIA) necesita saber cómo funcionan los modelos de lenguaje (10, SAA).

El README de cada tema indica su itinerario, con los elementos básicos marcados con ★. Los ejemplos resueltos, y el software que construyes y ejecutas, son repositorios propios. Los elementos marcados como *(próximamente)* se están escribiendo y se enlazarán cuando estén listos.

### Primer trimestre

| # | Etapa | Módulo | Tema | Ejemplos resueltos y profundizaciones |
| ---: | --- | --- | --- | --- |
| 1 | Primeros pasos | PIA | [Preparar el entorno](pia/setup/README.md): Python, uv o conda, Git y GitHub, trabajar con un asistente de programación con IA | Primera tarea: [numpy-mnist](https://github.com/avidaldo/numpy-mnist), del que haces fork en la semana 1. Profundizaciones: [un flujo de trabajo con Copilot guiado por especificaciones en VS Code](https://github.com/avidaldo/tutorial-SSD-customizations-VSCode/blob/main/tutorial.md), [personalizaciones de Copilot](https://github.com/avidaldo/vccode-customizations-AI-intro) |
| 2 | Qué son la IA y el aprendizaje automático | SAA | [El mapa del curso](saa/concepts/README.md): qué son la IA y el aprendizaje automático, y cada familia de modelos vista desde fuera | Profundizaciones: [IA clásica, inteligencia sin aprendizaje](saa/concepts/deep-dives/classical-ai/README.md), [probabilidad y teorema de Bayes](saa/concepts/deep-dives/probability/README.md) |
| 3 | Python para IA | PIA | [Por qué Python domina la IA](pia/setup/why_python.md) aunque sea lento; estructura de un programa, con [tres en raya](https://github.com/avidaldo/python-tic-tac-toe), recomendado | Profundización: [compare-python-c-efficiency](https://github.com/avidaldo/compare-python-c-efficiency), para medirlo tú mismo |
| 4 | Trabajar con datos | PIA | [Lo esencial de Python para datos](pia/python-data-essentials/README.md): NumPy y pandas para cargar, inspeccionar, remodelar y combinar datos, encontrar los problemas de una tabla y obtener datos de APIs web | Ejercicios: [numpy-mnist](https://github.com/avidaldo/numpy-mnist) |
| 5 | Construir con modelos de lenguaje | PIA | Llamar a modelos en local y a través de una API, prompts, salida estructurada, probar y medir un componente que usa un modelo *(próximamente)*. Se apoya en la nota de la etapa 2 [Los modelos de lenguaje vistos desde fuera](saa/concepts/background/language_models.md) | Ejemplo resuelto: [un chatbot con salvaguardas](https://github.com/avidaldo/ai-chat-guardrails), con un modelo local o remoto |
| 6 | Aprendizaje supervisado | SAA | Regresión y clasificación, y cómo saber si un modelo de verdad funciona *(próximamente)*. Se apoya en la nota de la etapa 2 [La vida de un proyecto de aprendizaje automático](saa/concepts/background/ml_project_lifecycle.md) | Ejemplos resueltos: [viviendas de California](https://github.com/avidaldo/california_e2e), [ventas de casas en King County](https://github.com/avidaldo/king-county), [enfermedad de tiroides](https://github.com/avidaldo/thyroid). Profundización: preparación de datos, desde la exploración hasta la codificación y el escalado *(próximamente)* |
| 7 | Servir modelos | PIA | Un modelo detrás de una API web y una demo, en un contenedor, desplegado *(próximamente)* | Ejemplos resueltos: [un clasificador de imágenes servido con FastAPI](https://github.com/avidaldo/cifar-10-fastapi), y [el mismo clasificador como app de Gradio](https://huggingface.co/spaces/avidaldo/cifar-10-fastapi-gradio) |

### Segundo trimestre

| # | Etapa | Módulo | Tema | Ejemplos resueltos y profundizaciones |
| ---: | --- | --- | --- | --- |
| 8 | Redes neuronales | SAA | Cómo aprende una red, redes para tablas, redes convolucionales, reutilizar una red preentrenada *(próximamente)*. Se apoya en la nota de la etapa 2 [Las redes neuronales vistas desde fuera](saa/concepts/background/neural_networks.md) | |
| 9 | Agentes y MCP | PIA | Llamadas a herramientas (*tool calling*), agentes que usan herramientas de forma segura, y MCP, un protocolo estándar para conectar modelos con herramientas *(próximamente)* | |
| 10 | Cómo funcionan los modelos de lenguaje | SAA | De las palabras como recuentos a los *embeddings*, la atención y los *transformers* *(próximamente)*. Se apoya en la nota de la etapa 2 [Los modelos de lenguaje vistos desde fuera](saa/concepts/background/language_models.md) | |
| 11 | Generación aumentada por recuperación (RAG) | PIA | Basar las respuestas de un modelo en tus propios documentos, con respuestas que citan sus fuentes *(próximamente)* | |
| 12 | Automatización y negocio | PIA | Hacer que los sistemas de IA funcionen solos, y decidir si merecen la pena *(próximamente)* | |
| 13 | Aprendizaje no supervisado | SAA | *Clustering*, reducción de dimensionalidad y detección de anomalías *(próximamente)* | |
| 14 | Visión y voz con modelos preentrenados | PIA | [Visión por computador](https://github.com/avidaldo/computer-vision) con OpenCV, detección de objetos con YOLO, *embeddings* CLIP y una app de autenticación facial. Voz con modelos preentrenados: de voz a texto y de texto a voz *(próximamente)* | |
| 15 | Aprendizaje por refuerzo | SAA | [Aprender de las recompensas](saa/reinforcement-learning/README.md): agentes, entornos y Q-learning | Ejemplo resuelto: [tres en raya con Q-learning](https://github.com/avidaldo/tictactoe-qlearning), desde la versión más sencilla hasta un agente que nunca pierde |

El examen de febrero cubre el primer trimestre, y el de mayo, todo el curso: consulta [cómo se te evalúa](course/assessment.md).
