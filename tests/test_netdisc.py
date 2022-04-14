from netdisc import __version__
import pkg_resources


def test_version():
    assert __version__ == pkg_resources.require("netdisc")[0].version
