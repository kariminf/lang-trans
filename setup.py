import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "lang-trans",
    version = "0.2.0",
    author = "Abdelkrime Aries",
    author_email = "kariminfo0@gmail.com",
    description = ("Python transliteration library"),
    license = "Apache-2.0",
    keywords = "transliteration nlp languages romanization",
    url = "https://github.com/kariminf/lang-trans",
    packages=['lang_trans', 'lang_trans.arabic'],
    long_description=read('README.md')
)
