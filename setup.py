import os
from setuptools import setup

def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except IOError:
        return ''

setup(
    name = "lang-trans",
    version = "0.2.2",
    author = "Abdelkrime Aries",
    author_email = "kariminfo0@gmail.com",
    description = ("Python transliteration library"),
    license = "Apache-2.0",
    keywords = "transliteration nlp languages romanization",
    url = "https://github.com/kariminf/lang-trans",
    packages=['lang_trans', 'lang_trans.arabic'],
    long_description=readme()
)
