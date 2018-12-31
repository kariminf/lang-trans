import os
from setuptools import setup

def readme():
    try:
        with open("README.md") as f:
            return f.read()
    except IOError:
        return ""

setup(
    name = "lang-trans",
    version = "0.6.0",
    author = "Abdelkrime Aries",
    author_email = "kariminfo0@gmail.com",
    description = ("Python transliteration library"),
    license = "Apache-2.0",
    keywords = "transliteration nlp languages romanization",
    url = "https://github.com/kariminf/lang-trans",
    packages=["lang_trans"],
    long_description=readme(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Build Tools"
    ],
)
