# File: setup.py
from setuptools import setup, find_packages

setup(
    name="quantum_nexus",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
    ],
    author="Eric Pace",
    author_email="sdgwprime@gmail.com",
    description="Quantum Synthesis Nexus Implementation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)