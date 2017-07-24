#
from setuptools import setup, find_packages, Command


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


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
