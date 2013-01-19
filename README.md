# Pyproj: The minimal Python project
![Python Logo](http://www.python.org/community/logos/python-powered-w-200x80.png)

![Travis Build Status](https://api.travis-ci.org/cabrera/pyproj.png?branch=master)

pyproj was born as an experiment. The problem to solve: what does a
Python project that supports...:

* tox
* pip-style installation
* py.test
* virtualenv
* Travis CI

...look like? Here it is, lean, mean, and keeping it as simple as possible, but no simpler.

## Guidelines for Newcomers

Starting a Python project is pretty easy. Python lends itself very
well to implementing short scripts, to experimenting, and to
learning.

However, when you want to put together a larger Python effort, there
are more steps to take. A Python project that you want to keep alive,
grow, and maintain needs a little more help. Some key features of such a project include:

* Easy to install
* Easy to test
* Easy to modify
* Easy to share

Python makes all of the above pretty easy, thanks to a rich ecosystem
of tools and a great community of developers. Towards that end, this
page covers the following very briefly:

* pip
* tox
* pytest
* travis-ci

### pip

pip is the Python package manager of choice, akin to:

* Ruby's gem
* Haskell's cabal
* Javascript/Node's npm

It's use is pretty straightforward:

```bash
pip install git+https://github.com/cabrera/pyproj
```

If a package is already registered in [PyPi](pypi.python.org), it's even easier:

```bash
pip install pyproj
```

It even supports installation from a local file system!

```bash
pip install .
```

All it takes is a setup.py being present in the project. See setup.py
for more details.

### pytest

[pytest](pytest.org/latest/) is a Python a tool to discover and run tests. Here's how to use it on this project:

```bash
py.test
== test session starts ==
platform linux -- Python 3.3.0 -- pytest-2.3.4
collected 4 items

test_pyproj.py ....

== 4 passed in 0.05 seconds ==
```

It uses some simple heuristics to identify tests. Some of these include:

* Runs any function starting with the name 'test_'
* Runs any class that inherits from the unittest.TestCase class

### Travis

[travis](http://travis-ci.org) is a continuous-integration engine available for use by all open-source projects. Setting up doesn't take much effort, and the pay offs are pretty sweet. Here's the process in 6 steps:

1. Sign in to travis-ci.org through GitHub OAuth
2. Activate the GitHub service hook
3. Add a .travis.yml file to your repository
4. Trigger your first build with a Git push

That's enough for getting started. There are more steps in the
[Travis CI Getting Started Guide](http://about.travis-ci.org/docs/user/getting-started/),
fun stuff like connecting databases and customizing the execution.

The .travis.yml file for this project looks like:

```
language: python
python:
  - 2.7
  - 3.2
script: python setup.py test
install:
  - pip install pytest
  - pip install .
```

## How to contribute

* Know of some additional, open-source module/project pyproj isn't taking advantage of?
* Feel like adding documentation or examples?
* Is something not idiomatic?

Send in a patch!

## Roadmap

* Sphinx docs
* Improved HISTORY.md
* PyPi integration
* Add more details about tox
* Get tox working
