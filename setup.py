#!/usr/bin/env python3
from setuptools import find_packages, setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='textproof',
    version='1.0.0',
    description='Perform command-line spelling and grammar check on text.',
    long_description_content_type='text/markdown',

    author='Jason C. McDonald',
    author_email='codemouse92@outlook.com',
    url='https://github.com/codemouse92/textproof',
    project_urls={
        'Bug Reports': 'https://github.com/codemouse92/textproof/issues',
        'Funding': 'https://github.com/sponsors/CodeMouse92',
        'Source': 'https://github.com/codemouse92/textproof',
    },
    keywords='proof, spelling, grammar, utility',

    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=('tests')),
    include_package_data=True,
    python_requires='>=3.6, <4',
    install_requires=['requests', 'click'],
    extras_require={
        'test': ['pytest', 'coverage', 'tox'],
    },

    entry_points={
        'console_scripts': [
            'textproof=textproof.__main__:main'
        ]
    }
)
