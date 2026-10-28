# Herramientas esenciales para programar IA

## Tu primera semana

1. Crea una cuenta de [GitHub](https://github.com).
2. Instala [Git](https://git-scm.com/downloads), y la [CLI de GitHub](https://cli.github.com/) para iniciar sesión desde la terminal con `gh auth login` ([Git y GitHub](git_github.md)).
3. Instala [uv](uv_tutorial.md) o, si prefieres conda, [Miniforge](conda_tutorial.md). Los dos instalan el propio Python: no hace falta instalarlo aparte.
4. Instala un editor: [VS Code](https://code.visualstudio.com/) con sus extensiones *Python* y *Jupyter*, o PyCharm.
5. Elige un asistente de programación con IA ([Trabajar con un asistente de programación con IA](ai_assisted_development.md)).
6. Clona este repositorio, y después haz fork y prepara [numpy-mnist](https://github.com/avidaldo/numpy-mnist), hasta el paso 4 de su README.

El resto de esta nota explica cada herramienta.

## Lenguajes de programación

### Python

Python es el **lenguaje de programación predominante en el aprendizaje automático**. Es el lenguaje que usamos en los dos módulos. Python es un lenguaje de programación interpretado, de alto nivel y de propósito general. Es versátil y fácil de aprender, y tiene una **enorme colección de bibliotecas y frameworks para IA**, aprendizaje automático y aprendizaje profundo ([por qué](why_python.md)).

Cursos de programación en Python:
- https://edube.org/study/pe1
- https://edube.org/study/pe2


### Otros lenguajes de programación relevantes en IA

- R: se usa sobre todo en estadística y análisis de datos.
- C/C++: muchas de las bibliotecas que se usan desde Python están implementadas en C/C++, ya que son lenguajes de bajo nivel y mucho más rápidos que Python. C++ sigue siendo la referencia cuando el rendimiento es crítico.
- CUDA: la extensión de C++ de NVIDIA para programar GPUs, sobre las que se ejecuta la mayor parte del aprendizaje profundo.
- Rust: rápido y seguro con la memoria, y cada vez más el lenguaje de las herramientas de Python: uv, el linter Ruff, la biblioteca de dataframes Polars y los tokenizadores de Hugging Face están escritos en él.
- Julia: lenguaje de programación de alto rendimiento diseñado para la computación científica y técnica.
- Mojo: pretende conseguir la facilidad de uso de Python con un rendimiento similar al de C.


## Git y las forjas de Git

Git es un sistema de control de versiones distribuido que nos permite llevar un registro de los cambios en el código fuente de un proyecto. Las forjas de Git son servicios que nos permiten alojar nuestros repositorios de Git en línea, como GitHub, GitLab, Codeberg y Bitbucket. Los dos módulos funcionan como la mayoría de los equipos de software: sobre repositorios públicos, mediante issues y pull requests. Haces fork de un repositorio, trabajas en tu fork y propones tus cambios en un pull request, que es también la forma de entregar tu trabajo para recibir feedback.

- [Git y GitHub: de los commits a los pull requests](git_github.md)
- [Git and GitHub for AI Programming](https://www.youtube.com/watch?v=T1tYBbiWTbc) (vídeo)


## IDEs (entornos de desarrollo integrados)

Para trabajar con Python en aprendizaje automático y aprendizaje profundo, algunos de los IDEs más populares son:

### [Visual Studio Code (VS Code)](https://code.visualstudio.com/)

Visual Studio Code es un editor de código fuente desarrollado por Microsoft. Es multiplataforma y admite múltiples lenguajes de programación. Es uno de los editores más populares entre los desarrolladores de software.

- [VISUAL STUDIO CODE: Beginner's Tutorial](https://www.youtube.com/watch?v=CxF3ykWP1H4)

### [Cursor](https://www.cursor.com/)

Cursor es un [fork](https://es.wikipedia.org/wiki/Bifurcaci%C3%B3n_(desarrollo_de_software)) de VS Code centrado en usar LLMs para programar.

### [PyCharm](https://www.jetbrains.com/pycharm/)

PyCharm es un IDE desarrollado por JetBrains. Es uno de los IDEs más populares para Python y lo usan muchos desarrolladores de software. También cubre los notebooks y la exploración de datos: JetBrains dejó de vender DataSpell, su IDE de ciencia de datos, en mayo de 2026, y pasó a sus usuarios a PyCharm.

### Asistentes de programación con IA

La mayoría de estos editores integran asistentes de programación con IA, como GitHub Copilot, Claude Code u OpenAI Codex, y algunos asistentes también funcionan por su cuenta en la terminal. Usarás uno durante todo el curso: consulta [Trabajar con un asistente de programación con IA](ai_assisted_development.md).

## Notebooks de Jupyter

Jupyter es una aplicación que nos permite crear notebooks (documentos que combinan código, texto enriquecido, ecuaciones, visualizaciones, etc.) en el navegador. Estos notebooks son archivos con la extensión `.ipynb` (cuando se usa el lenguaje Python) que se pueden exportar a distintos formatos estáticos, como HTML o PDF. Internamente, los archivos `.ipynb` son JSON.

Editores como VS Code y PyCharm abren los notebooks directamente. Un notebook se ejecuta sobre un **kernel**, el Python de un entorno: elige el entorno de tu proyecto como kernel (*Select Kernel* en VS Code). El entorno necesita el paquete `ipykernel`, que viene incluido en `jupyter`.

## Entornos virtuales

Los **entornos virtuales** nos permiten aislar las **dependencias** de un proyecto de las del sistema operativo. Así podemos tener distintas versiones de las mismas **bibliotecas** en distintos proyectos sin conflictos entre ellas.

Todo repositorio de estos módulos lista sus dependencias en un archivo `requirements.txt`, que instalan estas dos herramientas. Elige una:

- **uv**, recomendada: una herramienta moderna y rápida que gestiona proyectos de Python, sus entornos virtuales y sus dependencias, e instala el propio Python. [Tutorial de uv: proyectos, entornos y paquetes de Python](uv_tutorial.md); [UV for Python… (Almost) All Batteries Included](https://www.youtube.com/watch?v=qh98qOND6MI) (vídeo).
- **conda**, la alternativa: una buena opción si ya lo usas, o si necesitas programas que no son paquetes de Python, como ffmpeg. [Tutorial de conda: gestión de entornos y paquetes](conda_tutorial.md).

Todo en estos módulos funciona en Windows, macOS y Linux. En Windows, cuando una herramienta o un tutorial espera Linux, [WSL](https://learn.microsoft.com/es-es/windows/wsl/install) (Subsistema de Windows para Linux) ejecuta un Linux completo dentro de Windows.

Cómo se relacionan estas herramientas con pip, venv y Poetry: [Gestión de dependencias y entornos virtuales en Python](py_dependencies.md); [Introduction to pip, conda, and virtual environments](https://www.youtube.com/watch?v=7Rd-Gj8o-6Q) (vídeo).


## [Google Colab](https://colab.research.google.com/)

Google Colab es un servicio gratuito de Google que nos permite ejecutar notebooks de Jupyter en la nube. Colab nos permite ejecutar código en Python, R y otros lenguajes de programación, y da acceso a recursos de hardware como GPUs y TPUs. Es una buena alternativa cuando tu ordenador es demasiado lento para un notebook, como puede pasar con las redes neuronales del segundo trimestre.
