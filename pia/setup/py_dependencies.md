# Dependency and Virtual Environment Management in Python

## The Evolution of Dependency Management in Python

As Python's popularity grew in the 2000s, the need for effective library management became critical. Without an efficient system to install and organise libraries, projects could easily fall into **"dependency hell"**, a scenario where package version conflicts make a project difficult to maintain and deploy. This problem is exacerbated **when different versions of the same libraries are needed for different projects**.

***

### 1. **Pip**: The Standard Package Manager

`pip` emerged in 2008 and became the standard for installing packages from the official [**Python Package Index (PyPI)**](https://pypi.org/) with a simple command (`pip install package`).

To reproduce a project's environment, `pip` uses `requirements.txt` files, which list the necessary libraries with specific versions.
  
**Advantages**:
- **Lightweight** and simple.
- Highly flexible and compatible with any Python project.
- It is the default choice for nearly every Python developer.

**Limitations**:
- **The System's Python**: on recent Linux distributions and on macOS's Homebrew, `pip install` outside a virtual environment stops with an `externally-managed-environment` error ([PEP 668](https://peps.python.org/pep-0668/)). That Python belongs to the operating system's package manager, and a virtual environment is the expected place for your packages.
- **Separation of Concerns**: `pip` does not natively manage virtual environments. Its philosophy is to focus solely on package management, requiring it to be combined with tools like `venv` or `virtualenv` to isolate dependencies.
- **Dependency Resolution**: Although the **new resolver introduced in `pip 20.3`** significantly improved conflict management, `pip` has long lacked a lock file that guarantees identical installations across machines, unlike tools such as Poetry or Pipenv. Since version 25.1 it has an experimental `pip lock` command, which writes the standard lock file of PEP 751, `pylock.toml`, valid only for the Python version and platform that produced it.

***

### 2. Virtualenv and venv: Dependency Isolation

Even before `pip`, **virtualenv** was created to **isolate project dependencies**. This prevents conflicts between different versions of the same libraries used in various projects by creating **virtual environments**—isolated directories where dependencies can be installed without affecting the global Python installation.
 
Starting with **Python 3.3**, Python introduced **`venv`**, an integrated and lighter tool for creating virtual environments, making it the standard and eliminating the need to install `virtualenv` separately for basic use.

**Example of `venv` usage**:
```bash
# Create a virtual environment named .venv
python3 -m venv .venv

# Activate the environment (on Linux/macOS)
source .venv/bin/activate

# Now, any package installed with pip will be contained within .venv
pip install numpy

# Deactivate the environment
deactivate
```

***

### 3. Conda: Multi-language Package Management and Virtual Environments

`Conda` was launched in 2012 as part of the **Anaconda** distribution, which is especially geared towards data science and machine learning. Unlike `pip`, it is a **multi-language** package manager (it can install packages for Python, R, and others, including non-Python system-level dependencies).

`Conda` offers **pre-compiled** packages, which simplified the installation of complex libraries like `numpy` or `pandas` at a time when installing them with `pip` often meant compiling them.

**Advantages of Conda in Machine Learning**:
- **Integrated Virtual Environments**: `Conda` manages both dependencies and virtual environments in an integrated manner.
- **Packages for ML and Data Science**: `Conda` became popular in machine learning and data science because it shipped **pre-built, optimised libraries** (like `NumPy` and `scikit-learn`) at a time when installing them with `pip` often meant compiling them.
- **Complex Dependency Management**: It excels at managing non-Python dependencies (like specific C libraries) that can be problematic when installing with `pip` alone.

That second advantage has faded. Today PyPI distributes pre-built wheels for almost every scientific library, GPU builds of PyTorch included, and PyTorch stopped publishing to its own Anaconda channel after version 2.5 (conda users now get it from the community-run `conda-forge` channel).

**Limitations**:
- **Heavier Footprint**: `Conda` requires more disk space than `pip` and its modern alternatives. Its dependency solver was notoriously slow until conda 23.10 (2023) made the much faster libmamba solver the default.
- **Unnecessary Complexity for Small Projects**: For small or simple projects that only require Python libraries, a `pip`/`venv` or `uv` approach is a lighter option.

**Pixi** (2023), a fast tool written in Rust, manages conda-forge packages (and PyPI ones) per project with a lock file: it is to conda roughly what uv is to pip.

***

### 4. Advanced Tooling: Pipenv, Poetry, and uv

Over time, more advanced tools emerged to address the limitations of earlier tools and offer a more integrated experience in managing virtual environments and dependencies.

- **Pipenv** (2017): Was one of the first attempts to unify package and environment management. It introduces the `Pipfile` for declaring dependencies (separating production and development) and the `Pipfile.lock` to pin exact versions, ensuring reproducibility.
  
- **Poetry** (2018): Has established itself as one of the most comprehensive tools. It goes beyond Pipenv, offering a more robust dependency resolution system and integrated tools for building and publishing packages to PyPI. It uses the standard `pyproject.toml`, which centralises not only dependencies but all project configurations (linters, formatters, etc.).

#### **uv: The Next-Generation Package Manager (2024)**

**`uv`** is a high-performance, **Rust-based** package and project manager. It started in 2024 as a fast replacement for `pip`, and it now covers the whole workflow of a Python project.

**Key Features of uv**:
- **Extreme Speed**: `uv` completes installation and dependency resolution **10 to 100 times faster** than `pip`, `pip-tools` and Poetry.
- **Project Management**: `uv init`, `uv add`, `uv lock`, `uv sync` and `uv run` manage a project declared in the standard `pyproject.toml`, with exact versions pinned in `uv.lock`. `uv build` and `uv publish` package it for PyPI.
- **Integrated Environments and Python Versions**: `uv` creates and manages virtual environments, and it can install Python itself (`uv python install 3.13`), so no separate `pyenv` is needed.
- **Compatibility**: It works with existing standards, including `requirements.txt` and `pyproject.toml`, so it is easy to adopt in existing projects.

**Impact**: `uv` has quickly become a common choice for new Python projects, and it is the tool recommended in these modules.


***

## Comparison Table

| Feature                 | `pip` + `venv`                               | `conda`                                     | `Poetry`                                       | `uv`                                                 |
| ----------------------- | -------------------------------------------- | ------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| **Environment Mgmt**    | Yes (with `venv`)                            | Yes (integrated)                            | Yes (integrated)                               | Yes (integrated and ultra-fast)                      |
| **Package Mgmt**        | Python (PyPI)                                | Python, R, C/C++, etc. (Anaconda, Conda-Forge) | Python (PyPI)                                  | Python (PyPI)                                        |
| **Configuration File**  | `requirements.txt` (flexible versions)       | `environment.yml`                           | `pyproject.toml`                               | `pyproject.toml` + `uv.lock`                         |
| **Non-Python Deps**     | No (requires system package managers)        | Yes (its key strength)                      | No                                             | No                                                   |
| **Python Versions**     | No                                           | Yes                                         | Experimental (`poetry python install`, 2.1+)   | Yes (`uv python install`)                            |
| **Speed**               | Moderate                                     | Moderate (libmamba solver since 2023)       | Moderate-to-Slow                               | **Extremely fast**                                   |
| **Project Mgmt**        | No                                           | No                                          | Yes (build, publish, scripts)                  | Yes (init, add, lock, sync, run, build, publish)     |
| **Ideal for...**        | Simple scripts, learning the basics.         | Projects with heavy non-Python dependencies; the alternative in these modules. | Libraries and applications (older projects).   | Any Python project; the default in these modules.    |

***

## Conclusion: Which Tool to Choose?

The choice depends on the project's complexity and ecosystem:

- **For any new Python project**, including machine learning: **`uv`**. It manages the project, its environment, its locked dependencies and even the Python version, and it is what we use in these modules.

- **To understand the fundamentals**: the combination of **`pip` and `venv`** is still worth knowing, because it is what every other tool automates and what you will find in older projects and tutorials.

- **For projects with heavy non-Python dependencies** (specific CUDA toolkits, compiled scientific libraries, programs such as ffmpeg, other languages): **`Conda`** through `conda-forge` still earns its place. It is also the alternative to uv in these modules: every course repository installs with either. See the [conda tutorial](conda_tutorial.md).

- **For existing Poetry projects**: keep **`Poetry`** where it is already in use; there is little reason to start a new project with it.
