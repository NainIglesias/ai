# Gestión de dependencias y entornos virtuales en Python

## La evolución de la gestión de dependencias en Python

A medida que crecía la popularidad de Python en los años 2000, se volvió crucial gestionar bien las bibliotecas. Sin un sistema eficiente para instalarlas y organizarlas, los proyectos podían caer fácilmente en el **«infierno de dependencias»**, una situación en la que los conflictos entre versiones de paquetes hacen que un proyecto sea difícil de mantener y desplegar. El problema se agrava **cuando distintos proyectos necesitan versiones distintas de las mismas bibliotecas**.

***

### 1. **Pip**: el gestor de paquetes estándar

`pip` apareció en 2008 y se convirtió en el estándar para instalar paquetes del [**Python Package Index (PyPI)**](https://pypi.org/) oficial con un comando sencillo (`pip install paquete`).

Para reproducir el entorno de un proyecto, `pip` usa archivos `requirements.txt`, que listan las bibliotecas necesarias con versiones concretas.
  
**Ventajas**:
- **Ligero** y sencillo.
- Muy flexible y compatible con cualquier proyecto de Python.
- Es la opción por defecto de casi cualquier desarrollador de Python.

**Limitaciones**:
- **El Python del sistema**: en las distribuciones de Linux recientes y en el Homebrew de macOS, `pip install` fuera de un entorno virtual se detiene con un error `externally-managed-environment` ([PEP 668](https://peps.python.org/pep-0668/)). Ese Python pertenece al gestor de paquetes del sistema operativo, y un entorno virtual es el sitio previsto para tus paquetes.
- **Separación de responsabilidades**: `pip` no gestiona entornos virtuales de forma nativa. Su filosofía es centrarse solo en la gestión de paquetes, así que hay que combinarlo con herramientas como `venv` o `virtualenv` para aislar las dependencias.
- **Resolución de dependencias**: aunque el **nuevo resolvedor introducido en `pip 20.3`** mejoró mucho la gestión de conflictos, `pip` ha carecido durante mucho tiempo de un archivo de bloqueo (*lock file*) que garantice instalaciones idénticas en distintas máquinas, a diferencia de herramientas como Poetry o Pipenv. Desde la versión 25.1 tiene un comando experimental `pip lock`, que escribe el archivo de bloqueo estándar de la PEP 751, `pylock.toml`, válido solo para la versión de Python y la plataforma que lo generaron.

***

### 2. Virtualenv y venv: aislar las dependencias

Incluso antes de `pip`, se creó **virtualenv** para **aislar las dependencias de cada proyecto**. Así se evitan conflictos entre distintas versiones de las mismas bibliotecas usadas en varios proyectos, creando **entornos virtuales**: directorios aislados donde se pueden instalar dependencias sin afectar a la instalación global de Python.
 
A partir de **Python 3.3**, Python incorporó **`venv`**, una herramienta integrada y más ligera para crear entornos virtuales, que se convirtió en el estándar y eliminó la necesidad de instalar `virtualenv` aparte para el uso básico.

**Ejemplo de uso de `venv`**:
```bash
# Crea un entorno virtual llamado .venv
python3 -m venv .venv

# Activa el entorno (en Linux/macOS)
source .venv/bin/activate

# Ahora, cualquier paquete instalado con pip quedará dentro de .venv
pip install numpy

# Desactiva el entorno
deactivate
```

***

### 3. Conda: gestión de paquetes multilenguaje y entornos virtuales

`Conda` se lanzó en 2012 como parte de la distribución **Anaconda**, orientada especialmente a la ciencia de datos y el aprendizaje automático. A diferencia de `pip`, es un gestor de paquetes **multilenguaje** (puede instalar paquetes para Python, R y otros, incluidas dependencias del sistema que no son de Python).

`Conda` ofrece paquetes **precompilados**, lo que simplificó la instalación de bibliotecas complejas como `numpy` o `pandas` en una época en la que instalarlas con `pip` solía suponer compilarlas.

**Ventajas de Conda en aprendizaje automático**:
- **Entornos virtuales integrados**: `Conda` gestiona tanto las dependencias como los entornos virtuales de forma integrada.
- **Paquetes para ML y ciencia de datos**: `Conda` se hizo popular en el aprendizaje automático y la ciencia de datos porque distribuía **bibliotecas precompiladas y optimizadas** (como `NumPy` y `scikit-learn`) en una época en la que instalarlas con `pip` solía suponer compilarlas.
- **Gestión de dependencias complejas**: destaca gestionando dependencias que no son de Python (como bibliotecas de C concretas), que pueden dar problemas al instalar solo con `pip`.

Esa segunda ventaja se ha desvanecido. Hoy PyPI distribuye *wheels* precompilados para casi todas las bibliotecas científicas, incluidas las versiones para GPU de PyTorch, y PyTorch dejó de publicar en su propio canal de Anaconda después de la versión 2.5 (quien usa conda lo obtiene ahora del canal comunitario `conda-forge`).

**Limitaciones**:
- **Más pesado**: `Conda` necesita más espacio en disco que `pip` y sus alternativas modernas. Su resolvedor de dependencias fue famoso por su lentitud hasta que conda 23.10 (2023) puso por defecto el resolvedor libmamba, mucho más rápido.
- **Complejidad innecesaria para proyectos pequeños**: para proyectos pequeños o sencillos que solo necesitan bibliotecas de Python, un enfoque con `pip`/`venv` o con `uv` es más ligero.

**Pixi** (2023), una herramienta rápida escrita en Rust, gestiona paquetes de conda-forge (y de PyPI) por proyecto con un archivo de bloqueo: viene a ser para conda lo que uv es para pip.

***

### 4. Herramientas avanzadas: Pipenv, Poetry y uv

Con el tiempo surgieron herramientas más avanzadas para resolver las limitaciones de las anteriores y ofrecer una experiencia más integrada en la gestión de entornos virtuales y dependencias.

- **Pipenv** (2017): fue uno de los primeros intentos de unificar la gestión de paquetes y de entornos. Introduce el `Pipfile` para declarar dependencias (separando producción y desarrollo) y el `Pipfile.lock` para fijar versiones exactas, garantizando la reproducibilidad.
  
- **Poetry** (2018): se ha consolidado como una de las herramientas más completas. Va más allá de Pipenv, con un sistema de resolución de dependencias más robusto y herramientas integradas para construir y publicar paquetes en PyPI. Usa el estándar `pyproject.toml`, que centraliza no solo las dependencias sino toda la configuración del proyecto (linters, formateadores, etc.).

#### **uv: el gestor de paquetes de nueva generación (2024)**

**`uv`** es un gestor de paquetes y proyectos de alto rendimiento, **escrito en Rust**. Nació en 2024 como sustituto rápido de `pip`, y hoy cubre todo el flujo de trabajo de un proyecto de Python.

**Características clave de uv**:
- **Velocidad extrema**: `uv` completa la instalación y la resolución de dependencias **entre 10 y 100 veces más rápido** que `pip`, `pip-tools` y Poetry.
- **Gestión de proyectos**: `uv init`, `uv add`, `uv lock`, `uv sync` y `uv run` gestionan un proyecto declarado en el estándar `pyproject.toml`, con las versiones exactas fijadas en `uv.lock`. `uv build` y `uv publish` lo empaquetan para PyPI.
- **Entornos y versiones de Python integrados**: `uv` crea y gestiona entornos virtuales, y puede instalar el propio Python (`uv python install 3.13`), así que no hace falta un `pyenv` aparte.
- **Compatibilidad**: funciona con los estándares existentes, incluidos `requirements.txt` y `pyproject.toml`, así que es fácil adoptarlo en proyectos ya existentes.

**Impacto**: `uv` se ha convertido rápidamente en una opción habitual para proyectos nuevos de Python, y es la herramienta recomendada en estos módulos.


***

## Tabla comparativa

| Característica          | `pip` + `venv`                               | `conda`                                     | `Poetry`                                       | `uv`                                                 |
| ----------------------- | -------------------------------------------- | ------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| **Gestión de entornos** | Sí (con `venv`)                              | Sí (integrada)                              | Sí (integrada)                                 | Sí (integrada y ultrarrápida)                        |
| **Gestión de paquetes** | Python (PyPI)                                | Python, R, C/C++, etc. (Anaconda, Conda-Forge) | Python (PyPI)                               | Python (PyPI)                                        |
| **Archivo de configuración** | `requirements.txt` (versiones flexibles) | `environment.yml`                         | `pyproject.toml`                               | `pyproject.toml` + `uv.lock`                         |
| **Dependencias no Python** | No (requiere gestores de paquetes del sistema) | Sí (su punto fuerte)                  | No                                             | No                                                   |
| **Versiones de Python** | No                                           | Sí                                          | Experimental (`poetry python install`, 2.1+)   | Sí (`uv python install`)                             |
| **Velocidad**           | Moderada                                     | Moderada (resolvedor libmamba desde 2023)   | De moderada a lenta                            | **Extremadamente rápida**                            |
| **Gestión de proyectos** | No                                          | No                                          | Sí (build, publish, scripts)                   | Sí (init, add, lock, sync, run, build, publish)      |
| **Ideal para...**       | Scripts sencillos, aprender lo básico.       | Proyectos con muchas dependencias no Python; la alternativa en estos módulos. | Bibliotecas y aplicaciones (proyectos más antiguos). | Cualquier proyecto de Python; la opción por defecto en estos módulos. |

***

## Conclusión: ¿qué herramienta elegir?

La elección depende de la complejidad y del ecosistema del proyecto:

- **Para cualquier proyecto nuevo de Python**, incluido el aprendizaje automático: **`uv`**. Gestiona el proyecto, su entorno, sus dependencias bloqueadas e incluso la versión de Python, y es lo que usamos en estos módulos.

- **Para entender los fundamentos**: la combinación de **`pip` y `venv`** sigue mereciendo la pena conocerla, porque es lo que automatizan todas las demás herramientas y lo que encontrarás en proyectos y tutoriales más antiguos.

- **Para proyectos con muchas dependencias que no son de Python** (toolkits de CUDA concretos, bibliotecas científicas compiladas, programas como ffmpeg, otros lenguajes): **`Conda`** a través de `conda-forge` sigue ganándose su sitio. También es la alternativa a uv en estos módulos: todo repositorio del curso se instala con cualquiera de los dos. Consulta el [tutorial de conda](conda_tutorial.md).

- **Para proyectos de Poetry ya existentes**: mantén **`Poetry`** donde ya se usa; hay pocas razones para empezar un proyecto nuevo con él.
