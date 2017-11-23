"""This module enables CRUD operations with Bugzilla 5.1 REST API

.. _Bugzilla REST API Docs:
   https://wiki.mozilla.org/Bugzilla:REST_API
   http://bugzilla.readthedocs.org/en/latest/api/index.html
"""

import sys
import json
import requests

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


class InvalidCredentials(Exception):
    pass


class BugzillaRESTClient():
    """"Used for CRUD operations against Bugzilla REST API"""

    def __init__(self, api_details):
        self.bugzilla_api_key = api_details['bugzilla_api_key']
        self.bug = api_details['bug']
        self.bugzilla_host = api_details['bugzilla_host']

    def _get_json_update(self, comment, bug_id):
        """Returns bugzilla JSON as string to PUT to REST API."""

        data = {
            'ids': [bug_id],
            'comment': comment,
            'Bugzilla_api_key': self.bugzilla_api_key
        }
        return data

    def bug_update(self, comment, bug_id=''):
        """Update bugzilla bug with new comment

        Returns:
            json string to POST to REST API
        """
        url = '{0}/rest/bug/{1}/comment'.format(self.bugzilla_host, bug_id)
        data = self._get_json_update(comment, bug_id)
        req = requests.post(url, data=json.dumps(data), headers=HEADERS)
        response = req.json()

        if 'id' in response:
            return response['id']

        err_msg = "\nUnable to post results to ticket {0}.".format(bug_id)
        err_msg += " Please check that the bug number is correct"
        sys.exit(err_msg)
