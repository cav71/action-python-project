import contextlib
import json
from unittest import mock

import pytest

from action_python_project import builder

REFS = [
    ("cav71/lektor-ng/.github/workflows/beta.yml@refs/heads/beta/0.0.0", ("beta", "0.0.0")),
    ("cav71/lektor-ng/.github/workflows/release.yml@refs/heads/release/0.0.0", ("release", "0.0.0")),
    ("cav71/lektor-ng/.github/workflows/main.yml@refs/heads/main", ("main", None)),
    ("cav71/lektor-ng/.github/workflows/tags.yml@refs/tags/v0.0.0", (None, None)),
]


def test_rget():
    data = {}
    assert None == builder.rget(data, "")
    assert None == builder.rget(data, "x.y")
    assert {"b": 1} == builder.rget({"a": {"b": 1}}, "a")
    assert 1 == builder.rget({"a": {"b": 1}}, "a.b")
    assert None == builder.rget({"a": {"b": 1}}, "x.y")


def test_parse_ref():
    for branch, expected in REFS:
        found = builder.parse_ref(branch.rpartition("@")[2], "main")
        assert expected == found

@pytest.mark.parametrize("modetxt", ["release", "post", "beta"])
def test_get_gdata_pyproject(loader, modetxt):
    pyproject = loader("pyproject", "toml")

    mode = builder.ReleaseMode[modetxt.upper()]
    gdata = builder.get_gdata(mode, pyproject)
    assert {
        "name": "lektor-ng",
        "sha": None,
        "version": "0.0.0",
        "mode": mode,
        "number": None,
        "branch": None,
    } == gdata.__dict__

    if mode == builder.ReleaseMode.RELEASE:
        assert "0.0.0" == gdata.version_string()
    elif mode == builder.ReleaseMode.POST:
        assert "0.0.0.post0" == gdata.version_string()
    else:
        assert "0.0.0b0" == gdata.version_string()


def test_get_gdata_git(loader):
    pyproject = loader("pyproject", "toml")

    git = mock.MagicMock()
    git.default.return_value = "origin/main"
    git.branch.return_value = "release/0.0.0"
    git.sha.return_value = "ABCDFE"


    return
    gitdump = loader("gitdump.release")


    pass


# def test_pypi_parse_releases(loader):
#     data = loader("pypi")
#     releases = builder.pypi_parse_releases("xxx", data)
#
#     assert not releases["posts"]
#     assert 43 == len(releases["versions"])
#     assert 43 == (
#         len(releases["releases"])
#         + sum(len(x) for x in releases["betas"].values())
#         + sum(len(x) for x in releases["posts"].values())
#     )
#     assert 43 == len(releases["category"])
#
#
# def test_parse_ref():
#     assert "release/0.0.0" == builder.parse_ref("refs/heads/release/0.0.0", "yyyy")
#     assert "release/0.0.0" == builder.parse_ref("release/0.0.0", "yyyy")
#     assert "beta/0.0.0" == builder.parse_ref("refs/heads/beta/0.0.0", "yyyy")
#     assert "beta/0.0.0" == builder.parse_ref("beta/0.0.0", "yyyy")
#
#
# def test_pypi_get_releases(datadir):
#     with mock.patch("builder.pypi_fetch_data") as mck:
#         mck.return_value = json.loads((datadir / "pypi.json").read_text())
#         releases = builder.pypi_parse_releases("xxx")
#         assert not releases["posts"]
#         assert 43 == len(releases["versions"])
#         assert 43 == (
#             len(releases["releases"])
#             + sum(len(x) for x in releases["betas"].values())
#             + sum(len(x) for x in releases["posts"].values())
#         )
#         assert 43 == len(releases["category"])
#
# @pytest.mark.parametrize("target", ["release"])#, "beta", "release"])
# def test_create_gitdump(branch, target):
#     #github = branch(f"github.{target}", "json")
#     git = mock.MagicMock()
#     git.default.return_value = "xxx"
#     git.branch.return_value = "yyy"
#     pyproject = {
#         "project": {
#             "name": "xyz",
#             "version": "0.0.0",
#         }
#     }
#
#     found = builder.make_gitdump(git, pyproject)
#     pass
#
#
# @pytest.mark.parametrize("mode", ["beta", "release", "post"])
# def _test_process_checkout(branch, mode):
#     breakpoint()
#     #     mck = stack.enter_context(mock.patch("tomllib.loads"))
#     #     mck.return_value = {
#     #         "project": {
#     #             "name": "xyz",
#     #             "version": "0.0.0",
#     #         }
#     #     }
#     #     mck = stack.enter_context(mock.patch("builder.pypi_fetch_data"))
#     #     mck.return_value = {
#     #         "releases": {
#     #         }
#     #     }
#     pyproject = {
#         "project": {
#             "name": "xyz",
#             "version": "0.0.0",
#         }
#     }
#     gitdump = branch(f"gitdump.{mode}", "json")
#     git = mock.MagicMock()
#     git.default.return_value = "xxx"
#     git.branch.return_value = "yyy"
#     expected = {
#         "beta": "0.0.0bNone",
#         "release": "0.0.0",
#         "post": "0.0.0.postNone",
#     }[mode]
#
#     gdata = builder.process_checkout(mode, pyproject, gitdump, git)
#     assert expected == gdata.version_string()
#     assert "89a35ec" == gdata.sha[:7]
#
#     git.sha.return_value = "abcdefg"
#     gdata = builder.process_checkout(mode, pyproject, None, git)
#     assert expected == gdata.version_string()
#     assert "abcdefg" == gdata.sha[:7]
