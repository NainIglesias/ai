# Trabajar con un asistente de programación con IA

Buena parte del código actual se escribe con un asistente de IA: GitHub Copilot, Claude Code, OpenAI Codex, Cursor, Gemini CLI y otros, dentro del editor o en la terminal. Las herramientas cambian cada pocos meses; la forma de trabajar con ellas cambia mucho menos. Elige una y aprende a dirigirla.

## El ciclo

1. **Pide un paso pequeño,** con el contexto que necesita: los archivos implicados, el mensaje de error, lo que esperas que ocurra.
2. **Lee el cambio** (el diff) antes de aceptarlo.
3. **Ejecuta el código y los tests.**
4. **Haz commit solo de lo que puedas explicar.** El código es tuyo en cuanto está en tu repositorio, lo haya escrito quien lo haya escrito.

Los asistentes son rápidos y seguros de sí mismos, y también se equivocan de formas verosímiles: un import que no existe, un test que no comprueba nada, un arreglo que oculta el error en lugar de resolverlo. Leer y ejecutar es la forma de pillarlos.

En modo *agente*, un asistente además ejecuta comandos y edita varios archivos por su cuenta. Lee cada comando antes de aprobarlo, y nunca le dejes borrar archivos, hacer push ni tocar nada fuera del proyecto sin preguntarte.

## Conseguir un asistente

El alumnado verificado tiene GitHub Copilot gratis a través de GitHub Education, con el plan *Copilot Student* ([cómo](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)). La mayoría de los demás asistentes tienen un plan gratuito, y algunos pueden usar un modelo que se ejecuta en tu propio ordenador.

## Instrucciones del proyecto: `AGENTS.md`

La mayoría de los asistentes leen un archivo Markdown en la raíz del repositorio con las instrucciones del proyecto, y `AGENTS.md` es el nombre que comparten casi todos; algunos leen además un archivo propio (`CLAUDE.md`, `.github/copilot-instructions.md`). Mantenlo corto y factual: cómo instalar, ejecutar y probar el proyecto, sus convenciones y lo que el asistente no debe tocar. Un asistente que sabe ejecutar los tests puede comprobar su propio trabajo.

## Lo que nunca hay que pegar

- Secretos: claves de API, contraseñas, tokens. Guárdalos en un archivo `.env` que git ignore.
- Datos personales, tuyos o de cualquier otra persona.

Los planes gratuitos y los precios cambian a menudo: comprueba qué incluye tu plan antes de depender de él. Los exámenes se hacen sin ninguna herramienta de IA, así que asegúrate de entender cada cambio que aceptas ([cómo se te evalúa](../../course/assessment.md)).

## Profundizaciones

Dos ejemplos resueltos para GitHub Copilot en VS Code. Las ideas se aplican a cualquier asistente; las rutas de los archivos y algunas funciones son propias de Copilot.

- [Construir un flujo de trabajo con Copilot guiado por especificaciones en VS Code](https://github.com/avidaldo/tutorial-SSD-customizations-VSCode/blob/main/tutorial.md): un tutorial en cuatro partes (instrucciones, *skills* y agentes, *hooks*, MCP)
- [Personalizaciones de Copilot: un repositorio de referencia](https://github.com/avidaldo/vccode-customizations-AI-intro)
