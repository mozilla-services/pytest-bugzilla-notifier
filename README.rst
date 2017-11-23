pytest-bugzilla-notifier
===================================

A plugin that allows you to post test runs to BugZilla tickets


Installation
------------

You can install "pytest-bugzilla-notifier" via `pip`_ from `PyPI`_::

    $ pip install pytest-bugzilla-notifier


Usage
-----

To use this plugin you need to have a username and password for a Bugzilla
account. First, you need to copy bugzilla.ini-dist to bugzilla.ini and add in
the BugZilla API key you will be using to access Bugzilla. Then you can
use the plugin by running the following::

    $ pytest --bug=<bug ID> --config=./bugzilla.ini --bugzilla-url=<server> /path/to/tests

<bug ID>
The ID that Bugzilla assigned to the bug you wish to have the test
results sent to.

<server>
The full URL to the Bugzilla instance you wish to send test results to
(eg https://bugzilla.mozilla.com)


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
that the test suite passed before submitting a pull request.


License
-------

Distributed under the terms of the `Mozilla Public License 2.0`_ license, "pytest-bugzilla-notifier" is free and open source software.


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Mozilla Public License 2.0`: http://mozilla.org/MPL/2.0/
.. _`file an issue`: https://github.com/mozilla-services/pytest-bugzilla-notifier/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
