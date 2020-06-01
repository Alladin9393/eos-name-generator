## EOS Name Generator 

[![Build Status](https://travis-ci.com/Alladin9393/eos-name-generator.svg?branch=develop)](https://travis-ci.com/Alladin9393/eos-name-generator)
[![CodeFactor](https://www.codefactor.io/repository/github/alladin9393/eos-name-generator/badge)](https://www.codefactor.io/repository/github/alladin9393/eos-name-generator)
[![codecov](https://codecov.io/gh/Alladin9393/eos-name-generator/branch/develop/graph/badge.svg)](https://codecov.io/gh/Alladin9393/eos-name-generator)

`EOS Name Generator` - is a python package for generating names according to [EOS name rules](#eos-name-rules).

This includes 3 ways to generate a name:

    * Random Generator
    * Recurrent Neural Network Generator
    * Markov Chain Generator
    
  * [Getting started](#getting-started)
    * [Requirements](#getting-started-requirements)
      * [Ubuntu 16.04 & 18.04](#ubuntu-1604--1804)
      * [MacOS](#macos)
    * [Installation](#installation)
  * [Algorithm description](#algorithm-description)
    * [Random Generator](#random-generator)
    * [Recurrent Neural Network Generator](#recurrent-neural-network-generator)
    * [Markov Chain Generator](#markov-chain-generator)
    * [EOS Name Rules](#eos-name-rules)
  * [Usage](#usage)
    * [Service](#service)
    * [Random Generator](#random-generator-usage)
    * [Recurrent Neural Network Generator](#recurrent-neural-network-generator-usage)
    * [Markov Chain Generator](#markov-chain-generator-usage)
  * [Development](#development)
  * [Production](#production)
  * [Contributing](#contributing)
    * [Request pull request's review](#request-pull-requests-review)

## Getting started

<h3 id="getting-started-requirements">Requirements</h4>

#### Ubuntu 16.04 & 18.04

If you have 16.04 version, install system requirements with the following terminal commands:

```bash
$ sudo apt update && sudo apt install -y software-properties-common build-essential
```

#### MacOS

Install Python 3.7 (also, we support 3.6):
```bash
$ brew install python3
```

## Installation

Install the package from the [PyPi](https://pypi.org/project/eos-name-generator) through pip:

```bash
$ pip3 install eos-name-generator
```

## Algorithm description

#### Random Generator

The algorithm selects a base word from a pre-prepared dictionary, after which an additional word of the appropriate 
length is selected `ADDITIONAL_WORD_LEN = EOS_NAME_LEN - BASE_WORD_LEN` if there is no such word, then the additional 
word is random numbers.

The probability that an additional word will be numbers can be set by the parameter `numbers_probabilities`.

#### Recurrent Neural Network Generator

#### Markov Chain Generator

#### EOS Name Rules

* Can only contain the characters `.abcdefghijklmnopqrstuvwxyz12345`. `a-z` (lowercase), `1-5` and `.` (period)
* Must start with a letter
* Must be `12` characters

## Usage

#### Service

Get the version of the package — `eos-name-generator --version`:

```bash
$ eos-name-generator --version
```

#### Random Generator
<a name="random-generator-usage"></a>

Generate random name:

```python
from eos_name_generator import RandomNameGenerator

if __name__ == '__main__':
    generator = RandomNameGenerator()
    name = generator.generate()
    print(name)    
```

Generate list of random names:

```python
from eos_name_generator import RandomNameGenerator

if __name__ == '__main__':
    generator = RandomNameGenerator()
    names = generator.generate_list(num=1000)
    
    for name in names:
        print(name)
```

#### Recurrent Neural Network Generator
<a name="recurrent-neural-network-generator-usage"></a>

#### Markov Chain Generator
<a name="markov-chain-generator-usage"></a>

## Development

Clone the project and move to project folder:

```bash
$ git clone https://github.com/Alladin9393/eos-name-generator.git && cd eos-name-generator
```

Create virtualenv and install requirements:

```bash
$ virtualenv venv -p python3 && source venv/bin/activate
$ pip3 install -r requirements.txt -r requirements-dev.txt
```

To run tests use:

```bash
$ coverage run -m pytest -vv tests
```

When you have developed new functionality, check it with the following command. This command creates the Python 
package from source code instead of installing it from the PyPi:

```bash
$ pip3 uninstall -y eos_name_generator && rm -rf dist/ eos_name_generator.egg-info && \
      python3 setup.py sdist && pip3 install dist/*.tar.gz
```
## Production

To build the package and upload it to [PypI](https://pypi.org/) to be accessible through 
[pip](https://github.com/pypa/pip), use the following commands. [Twine](https://twine.readthedocs.io/en/latest/) 
requires the username and password of the account package is going to be uploaded to.

```bash
$ python3 setup.py sdist
$ twine upload dist/*
username: alladin9393
password: ******
```

## Contributing

#### Request pull request's review

If you want to your pull request to be review, ensure you:

If you want to your pull request to be review, ensure you:
1. [Branch isn't out-of-date with the base branch](https://habrastorage.org/webt/ux/gi/wm/uxgiwmnft08fubvjfd6d-8pw2wq.png).
2. [Have written the description of the pull request and have added at least 2 reviewers](https://camo.githubusercontent.com/55c309334a8b61a4848a6ef25f9b0fb3751ae5e9/68747470733a2f2f686162726173746f726167652e6f72672f776562742f74312f70792f63752f7431707963753162786a736c796f6a6c707935306d7862357969652e706e67).
3. [Continuous integration has been passed](https://habrastorage.org/webt/oz/fl/-n/ozfl-nl-jynrh7ofz8yuz9_gapy.png).
