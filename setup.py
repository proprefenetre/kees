from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Kees',
    version='0.1.5',
    author='C. Eigenraam',
    author_email='proprefenetre@gmail.com',
    packages=['src'],
    scripts=['bin/kees'],
    url='https://github.com/proprefenetre/kees',
    license='LICENSE.md',
    description='Translate words to or from Dutch',
    long_description=readme(),
    install_requires=[
        'beautifulsoup4',
    ]
)
