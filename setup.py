import os
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read_file(filename, encoding='utf8'):
    """Read unicode from given file."""
    with codecs.open(filename, encoding=encoding) as fd:
        return fd.read()

here = os.path.abspath(os.path.dirname(__file__))
readme = read_file(os.path.join(here, 'README.rst'))

setup(
    name='fodselsnummer',
    description='For generating and validating of Norwegian "birth numbers" (fodselsnummer)',
    long_description=readme,
    version='1.5',
    license='MIT',
    author='Magnus Watn',
    keywords='fodselsnummer personnummer norway',
    url='https://github.com/magnuswatn/fodselsnummer',
    py_modules=['fodselsnummer'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
)
