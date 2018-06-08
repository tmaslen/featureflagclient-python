import pytest

from Featureflagclient import Featureflagclient

def test_actual_http_request_with_override():

	f2c = Featureflagclient(
		"https://featureflag.tech/node/exampleflag.json",
		{
			"text": "overridden"
		}
	)

	assert f2c.get( "trueBoolean" ) == True
	assert f2c.get( "text" ) == "overridden"