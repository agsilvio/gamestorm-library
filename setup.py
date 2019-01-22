import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gamestorm",
    version="0.0.1",
    author="Silvio Marco Costantini",
    author_email="agsilvio@protonmail.com",
    description="A minimal, batteries included, 2D game engine using grid-based graphics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agsilvio/gamestorm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC-BY-4.0",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[
        'pygame',
        'unittest2',
        'nose2'
    ],
)
