# Tutorial de conda: gestión de entornos y paquetes

> La alternativa a [uv](uv_tutorial.md) en estos módulos. Todo repositorio del curso lista sus dependencias en `requirements.txt`, que un entorno de conda instala con pip. Conda es la mejor opción si ya lo usas, o si necesitas programas que no son paquetes de Python, como ffmpeg o un toolkit de CUDA.

Conda es un sistema de gestión de paquetes y entornos de código abierto que funciona en Windows, macOS y Linux. Se usa mucho en las comunidades de ciencia de datos y aprendizaje automático.

## 1. Instalación

Instala **Miniforge**, el instalador mínimo de la comunidad, en lugar de la distribución completa de Anaconda: solo instala conda y Python, y por defecto toma los paquetes del canal comunitario `conda-forge`. Ese canal es gratuito para todo el mundo, mientras que el canal por defecto de Anaconda exige una licencia de pago en organizaciones de 200 personas o más, y por eso muchas empresas y universidades se han pasado a Miniforge.

1.  **Descarga el instalador** para tu sistema operativo desde las [versiones de Miniforge](https://github.com/conda-forge/miniforge).

2.  **Ejecuta el instalador**: sigue las instrucciones de tu sistema operativo. En macOS y Linux, permite que inicialice conda, lo que hace que esté disponible en tu terminal; en Windows, usa el *Miniforge Prompt* que añade al menú Inicio.

3.  **Comprueba la instalación**: abre una terminal nueva y ejecuta:
    ```bash
    conda --version
    ```
    Deberías ver la versión de conda instalada.

## 2. Instalar un repositorio del curso

Conda proporciona Python y el entorno; pip, dentro de él, instala los paquetes de `requirements.txt`:

```bash
conda create --name ai python=3.13
conda activate ai
cd <repositorio>
pip install -r requirements.txt
```

Conda y pip pueden compartir un entorno si conda va primero: instala con conda lo que necesites y después ejecuta pip. Instalar con conda después de pip puede romper los paquetes que instaló pip, así que si más adelante necesitas otro paquete de conda (ffmpeg, por ejemplo), lo más seguro es recrear el entorno en ese orden.

## 3. Gestionar entornos

Un entorno de conda es un directorio que contiene una colección concreta de paquetes de conda que has instalado.

### Crear un entorno

Para crear un entorno nuevo, usa `conda create`. Es buena práctica indicar la versión de Python que quieres usar.

```bash
# Crea un entorno llamado 'myenv' con Python 3.13
conda create --name myenv python=3.13
```

También puedes instalar paquetes a la vez:

```bash
conda create --name myenv python=3.13 numpy pandas jupyter
```

### Activar y desactivar un entorno

Antes de poder usar un entorno, tienes que activarlo.

```bash
# Activa el entorno
conda activate myenv
```

El prompt de tu terminal debería cambiar para mostrar el nombre del entorno activo.

Para desactivar el entorno actual y volver al entorno base:

```bash
# Desactiva el entorno
conda deactivate
```

### Listar los entornos

Para ver una lista de todos tus entornos:

```bash
conda env list
```

El entorno activo aparecerá marcado con un asterisco (*).

### Eliminar un entorno

Para borrar un entorno y todos los paquetes instalados en él:

```bash
# Asegúrate de que el entorno no está activo
conda deactivate

# Elimina el entorno
conda env remove --name myenv
```

## 4. Gestionar paquetes

Con el entorno activado, puedes instalar, actualizar y eliminar paquetes.

### Instalar paquetes

Usa `conda install` para instalar paquetes de los canales del entorno (con Miniforge, `conda-forge`).

```bash
# Activa primero tu entorno
conda activate myenv

# Instala paquetes
conda install numpy pandas scikit-learn
```

También puedes indicar versiones de los paquetes:

```bash
conda install "numpy>=2.1"
```

### Instalar desde otros canales

Un paquete que no está en `conda-forge` puede estar en otro canal, que indicas con `-c`:

```bash
conda install -c some-channel some-package
```

### Listar los paquetes instalados

Para ver todos los paquetes instalados en el entorno actual:

```bash
conda list
```

### Actualizar paquetes

Para actualizar un paquete concreto:

```bash
conda update numpy
```

Para actualizar todos los paquetes del entorno:

```bash
conda update --all
```

### Eliminar paquetes

Para desinstalar un paquete:

```bash
conda remove scikit-learn
```

## 5. Compartir entornos

Puedes compartir tu entorno con otras personas exportando su especificación a un archivo YAML.

### Exportar un entorno

1.  Activa el entorno que quieres exportar.
    ```bash
    conda activate myenv
    ```
2.  Exporta el entorno a un archivo (normalmente llamado `environment.yml`).
    ```bash
    conda env export --from-history > environment.yml
    ```

Con `--from-history`, el archivo lista solo los paquetes que pediste, así que también funciona en otros sistemas operativos; sin esa opción, fija la build exacta de cada paquete, lo que a menudo falla en otro sistema. Los paquetes instalados con pip no aparecen en él: mantenlos en `requirements.txt`.

### Crear un entorno a partir de un archivo

Para crear un entorno a partir de un archivo `environment.yml`:

```bash
conda env create -f environment.yml
```

Esto creará un entorno nuevo con el mismo nombre y los mismos paquetes que indica el archivo.
