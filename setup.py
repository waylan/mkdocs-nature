from setuptools import setup, find_packages

VERSION = '0.2'

with open('README.rst', mode='r') as fd:
    long_description = fd.read()

setup(
    name="mkdocs-nature",
    version=VERSION,
    url='https://waylan.github.io/mkdocs-nature/',
    license='BSD',
    description='A MkDocs theme. A clone of the "greenish" Sphinx theme of the same name.',
    long_description=long_description,
    author='Waylan Limberg',
    author_email='waylan.limberg@icloud.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mkdocs>=0.17'],
    entry_points={
        'mkdocs.themes': [
            'nature = nature',
        ]
    },
    zip_safe=False
)
