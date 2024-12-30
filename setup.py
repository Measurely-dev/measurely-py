from setuptools import find_packages, setup

setup(
    name="measurely-py",
    version="0.1.0",
    packages=find_packages(include=["measurely"]),
    description="A Python library for interacting with the Measurely API",
    author="YasTheGoat, afz",
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
    project_urls={
        "Author 1": "https://github.com/yasthegoat",
        "Author 2": "https://github.com/zxk-afz",
    },
    license="MIT",
)
