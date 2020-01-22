import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wqxtools",
    version="0.0.1",
    author="Emanuel Rodriguez",
    description="A lightweight interface to the WQX Web Services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6"
)
