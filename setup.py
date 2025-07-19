from setuptools import setup, find_packages

setup(
    name="secure-seed",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["psutil"],
    python_requires=">=3.7",
)
