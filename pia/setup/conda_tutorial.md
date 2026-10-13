# Conda Tutorial: Environment and Package Management

> The alternative to [uv](uv_tutorial.md) in these modules. Every course repository lists its dependencies in `requirements.txt`, which a conda environment installs with pip. Conda is the better choice if you already use it, or if you need programs that aren't Python packages, such as ffmpeg or a CUDA toolkit.

Conda is an open-source package and environment management system that runs on Windows, macOS, and Linux. It is widely used in the data science and machine learning communities.

## 1. Installation

Install **Miniforge**, the community's minimal installer, rather than the full Anaconda distribution: it installs only conda and Python, and takes packages from the community channel `conda-forge` by default. That channel is free for everyone, while Anaconda's own default channel requires a paid licence in organisations of 200 or more people, which is why many companies and universities have moved to Miniforge.

1.  **Download the installer** for your operating system from the [Miniforge releases](https://github.com/conda-forge/miniforge).

2.  **Run the installer**: Follow the instructions for your OS. On macOS and Linux, allow it to initialise conda, which makes it available in your terminal; on Windows, use the *Miniforge Prompt* that it adds to the Start menu.

3.  **Verify installation**: Open a new terminal and run:
    ```bash
    conda --version
    ```
    You should see the installed conda version.

## 2. Installing a Course Repository

Conda provides Python and the environment; pip, inside it, installs the packages of `requirements.txt`:

```bash
conda create --name ai python=3.13
conda activate ai
cd <repository>
pip install -r requirements.txt
```

Conda and pip can share an environment if conda goes first: install what you need with conda, then run pip. Installing with conda after pip can break the packages pip installed, so if you later need another conda package (ffmpeg, say), the safest course is to recreate the environment in that order.

## 3. Managing Environments

A conda environment is a directory that contains a specific collection of conda packages that you have installed.

### Create an Environment

To create a new environment, use `conda create`. It's good practice to specify the Python version you want to use.

```bash
# Creates an environment named 'myenv' with Python 3.13
conda create --name myenv python=3.13
```

You can also install packages at the same time:

```bash
conda create --name myenv python=3.13 numpy pandas jupyter
```

### Activate and Deactivate an Environment

Before you can use an environment, you need to activate it.

```bash
# Activate the environment
conda activate myenv
```

Your terminal prompt should change to show the name of the active environment.

To deactivate the current environment and return to the base environment:

```bash
# Deactivate the environment
conda deactivate
```

### List Environments

To see a list of all your environments:

```bash
conda env list
```

The active environment will be marked with an asterisk (*).

### Remove an Environment

To delete an environment and all the packages installed in it:

```bash
# Make sure the environment is not active
conda deactivate

# Remove the environment
conda env remove --name myenv
```

## 4. Managing Packages

With your environment activated, you can install, update, and remove packages.

### Install Packages

Use `conda install` to install packages from the environment's channels (with Miniforge, `conda-forge`).

```bash
# Activate your environment first
conda activate myenv

# Install packages
conda install numpy pandas scikit-learn
```

You can also specify package versions:

```bash
conda install "numpy>=2.1"
```

### Install from other channels

A package that isn't in `conda-forge` may be in another channel, which you name with `-c`:

```bash
conda install -c some-channel some-package
```

### List Installed Packages

To see all packages installed in the current environment:

```bash
conda list
```

### Update Packages

To update a specific package:

```bash
conda update numpy
```

To update all packages in the environment:

```bash
conda update --all
```

### Remove Packages

To uninstall a package:

```bash
conda remove scikit-learn
```

## 5. Sharing Environments

You can share your environment with others by exporting its specification to a YAML file.

### Export an Environment

1.  Activate the environment you want to export.
    ```bash
    conda activate myenv
    ```
2.  Export the environment to a file (commonly named `environment.yml`).
    ```bash
    conda env export --from-history > environment.yml
    ```

With `--from-history`, the file lists only the packages you asked for, so it also works on other operating systems; without it, it pins the exact build of every package, which often fails on another system. Packages installed with pip are not in it: keep them in `requirements.txt`.

### Create an Environment from a File

To create an environment from an `environment.yml` file:

```bash
conda env create -f environment.yml
```

This will create a new environment with the same name and packages as specified in the file.
