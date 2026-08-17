## builder tool


### Info

Extract system info and checks:
```
uv tool run --from git+https://github.com/cav71/action-python-project info
```

You can pass extra "checkers", see [example.py](example.py).


### Building
Create a release:
```
  uv tool run --from git+https://github.com/cav71/action-python-project builder \
    beta README.md src/lektor_ng/__init__.py    
```
Fetch from pyproject.toml the version and adds a N.M.ObXX number.

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
