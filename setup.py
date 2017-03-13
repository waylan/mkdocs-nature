from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="mkdocs-nature",
    version=VERSION,
    url='',
    license='BSD',
    description='A MkDocs theme. A clone of the "greenish" Sphinx theme of the same name.',
    author='Waylan Limberg',
    author_email='waylan.limberg@icloud.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'nature = nature',
        ]
    },
    zip_safe=False
)