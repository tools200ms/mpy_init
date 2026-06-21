from setuptools import setup, Extension
from Cython.Build import cythonize

# Make Cython to generate a C file with a main() function:
options = {"compiler_directives": {"language_level": "3"}}

extensions = [
    Extension(
        "yinit.main",
        ["src/yinit/main.py"],
    ),
    Extension(
        "yinit.runenv",
        ["src/yinit/runenv.py"],
    )
]

setup(
    name="yinit",
    ext_modules=cythonize(extensions, **options),
    package_dir={"": "src"},
    packages=["yinit"],
)
