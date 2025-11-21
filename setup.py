"""
Setup script for Game Theory Learning Platform.
"""

from setuptools import setup, find_packages
import os

# Read README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='gametheory-learning',
    version='1.0.0',
    author='Game Theory Learning Platform Contributors',
    author_email='',
    description='Interactive learning platform for game theory through hands-on Python exercises',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/GeoffreyWang1117/GameTheory',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'gametheory=gametheory.cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        'gametheory': ['exercises/**/*.py', 'exercises/info.json'],
    },
    keywords='game-theory education learning economics mathematics',
    project_urls={
        'Bug Reports': 'https://github.com/GeoffreyWang1117/GameTheory/issues',
        'Source': 'https://github.com/GeoffreyWang1117/GameTheory',
        'Documentation': 'https://github.com/GeoffreyWang1117/GameTheory/blob/main/README.md',
    },
)
