
# Evennia installation

The latest and more detailed installation instructions can be found
[here](https://github.com/evennia/evennia/wiki/Getting-Started). 

## Installing Python

First install [Python](https://www.python.org/). Linux users should
have it in their repositories, Windows/Mac users can get it from the
Python homepage. You need the 2.7.x version (Python 3 is not yet
supported). Windows users, make sure to select the option to make
Python available in your path - this is so you can call it everywhere
as `python`. Python 2.7.9 and later also includes the
[pip](https://pypi.python.org/pypi/pip/) installer out of the box,
otherwise install this separately (in linux it's usually found as the
`python-pip` package).

## Evennia package install 

Stand at the root of your new `evennia` directory and run

```
pip install -e .
```

(note the period "." at the end, this tells pip to install from the
current directory). This will install Evennia and all its dependencies
(into your virtualenv if you are using that) and make the `evennia`
command available on the command line. You can find Evennia's
dependencies in `evennia/requirements.txt`. 
