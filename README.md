featureflagclient
=================

Allows you to use feature flags in your code, works with any JSON feature flag service.

Features:

 * Extremely light-weight.
 * Feature flag service agnostic.

Created by [featureflag.tech](https://featureflag.tech).

## Get started

You can install this via pip from the package index as

```
pip install featureflagclient
```

If you have a JSON file in the cloud like this one:

[featureflag.tech/node/exampleflag.json](https://featureflag.tech/node/exampleflag.json)

You can access it like so

```
from featureflagclient.client import Featureflagclient

f2c = Featureflagclient("https://featureflag.tech/node/exampleflag.json")

if (f2c.get( "trueBoolean" )) {
	// do some python
}
```

A great way to use feature flags is to use the values from your flag source but override them in specific contexts. For example with a web application, you can have a feature disabled by default in your live production, but then override the value using a cookie or parameter in the request.

For example:

```
from featureflagclient.client import Featureflagclient

f2c = Featureflagclient(
	"https://featureflag.tech/node/exampleflag.json",
	{
		"falseBoolean": req.param("falseBooleanOverride") or None
	}
)

if (f2c.get( "trueBoolean" )) {
	// do some python
}
```

## Developing

### Setting up from scratch

Project uses the following Python libs:

 * Python 3.6
 * [pyenv](https://github.com/pyenv/pyenv) for managing the version of Python
 * [pipenv](https://docs.pipenv.org/) for managing dependencies and the Python env
 * [pytest](https://docs.pytest.org/en/latest/) for unit testing
 * [mypy](http://mypy-lang.org/) for static typing (not yet true)
 * [flake8](http://flake8.pycqa.org/en/latest/) for code linting (not yet true)

*pyenv - python version manager*

```
brew install pyenv
```

Add this to `.bash_profile`

```
eval "$(pyenv init -)"
```

reload terminal session.
 
*python 3.6.5*

``` 
pyenv install 3.6.5
```

*Setup env with dependencies*

```
cd [repo directory]
pipenv install
pipenv shell
```

*Run the tests*

```
pytest -v
```

### Release new version

1) Bump the version number in `setup.py`

2) Delete all the contents of the `dist` dir

3) Create distribution files:

```
python setup.py sdist bdist_wheel
```

4) Push to pypi:

```
twine upload dist/*
```

5) Check the deployment at:

```
https://pypi.org/manage/project/featureflagclient/releases/
```