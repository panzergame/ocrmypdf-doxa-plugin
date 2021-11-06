from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension("doxapy",
        ["doxa/DoxaPy.cpp"],
        include_dirs=["doxa/Doxa/"],
        cxx_std=17,
    ),
]

setup(
    packages=find_packages(),
    install_requires=[
        "ocrmypdf",
    ],
    python_requires='>=3.7',
    ext_modules=ext_modules
)
