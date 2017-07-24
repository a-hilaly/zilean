#
from setuptools import setup, find_packages, Command

setup(
    name='Zilean',
    version='0.0.1',
    description='Zlock',
    long_description=readme,
    author='Imp Alpha lab',
    author_email='hilalyamine@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
