from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="measurely-py",
    version="0.1.0",
    packages=find_packages(include=["measurely"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A Python library for interacting with the Measurely API",
    author="Measurely-dev, YasTheGoat, afz",
    author_email="",
    url="https://github.com/measurely-dev/measurely-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
    license="MIT",
)
