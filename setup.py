from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "yinit.about",
        ["src/yinit/about.pyx"],
    )
]

setup(
    name="yinit",
    ext_modules=cythonize(extensions, language_level="3"),
    package_dir={"": "src"},
    packages=["yinit"],
)
