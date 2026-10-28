# Tutorial de uv: proyectos, entornos y paquetes de Python

`uv` es un gestor de paquetes y proyectos de Python extremadamente rápido, escrito en Rust. Una sola herramienta sustituye a `pip`, `venv`, `pip-tools` y a la mayor parte de lo que hacen Poetry y `pyenv`: crea proyectos, instala paquetes, fija versiones exactas en un archivo de bloqueo (*lock file*), ejecuta código en el entorno adecuado e incluso instala el propio Python.

## 1. Instalación

La forma recomendada es el instalador independiente: no necesita Python, e instala `uv` solo para tu usuario, sin tocar el Python del sistema.

**Con curl (macOS, Linux):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Si no tienes `curl` (Ubuntu no siempre lo incluye), `wget` hace lo mismo y suele estar ya instalado:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

**Con PowerShell (Windows):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Otros métodos (Homebrew, WinGet, pipx y más) están en la [guía de instalación oficial](https://docs.astral.sh/uv/getting-started/installation/).

Cierra y vuelve a abrir la terminal (el instalador añade `~/.local/bin` a tu `PATH`) y después comprueba la instalación:
```bash
uv --version
```

Si probaste `pip install uv` y te salió `externally-managed-environment`, consulta [Solución de problemas](#solución-de-problemas).

## 2. Instalar las dependencias de un repositorio

Esto es lo que harás más a menudo: clonar un repositorio e instalar lo que necesita su código. Todo repositorio de estos módulos lista sus dependencias en `requirements.txt`:

```bash
git clone <url-del-repositorio>
cd <repositorio>
uv venv                              # crea el entorno, en .venv
uv pip install -r requirements.txt   # instala en él las dependencias
```

Si el repositorio tiene además un archivo `uv.lock`, `uv sync` instala en su lugar exactamente las versiones que registra.

Después ejecuta el código en ese entorno, sin activarlo:

```bash
uv run python script.py
uv run pytest
```

`uv run` usa la carpeta `.venv` del directorio actual (o de un directorio padre). Fuera de un proyecto, en un repositorio sin `pyproject.toml`, tiene prioridad un entorno que hayas activado; dentro de un proyecto, uv usa el `.venv` del proyecto y avisa de que ignora el activo. También puedes activar el entorno (siguiente sección) y ejecutar `python` y `pytest` como siempre.

## 3. Gestionar entornos virtuales

`uv` integra la gestión de entornos virtuales, de forma parecida a `venv`.

### Crear un entorno virtual

Para crear un entorno virtual nuevo, usa `uv venv`. Por defecto, crea un directorio `.venv` en tu ubicación actual.

```bash
# Crea un entorno virtual en el directorio .venv
uv venv
```

También puedes elegir la versión de Python. Si esa versión no está instalada, `uv` la descarga:

```bash
# Crea un entorno virtual con Python 3.13
uv venv -p 3.13

# O instala una versión de Python explícitamente
uv python install 3.13
```

### Activar y desactivar el entorno

Para activar el entorno virtual, tienes que ejecutar el script de activación.

**En macOS y Linux:**
```bash
source .venv/bin/activate
```

**En Windows (Símbolo del sistema):**
```batch
.venv\Scripts\activate.bat
```

**En Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

El prompt de tu terminal cambiará para indicar que el entorno virtual está activo.

Para desactivarlo, simplemente ejecuta:
```bash
deactivate
```

### Eliminar un entorno

Un entorno virtual de `uv` es solo un directorio. Para eliminarlo, puedes borrar el directorio.

```bash
# Asegúrate de no estar dentro del entorno
deactivate

# Borra el directorio (macOS, Linux)
rm -rf .venv
```

En Windows, en PowerShell: `Remove-Item -Recurse -Force .venv`.

## 4. Inicializar un proyecto de Python

Para un proyecto propio, `uv` guarda las dependencias que pides en `pyproject.toml`, el archivo de proyecto estándar (PEP 621), y la versión exacta de cada paquete instalado en `uv.lock`.

### Inicializar un proyecto nuevo

Para crear un proyecto de Python nuevo con un `pyproject.toml`:

```bash
uv init my-project
cd my-project
```

Esto crea un proyecto básico: un `pyproject.toml`, un archivo `.python-version`, un `README.md`, un `main.py` y un repositorio de Git.

### Inicializar en un directorio existente

Si ya tienes un directorio de proyecto:

```bash
uv init
```

Esto creará un `pyproject.toml` en el directorio actual.

## 5. Gestionar paquetes con `pyproject.toml`

`uv` gestiona automáticamente tu entorno virtual y tus dependencias cuando usas `uv add` y `uv remove`.

### Añadir paquetes

Usa `uv add` para instalar paquetes y actualizar automáticamente tu `pyproject.toml`:

```bash
# Añade paquetes a tu proyecto
uv add numpy pandas scikit-learn

# Añade una restricción de versión
uv add "numpy>=2.1"

# Añade dependencias de desarrollo
uv add --dev pytest ruff
```

Este comando:
- Crea el entorno virtual si no existe (nunca lo activa: `uv run` lo usa directamente)
- Instala los paquetes
- Actualiza `pyproject.toml` con las dependencias
- Crea o actualiza `uv.lock` para builds reproducibles

En `pyproject.toml`, mejor una cota inferior (`>=`) que una versión exacta (`==`): las versiones exactas ya están en `uv.lock`, y una versión antigua fijada puede dejar de instalarse en un Python más nuevo. NumPy 1.26, por ejemplo, no tiene builds para Python 3.13.

### Eliminar paquetes

Para eliminar un paquete:

```bash
uv remove scikit-learn
```

### Listar los paquetes instalados

Para ver todos los paquetes de tu proyecto:

```bash
uv pip list
```

### Sincronizar dependencias

Para que el entorno coincida exactamente con el archivo de bloqueo, instalando lo que falta y eliminando lo que no aparece (uv actualiza primero `uv.lock` si `pyproject.toml` ha cambiado):

```bash
uv sync
```

Para ver qué paquete necesita cuál, `uv tree` imprime el árbol de dependencias.

## 6. Ejecutar Python con uv

Puedes ejecutar scripts y comandos de Python sin activar manualmente el entorno virtual:

```bash
# Ejecuta un script de Python
uv run python script.py

# Ejecuta un módulo
uv run python -m pytest

# Ejecuta una herramienta instalada
uv run ruff format .
```

`uv run` usa automáticamente el entorno virtual del proyecto.

Para ejecutar una herramienta de línea de comandos una sola vez, sin añadirla al proyecto, usa `uvx` (abreviatura de `uv tool run`):

```bash
uvx ruff check .
```

## 7. Compartir proyectos

Cuando compartas tu proyecto, incluye tanto `pyproject.toml` como `uv.lock` en el control de versiones.

### Clonar y preparar un proyecto

Cualquiera puede replicar tu entorno con:

```bash
# Clona el repositorio
git clone <url-del-repositorio>
cd <directorio-del-proyecto>

# Instala todas las dependencias (crea el venv automáticamente)
uv sync
```

### `requirements.txt`

`requirements.txt` es el formato que leen todas las herramientas (pip, los entornos de conda y uv), y por eso todo repositorio de estos módulos tiene uno, incluso los que tienen `pyproject.toml`. Tiene dos formas:

- **Una lista corta de dependencias directas con versiones mínimas** (`pandas>=2.2`), escrita a mano. Se instala en cualquier sitio, y el instalador elige versiones recientes que encajen entre sí. Es la forma de los repositorios del curso.
- **La lista completa de versiones exactas** de cada paquete, generada a partir de un entorno o de un archivo de bloqueo. Reproduce un entorno exactamente, pero solo en un Python y un sistema operativo parecidos.

```bash
# Instala desde requirements.txt
uv pip install -r requirements.txt

# Añade los paquetes de un requirements.txt al pyproject.toml de tu proyecto
uv add -r requirements.txt

# Escribe las versiones exactas de uv.lock como requirements.txt
uv export --format requirements-txt > requirements.txt
```

`uv pip freeze > requirements.txt` también escribe versiones exactas, pero de lo que esté instalado en ese momento, incluidos paquetes que añadiste a mano y olvidaste: exportar desde el archivo de bloqueo es más seguro.

## 8. Notebooks de Jupyter con uv

Un notebook se ejecuta sobre un kernel, que necesita el paquete `ipykernel` en el entorno:

```bash
uv add --dev ipykernel                  # en un proyecto propio
```

Después elige el entorno `.venv` como kernel del notebook (*Select Kernel* en VS Code). En un repositorio instalado desde `requirements.txt`, el kernel está disponible si sus requisitos incluyen `jupyter` o `ipykernel`. Para abrir JupyterLab en el navegador sin añadirlo a un proyecto:

```bash
uv run --with jupyter jupyter lab
```

## Solución de problemas

### `pip install uv` falla con `externally-managed-environment`

Las versiones recientes de Debian y Ubuntu protegen el Python que viene con el sistema (PEP 668): se rechaza `pip install` en él, porque podría romper las propias herramientas del sistema operativo.

```text
error: externally-managed-environment
× This environment is externally managed
```

No uses `--break-system-packages` ni lo fuerces con `sudo`. Usa el instalador independiente de la primera sección, o:

```bash
sudo apt install pipx   # después: pipx install uv
```

`pipx` instala una aplicación de Python en un entorno propio y pone su comando en tu `PATH`. Si `pipx ensurepath` te lo indica, vuelve a abrir la terminal.

`pip install uv` solo es apropiado dentro de un entorno virtual que hayas creado tú (`python3 -m venv .venv`, que en Ubuntu necesita `sudo apt install python3-venv` o `python3-full`), y ahí solo existe mientras ese entorno esté activo.
