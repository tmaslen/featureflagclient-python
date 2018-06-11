featureflagclient
=================

Allows you to use feature flags in your code, works with any JSON
feature flag service.

Features:

-  Extremely light-weight.
-  Feature flag service agnostic.

Created by `featureflag.tech`_.

Get started
-----------

You can install this via pip from the package index as

::

   pip install featureflagclient

If you have a JSON file in the cloud like this one:

`featureflag.tech/node/exampleflag.json`_

You can access it like so

.. code-block:: python

   from featureflagclient.client import Featureflagclient

   f2c = Featureflagclient("https://featureflag.tech/node/exampleflag.json")

   if (f2c.get( "trueBoolean" )) {
       // do some python
   }

A great way to use feature flags is to use the values from your flag
source but override them in specific contexts. For example with a web
application, you can have a feature disabled by default in your live
production, but then override the value using a cookie or parameter in
the request.

For example:

.. code-block:: python

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