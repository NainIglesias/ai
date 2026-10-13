# uv Tutorial: Python Projects, Environments and Packages

`uv` is an extremely fast Python package and project manager, written in Rust. One tool replaces `pip`, `venv`, `pip-tools` and most of what Poetry and `pyenv` do: it creates projects, installs packages, pins exact versions in a lock file, runs code in the right environment, and even installs Python itself.

## 1. Installation

You can install `uv` with its standalone installer, or with `pip` if you already have Python installed.

**Using curl (macOS, Linux):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Using PowerShell (Windows):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Using pip:**
```bash
pip install uv
```

Verify the installation:
```bash
uv --version
```

## 2. Installing a Repository's Dependencies

This is what you will do most often: clone a repository and install what its code needs. Every repository of these modules lists its dependencies in `requirements.txt`:

```bash
git clone <repository-url>
cd <repository>
uv venv                              # create the environment, in .venv
uv pip install -r requirements.txt   # install the dependencies into it
```

If the repository also has a `uv.lock` file, `uv sync` installs exactly the versions it records instead.

Then run the code in that environment, without activating it:

```bash
uv run python script.py
uv run pytest
```

`uv run` uses the `.venv` folder of the current directory (or of a parent directory). Outside a project, in a repository without a `pyproject.toml`, an environment you have activated takes precedence; inside a project, uv uses the project's `.venv` and warns that it ignores the active one. You can also activate the environment (next section) and run `python` and `pytest` as usual.

## 3. Managing Virtual Environments

`uv` integrates virtual environment management, similar to `venv`.

### Create a Virtual Environment

To create a new virtual environment, use `uv venv`. By default, it creates a `.venv` directory in your current location.

```bash
# Create a virtual environment in the .venv directory
uv venv
```

You can also choose the Python version. If that version is not installed, `uv` downloads it:

```bash
# Create a virtual environment with Python 3.13
uv venv -p 3.13

# Or install a Python version explicitly
uv python install 3.13
```

### Activate and Deactivate the Environment

To activate the virtual environment, you need to run the activation script.

**On macOS and Linux:**
```bash
source .venv/bin/activate
```

**On Windows (Command Prompt):**
```batch
.venv\Scripts\activate.bat
```

**On Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

Your terminal prompt will change to indicate that the virtual environment is active.

To deactivate it, simply run:
```bash
deactivate
```

### Removing an Environment

A `uv` virtual environment is just a directory. To remove it, you can delete the directory.

```bash
# Make sure you are not inside the environment
deactivate

# Remove the directory (macOS, Linux)
rm -rf .venv
```

On Windows, in PowerShell: `Remove-Item -Recurse -Force .venv`.

## 4. Initialising a Python Project

For a project of your own, `uv` keeps the dependencies you ask for in `pyproject.toml`, the standard project file (PEP 621), and the exact version of every installed package in `uv.lock`.

### Initialise a New Project

To create a new Python project with a `pyproject.toml`:

```bash
uv init my-project
cd my-project
```

This creates a basic project: a `pyproject.toml`, a `.python-version` file, a `README.md`, a `main.py`, and a Git repository.

### Initialise in an Existing Directory

If you already have a project directory:

```bash
uv init
```

This will create a `pyproject.toml` in the current directory.

## 5. Managing Packages with `pyproject.toml`

`uv` automatically manages your virtual environment and dependencies when you use `uv add` and `uv remove`.

### Add Packages

Use `uv add` to install packages and automatically update your `pyproject.toml`:

```bash
# Add packages to your project
uv add numpy pandas scikit-learn

# Add a version constraint
uv add "numpy>=2.1"

# Add development dependencies
uv add --dev pytest ruff
```

This command:
- Creates the virtual environment if it doesn't exist (it never activates it: `uv run` uses it directly)
- Installs the packages
- Updates `pyproject.toml` with the dependencies
- Creates/updates `uv.lock` for reproducible builds

Prefer a lower bound (`>=`) to an exact pin (`==`) in `pyproject.toml`: the exact versions are already in `uv.lock`, and an old pin can stop installing on a newer Python. NumPy 1.26, for example, has no builds for Python 3.13.

### Remove Packages

To remove a package:

```bash
uv remove scikit-learn
```

### List Installed Packages

To see all packages in your project:

```bash
uv pip list
```

### Sync Dependencies

To make the environment match the lock file exactly, installing what is missing and removing what isn't listed (uv first updates `uv.lock` if `pyproject.toml` changed):

```bash
uv sync
```

To see which package needs which, `uv tree` prints the dependency tree.

## 6. Running Python with uv

You can run Python scripts and commands without manually activating the virtual environment:

```bash
# Run a Python script
uv run python script.py

# Run a module
uv run python -m pytest

# Run an installed tool
uv run ruff format .
```

`uv run` automatically uses the project's virtual environment.

To run a command-line tool once, without adding it to the project, use `uvx` (short for `uv tool run`):

```bash
uvx ruff check .
```

## 7. Sharing Projects

When sharing your project, include both `pyproject.toml` and `uv.lock` in version control.

### Clone and Setup a Project

Anyone can replicate your environment with:

```bash
# Clone the repository
git clone <repository-url>
cd <project-directory>

# Install all dependencies (creates venv automatically)
uv sync
```

### `requirements.txt`

`requirements.txt` is the format every tool reads (pip, conda environments and uv), which is why every repository of these modules has one, even those with a `pyproject.toml`. It comes in two forms:

- **A short list of direct dependencies with minimum versions** (`pandas>=2.2`), written by hand. It installs anywhere, and the installer picks recent versions that fit together. This is the form of the course repositories.
- **The full list of exact versions** of every package, generated from an environment or a lock. It reproduces one environment exactly, but only on a similar Python and operating system.

```bash
# Install from requirements.txt
uv pip install -r requirements.txt

# Add the packages of a requirements.txt to your project's pyproject.toml
uv add -r requirements.txt

# Write the exact versions of uv.lock as a requirements.txt
uv export --format requirements-txt > requirements.txt
```

`uv pip freeze > requirements.txt` also writes exact versions, but from whatever happens to be installed, including packages you added by hand and forgot: exporting from the lock is safer.

## 8. Jupyter Notebooks with uv

A notebook runs on a kernel, which needs the `ipykernel` package in the environment:

```bash
uv add --dev ipykernel                  # in a project of your own
```

Then choose the `.venv` environment as the notebook's kernel (*Select Kernel* in VS Code). In a repository installed from `requirements.txt`, the kernel is there if its requirements include `jupyter` or `ipykernel`. To open JupyterLab in the browser without adding it to a project:

```bash
uv run --with jupyter jupyter lab
```
