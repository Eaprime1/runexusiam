#```python
# docs/conf.py

project = 'Ethics Pyramid'
copyright = '2024, SDWG Team'
author = 'SDWG Team'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/ethics_pyramid_logo.png'

# Custom styling for quantum-runic elements
html_css_files = [
    'custom.css',
]
