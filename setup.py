import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bkkfutar",
    version="0.2",
    author="Gabor Simon",
    author_email="simonghun@gmail.com",
    description="A simple client for BKK Futar API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabor-simon/bkk-futar-python-client",
    packages=setuptools.find_packages(exclude=("tests",)),
    install_requires=[
          'requests',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)