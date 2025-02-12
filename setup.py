from setuptools import setup

setup(
    name="AoAlib",
    version="1.0",
    python_requires=">=3.12, <=3.13",
    install_requires=[
        "numpy==2.1.2",
        "scipy==1.14.1",
        "matplotlib==3.9.2",
        "pybind11==2.13.6",
        "joblib==1.4.2",
        "numiphy@git+https://github.com/phyzan/numiphy.git",
        "henonpy@git+https://github.com/phyzan/henonpy.git",
        "bohmian@git+https://github.com/phyzan/bohmian.git",
    ],
)