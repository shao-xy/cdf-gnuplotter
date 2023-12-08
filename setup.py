from setuptools import setup
from core.configs import VERSION

setup(
    name='cdf-genplotter',
    version=str(VERSION),
    packages=['core'],  # Add your subdirectories here
    scripts=['cdf-genplot'],  # Add your executables here
    install_requires=[
        # Add any dependencies your project requires
    ],
)
