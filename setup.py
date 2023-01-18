from setuptools import find_packages, setup

setup(
    name='sqlite_server',
    packages=find_packages(include=['sqlite_server']),
    version='0.1.0',
    description='On request SQLite server',
    author='osmocode',
    license='MIT'
)