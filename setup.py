from setuptools import setup

setup(
    name='Kees',
    version='0.1.0',
    author='C. Eigenraam',
    author_email='proprefenetre@gmail.com',
    packages=['src'],
    url='https://github.com/proprefenetre/kees',
    license='LICENSE.md',
    description='Translate words to or from Dutch',
    long_description=open('README.md').read(),
    install_requires=['bs4']
)
