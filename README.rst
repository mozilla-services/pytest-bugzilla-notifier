pytest-bugzilla-notifier
===================================

This plugin currently has the following functionality:

* posts the results of test runs to be added to existing BugZilla tickets
* create new tickets as part of a pytest test



Installation
------------

You can install "pytest-bugzilla-notifier" via `pip`_ from `PyPI`_::

    $ pip install pytest-bugzilla-notifier

Pre-requisites
--------------

To use this plugin you need to have a username and password for a Bugzilla
account. First, you need to copy bugzilla.ini-dist to bugzilla.ini and add in
the BugZilla API key you will be using to access Bugzilla.

Reporting test runs
-------------------

You can use the plugin to update a ticket with the results by using the following command::

    $ pytest --bug=<bug ID> --config=./bugzilla.ini --bugzilla-url=<server> /path/to/tests

<bug ID>
The ID that Bugzilla assigned to the bug you wish to have the test
results sent to.

<server>
The full URL to the Bugzilla instance you wish to send test results to
(eg https://bugzilla.mozilla.com)


Creating new tickets
--------------------

To create a new ticket in BugZilla, you need to import the library using::

    from pytest_bugzilla_notifier.bugzilla_rest_client import BugzillaRESTClient

 and then you can create bugs using code similar to this::

    api_details = {
        'bugzilla_host': '<bugzilla host you are using>',
        'bugzilla_api_key': '<bugzilla API key>'
    }
    rest_client = BugzillaRESTClient(api_details)
    bug_data = {
        'product': 'Firefox',
        'component': 'Developer Tools',
        'summary': 'Test Bug',
        'version': 'unspecified'
    }
    bug_id = rest_client.bug_create(bug_data)

If everything worked as expected, `bug_id`_ will contain the ID BugZilla has assigned to your ticket.

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
