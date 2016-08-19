from setuptools import setup

setup(
    name='samuel',
    description='Small app for translating words to or from Dutch, using'
    'the online dictionary www.mijnwoordenboek.nl',
    version='1.0',
    url='https://github.com/proprefenetre/samuel',
    author='Cornelis Eigenraam',
    author_email='proprefenetre@gmail.com',
    scripts=['bin/samuel'],
    packages=['samuel'],
    license='MIT',
    keywords='translation, translate, synonyms, synonym, dictionary, dutch'
)
