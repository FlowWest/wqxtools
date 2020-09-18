import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
LONG_DESCRIPTION = (HERE / "README.md").read_text()

INSTALL_REQUIRES = ["requests"]

setup(
    name="wqxtools",
    version="0.0.1",
    author="Emanuel Rodriguez",
    description="A lightweight interface to the WQX Web Services",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=["License :: OSI Approved :: MIT License"],
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
)
