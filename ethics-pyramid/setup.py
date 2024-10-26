```python
# setup.py

from setuptools import setup, find_packages

setup(
    name="ethics_pyramid",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "pyyaml>=5.4.1",
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=21.5b2",
            "flake8>=3.9.2",
            "isort>=5.9.1",
        ]
    },
    author="SDWG Team",
    author_email="team@sdwg.dev",
    description="The Ethics Pyramid: A Quantum-Runic Framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sdwg/ethics-pyramid",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
```