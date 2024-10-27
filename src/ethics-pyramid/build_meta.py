# src/ethics_pyramid/build_meta.py

from setuptools import setup, find_packages
import os
import sys

def read_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def get_package_info():
    return {
        'name': 'ethics_pyramid',
        'version': '0.1.0',
        'packages': find_packages(where='src'),
        'package_dir': {'': 'src'},
        'install_requires': read_requirements('requirements.txt'),
        'author': 'SDWG Team',
        'description': 'Quantum-Runic Ethics Framework',
        'python_requires': '>=3.9',
    }

if __name__ == '__main__':
    setup(**get_package_info())