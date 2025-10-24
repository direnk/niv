from setuptools import setup, find_packages

setup(
    name="niv",
    version="1.0.0",
    author="Diren Kumaratilleke",
    author_email="",
    description="National Impact Velocity – Throughput-based framework for network control (DARPA Challenge 2)",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "networkx",
        "pandas_datareader",
        "pyyaml",
    ],
    python_requires=">=3.10",
    license="MIT",
)
