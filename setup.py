import os
from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name = "lang-trans",
    version = "0.2.1",
    author = "Abdelkrime Aries",
    author_email = "kariminfo0@gmail.com",
    description = ("Python transliteration library"),
    license = "Apache-2.0",
    keywords = "transliteration nlp languages romanization",
    url = "https://github.com/kariminf/lang-trans",
    packages=['lang_trans', 'lang_trans.arabic'],
    long_description=long_description
)
