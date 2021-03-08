import setuptools


with open("README.md", "r") as lg:
    long_description = lg.read()

setuptools.setup(
    name="jwrap",
    py_modules=['jwrap'],
    version="0.3",
    author="gd",
    author_email="gechandev@gmail.com",
    description="Wrapper for easy interacting with JSON files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitea.gch.icu/gd/jwrap/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
