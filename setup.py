"""
Setup the package.
"""
from setuptools import find_packages, setup

with open('README.md') as read_me:
    long_description = read_me.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    version='0.2.0',
    name='eos-name-generator',
    description='Python package for generation random name which suits `EOS` name conversations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Alladin9393/name-generator',
    license='MIT',
    author='Alladin9393',
    author_email='ember.toon@protonmail.com',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'eos-name-generator = cli.entrypoint:cli',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
