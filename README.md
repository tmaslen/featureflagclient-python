[pyenv](https://github.com/pyenv/pyenv) for managing the version of Python
[Python 3.6]()
[pipenv](https://docs.pipenv.org/) for managing dependencies and the Python env
[pytest]() for unit testing
[mypy](http://mypy-lang.org/) for static typing
[flake8](http://flake8.pycqa.org/en/latest/) for code linting

## Setup from scratch

### pyenv - python version manager

```
brew install pyenv
```

Add this to `.bash_profile`

```
eval "$(pyenv init -)"
```

reload terminal session.
 
### python 3.6.5

``` 
pyenv install 3.6.5
```

## Develop

```
cd [project directory]
pipenv install
pipenv shell
```