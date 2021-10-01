from setuptools import setup

setup(
    name='lnrec',
    version='0.1.0',
    author='Nate Chodosh',
    author_email='nchodosh@gmail.com',
    packages=['lnrec'],
    description='A simple package for recursively linking files',
    scripts=['bin/lnr'],
    install_requires=['fire'],
)
