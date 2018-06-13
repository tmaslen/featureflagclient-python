from _pytest.monkeypatch import MonkeyPatch
import pytest
import urllib.request

from featureflagclient.client import Featureflagclient
from featureflagclient.client import FeatureflagclientErrorMalformedJson
from featureflagclient.client import FeatureflagclientError404

monkeypatch = MonkeyPatch()


def test_constructor():

    def MockUrlOpen(url):
        class o:
            def read():
                return """
                {
                    "foo": true,
                    "bar": true
                }
                """
        return o

    monkeypatch.setattr(urllib.request, 'urlopen', MockUrlOpen)

    f2c = Featureflagclient(
        "https://featureflag.tech/node/exampleflag3.json",
        {
            "foo": False
        }
    )

    assert f2c.get("foo") is False
    assert f2c.get("bar") is True

    monkeypatch.undo()


def test_constructor_throws_404_error():
    with pytest.raises(FeatureflagclientError404):
        def MockUrlOpen(url):
            class o:
                def read():
                    raise urllib.error.HTTPError(url="featureflag.tech", code=404, msg='Not Found', hdrs=None, fp=None)
            return o

        monkeypatch.setattr(urllib.request, 'urlopen', MockUrlOpen)

        Featureflagclient("https://featureflag.tech/node/exampleflag.json")

        monkeypatch.undo()


def test_constructor_throws_malformed_json_error():
    with pytest.raises(FeatureflagclientErrorMalformedJson):

        def MockUrlOpen(url):
            class o:
                def read():
                    return """
                    {
                        "foo": true
                    """
            return o

        monkeypatch.setattr(urllib.request, 'urlopen', MockUrlOpen)

        Featureflagclient("https://featureflag.tech/node/exampleflag.json")

        monkeypatch.undo()


def test_get_method():
    f2c = Featureflagclient(None, {
        "trueBoolean": True,
        "falseBoolean": False,
        "number": 33,
        "array": [1, 2],
        "object": {"foo": "bar"},
        "text": "laserwolf"
    })

    assert f2c.get("notDefined") is None
    assert f2c.get("trueBoolean") is True
    assert f2c.get("falseBoolean") is False
    assert f2c.get("number") == 33
    assert f2c.get("array") == [1, 2]
    assert f2c.get("object") == {"foo": "bar"}
    assert f2c.get("text") == "laserwolf"
