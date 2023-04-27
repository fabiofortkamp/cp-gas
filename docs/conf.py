"""Sphinx configuration."""
project = "Correlations for Specific Heat of Gases"
author = "Fábio Fortkamp"
copyright = "2023, Fábio Fortkamp"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
