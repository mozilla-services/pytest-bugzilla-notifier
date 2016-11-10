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
        self.username = api_details['username']
        self.password = api_details['password']
        self.bug = api_details['bug']
        self.bugzilla_host = api_details['bugzilla_host']
        self.token = self.get_token(self.bugzilla_host)

    def _get_json_update(self, comment, bug_id):
        """Returns bugzilla JSON as string to PUT to REST API."""

        data = {
            'ids': [bug_id],
            'comment': comment
        }
        return data

    def get_token(self, host):
        """Fetch and return bugzilla token as string."""

        params = {
            'login': self.username,
            'password': self.password
        }
        url = '{0}/rest/login'.format(host)
        req = requests.get(url, params=params)
        decoded = json.loads(req.text)

        try:
            if 'token' not in decoded:
                raise InvalidCredentials
        except InvalidCredentials:
            err_msg = '{0}\n{1}\n\n'.format(
                decoded['message'],
                decoded['documentation']
            )

            sys.exit(err_msg)
        else:
            return decoded['token']

    def bug_update(self, comment, bug_id=''):
        """Update bugzilla bug with new comment

        Returns:
            json string to POST to REST API
        """
        url = '{0}/rest/bug/{1}/comment?token={2}'.format(
            self.bugzilla_host, bug_id, self.token)
        data = self._get_json_update(comment, bug_id)
        req = requests.post(url, data=json.dumps(data), headers=HEADERS)
        response = req.json()

        if 'id' in response:
            return response['id']

        err_msg = "\nUnable to post results to ticket {0}.".format(bug_id)
        err_msg += " Please check that the bug number is correct"
        sys.exit(err_msg)
