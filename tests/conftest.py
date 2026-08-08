import json
import tomllib
from pathlib import Path

import pytest


@pytest.fixture()
def datadir():
    return Path(__file__).parent / "data"


@pytest.fixture(scope="function")
def loader(datadir):
    def _load(name, typ="json"):
        txt = (datadir / f"{name}.{typ}").read_text()
        if typ == "json":
            return json.loads(txt)
        elif typ == "env":
            return {line.partition("=")[0]: line.partition("=")[2] for line in txt.splitlines() if line.strip()}
        elif typ == "toml":
            return tomllib.loads(txt)
        else:
            raise RuntimeError(f"un-handled {typ=}")

    yield _load
