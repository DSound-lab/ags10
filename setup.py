from setuptools import setup, find_packages

setup(
    name="ags10",
    version="1.0.0",
    author="Dennis",
    description="AGS10 TVOC sensor python library using smbus2",
    packages=find_packages(),
    install_requires=["smbus2>=0.4.2"],
    python_requires=">=3.7",
)
