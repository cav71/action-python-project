## builder tool

Get a version string for a package and build the wheel.

Examples:

Fetch from pyproject.toml the version and adds a N.M.ObXX number.
```
  uv tool run --from git+https://github.com/cav71/action-python-project builder \
    beta README.md src/lektor_ng/__init__.py    
```

Config:
pyproject.toml
```
[tool.builder]
template = ampersand | jinja2 (default ampersand)
files = [
  README.md,
  src/lektor_ng/__init__.py
]
```


## TODO

Things left to do:
- fix mypy issues
- use jinja2 file processing

