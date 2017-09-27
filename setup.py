from setuptools import setup, find_packages

setup(
    name='local_sphinx_test',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version='1',
    description='na',
    author='na',
    url='na',
    keywords=['local_sphinx_test'],
    install_requires=[],
    classifiers=[],
)
