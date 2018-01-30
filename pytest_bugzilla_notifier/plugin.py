import pytest


class BugzillaPlugin(object):
    def __init__(self, client, api_details):
        self.client = client
        self.api_details = api_details
        self.bugzilla_host = api_details['bugzilla_host']
        self.results = list()
        self.bugzilla_api_key = api_details['bugzilla_api_key']

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        rep = outcome.get_result()
        if rep.when == 'call':
            '''
            The test result returns a tuple that contains the path of the
            test, the line number an assertion was on, and the 'domain' of
            the test, which is the name of the test method the assertion was
            part of
            '''
            location = rep.location
            test_name = location[2]
            self.results.append("{0} -> {1}".format(test_name, rep.outcome))

    def pytest_sessionfinish(self):
        # Build payload to send
        test_results = "Test output generated by pytest-bugzilla-notifier\n\n"
        for result in self.results:
            test_results += "{}\n".format(result)
        return self.post_results(test_results)

    def post_results(self, test_results, bug_id):
        return self.client.bug_update(test_results, bug_id)

    def post_bug(self, bug_data):
        return self.client.bug_create(bug_data)

    def read_bug(self, bug_id):
        return self.client.bug_read(bug_id)

    def search_for_bug(self, search_details):
        return self.client.bug_search(search_details)
