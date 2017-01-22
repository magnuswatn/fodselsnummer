try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='fodselsnummer',
    description='For generating and validating of Norwegian "birth numbers" (fodselsnummer)',
    version='1.1',
    license='MIT',
    author='Magnus Watn',
    url='https://github.com/magnuswatn/fodselsnummer',
    py_modules=['fodselsnummer'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
)
