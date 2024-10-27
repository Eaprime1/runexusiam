from setuptools import setup, find_packages

setup(
    name="ethics_pyramid",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "pytest>=6.0.0",
    ],
    author="SDWG Team",
    description="Ethics Pyramid: Quantum-Runic Framework",
    python_requires=">=3.8",
)