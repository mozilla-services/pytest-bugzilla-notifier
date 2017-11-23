import pytest
from mock import create_autospec
from pytest_bugzilla_notifier.plugin import BugzillaPlugin
from pytest_bugzilla_notifier.bugzilla_rest_client import BugzillaRESTClient

BUGZILLA_HOST = 'http://localhost'
BUGZILLA_BUG = 12345
BUGZILLA_TOKEN = 'testtoken'
BUGZILLA_COMMENT_ID = 13
BUGZILLA_API_KEY = 'bugzillaapikey'

PYTEST_FILE = """
    def test_func():
        pass
"""


@pytest.fixture
def rest_client():
    return create_autospec(BugzillaRESTClient)


@pytest.fixture
def pytest_test_items(testdir):
    testdir.makepyfile(PYTEST_FILE)
    return [testdir.getitem(PYTEST_FILE)]


def test_pytest_configure(rest_client):
    api_details = {
        'username': 'test',
        'password': 'test',
        'product': 'Test Product',
        'component': 'Test Component',
        'bug': BUGZILLA_BUG,
        'bugzilla_host': BUGZILLA_HOST,
        'bugzilla_api_key': BUGZILLA_API_KEY,
    }
    with pytest.raises(AttributeError):
        bz_plugin = BugzillaPlugin(rest_client, api_details)
        bz_plugin.pytest_configure()


def test_post_results(rest_client):
    rest_client.bug_update.return_value = 12345
    api_details = {
        'username': 'test',
        'password': 'test',
        'product': 'Test Product',
        'component': 'Test Component',
        'bug': BUGZILLA_BUG,
        'bugzilla_host': BUGZILLA_HOST,
        'bugzilla_api_key': BUGZILLA_API_KEY,
    }
    test_results = (
        'test_one -> passed',
        'test_two -> failed',
        'test_three -> skipped'
    )
    bz_plugin = BugzillaPlugin(rest_client, api_details)
    result = bz_plugin.post_results(test_results)
    assert result == 12345
