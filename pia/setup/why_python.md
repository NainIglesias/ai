# Why Python Rules AI

## The Puzzle

Python is one of the slowest mainstream languages. It is interpreted: each line is translated while the program runs, so a loop runs tens of times slower than the same loop compiled from C. And AI is, above all, matrix multiplication, repeated trillions of times: every layer of a neural network and every step of a transformer's attention multiplies matrices. So how can Python be the main language of AI?

## The Answer: Python Describes, Compiled Code Computes

In practice, Python almost never performs the heavy computation of an AI program. It **describes** what to compute and **calls** libraries that do it, and those libraries are written in compiled languages and run on hardware designed for the job:

```text
┌──────────────────────────────────────────────────────────────┐
│ Python: notebooks, training scripts, data preparation        │  ← where AI developers work
├──────────────────────────────────────────────────────────────┤
│ Libraries: NumPy, pandas, scikit-learn, PyTorch, TensorFlow  │  ← Python interface, compiled core
├──────────────────────────────────────────────────────────────┤
│ Compiled engines: BLAS (C, Fortran), cuBLAS (CUDA), C++      │  ← expert-tuned code
├──────────────────────────────────────────────────────────────┤
│ Hardware: CPU cores, GPU with thousands of cores             │
└──────────────────────────────────────────────────────────────┘
```

This is what it means to call Python a **glue language**: it connects fast components written in other languages. The slowness of its interpreter costs a little on each call, but nothing on the billions of operations performed inside each call.

A glue language is a kind of **scripting language**: one made for writing programs quickly, which run straight away, without a compile step, and drive other software. Python's strengths are those of a good scripting language, and they are why AI developers work in Python and not in C:

- **It is easy to read and write.** Its code looks close to pseudocode, so scientists, analysts and students who are not professional programmers can use it, and programs are short: no types to declare, no memory to manage.
- **It is interactive.** Notebooks and the interpreter run a piece of code and show the result at once, which is what exploring data and testing ideas requires.
- **It connects easily to compiled code.** Libraries written in C, C++ or Fortran can be called from Python, through its C interface and tools such as Cython, ctypes and pybind11. This is what lets it be the glue.
- **It has the ecosystem and the community.** NumPy, pandas, scikit-learn, PyTorch and Hugging Face are all used from Python, and new models, tutorials and research code are published in Python first. Because everyone uses it, most courses, answers and examples are in Python, which attracts even more users.

## The Journey in Numbers

The same multiplication of two large matrices, measured on one computer. Other computers give other numbers, but similar proportions.

| How the matrices were multiplied | GFLOPS (billions of operations per second) | Compared with pure Python |
|---|---|---|
| Pure Python, three nested loops | 0.11 | 1× |
| C, the same three loops | 2.4 | about 20× |
| C, loops reordered to read memory in order | 35 | about 300× |
| NumPy (BLAS, all CPU cores) | 500 | about 5,000× |
| A hand-written CUDA kernel on the GPU (32-bit numbers) | 1,500 | about 15,000× |
| cuBLAS on the GPU (32-bit numbers) | 17,000 | about 150,000× |
| cuBLAS on the GPU (16-bit numbers, tensor cores) | 49,000 | about 450,000× |

From the first row to the last, the same operation runs almost half a million times faster. And every row from NumPy downwards is started with a single line of Python.

## What Happens in a Real AI Workflow

Consider one step of training a neural network with PyTorch. In Python, the programmer writes something like "take this batch of examples, pass it through the model, measure the error, adjust the weights". Each of those phrases is one or a few Python calls. Behind them, PyTorch's C++ core decides what to do, and cuBLAS and other CUDA libraries perform billions of multiplications on the GPU. The Python part of each step takes microseconds; the GPU part takes milliseconds. Python's slowness is simply not where the time goes.

The same is true outside deep learning: pandas runs its table operations in C, and scikit-learn trains its models in Cython, C and C++.

## Why the Combination Works

- **Each language does what it is best at.** Python for writing and trying ideas quickly; C, C++ and CUDA for computing at the speed of the hardware.
- **Experts optimise once, everyone benefits.** A handful of specialists tune BLAS and cuBLAS for each new processor, and every Python program that multiplies matrices becomes faster without changing a line.
- **The hardware keeps improving underneath.** When a new GPU arrives, the libraries are updated to use it, and Python code written years earlier runs on it unchanged.

## The Limit: When the Glue Itself Is Slow

The combination breaks down when a program does its heavy work in Python loops instead of library calls: for example, processing a dataset value by value in a `for` loop. Then the interpreter is back in the path of the work. The fix is almost always the same: express the work as operations on whole arrays or tables (**vectorisation**, which [Python data essentials](../python-data-essentials/README.md) practises with NumPy and pandas), or, when no library function fits, compile that part with a tool such as Numba.

## Python Is Getting Faster, and It Doesn't Change the Picture

CPython itself is speeding up. Python 3.13 shipped an experimental *free-threaded* build without the global interpreter lock (GIL), so that threads can run Python code on several cores at once, and an experimental just-in-time compiler; in 3.14 the free-threaded build became officially supported, though still optional ([PEP 779](https://peps.python.org/pep-0779/)). These help programs whose time goes into Python code itself. They don't change the division of labour above: the heavy computation of AI still runs in compiled libraries.

## Measure It Yourself

[compare-python-c-efficiency](https://github.com/avidaldo/compare-python-c-efficiency) builds every row of the table above in notebooks you can run: the same multiplication in Python and in C, NumPy calling BLAS, and CUDA on a GPU, with optional notebooks on memory, compilers and GPU performance. It needs a C compiler, and an NVIDIA GPU or Google Colab for the GPU part.
