import pytest
from mock import create_autospec
from pytest_bugzilla_notifier.plugin import BugzillaPlugin
from pytest_bugzilla_notifier.bugzilla_rest_client import BugzillaRESTClient

BUGZILLA_HOST = 'http://localhost'
BUGZILLA_BUG = 12345
BUGZILLA_TOKEN = 'testtoken'
BUGZILLA_COMMENT_ID = 13
BUGZILLA_API_KEY = 'bugzillaapikey'


@pytest.fixture
def rest_client():
    return create_autospec(BugzillaRESTClient)


@pytest.fixture
def api_details():
    return {
        'bugzilla_host': BUGZILLA_HOST,
        'bugzilla_api_key': BUGZILLA_API_KEY
    }


def test_pytest_configure(rest_client, api_details):
    with pytest.raises(AttributeError):
        bz_plugin = BugzillaPlugin(rest_client, api_details)
        bz_plugin.pytest_configure()


def test_post_results(rest_client, api_details):
    rest_client.bug_update.return_value = BUGZILLA_BUG
    test_results = (
        'test_one -> passed',
        'test_two -> failed',
        'test_three -> skipped'
    )
    bz_plugin = BugzillaPlugin(rest_client, api_details)
    result = bz_plugin.post_results(test_results, BUGZILLA_BUG)
    assert result == 12345


def test_create_new_bug(rest_client, api_details):
    rest_client.bug_create.return_value = 12345
    bug_data = {
        'product': 'QA test',
        'component': 'TestComponent',
        'summary': 'This is a summary of the bug',
        'version': ''
    }
    bz_plugin = BugzillaPlugin(rest_client, api_details)
    result = bz_plugin.post_bug(bug_data)
    assert result == 12345


def test_missing_default_create_bug_fields_detected(rest_client, api_details):
    msg = "Missing a default field (product, component, summary, version)"
    rest_client.bug_create.return_value = msg
    bz_plugin = BugzillaPlugin(rest_client, api_details)
    result = bz_plugin.post_bug({'foo': 1, 'bar': 2, 'product': 'test'})
    assert result == msg


def test_search_for_existing_bug(rest_client, api_details):
    search_response = {
        'faults': [],
        'bugs': [
            {'id': BUGZILLA_BUG}
        ]
    }
    rest_client.bug_search.return_value = search_response
    search_details = {
        'product': 'QA test',
        'component': 'TestComponent',
        'summary': 'This is a summary of the bug',
        'version': ''
    }
    bz_plugin = BugzillaPlugin(rest_client, api_details)
    result = bz_plugin.search_for_bug(search_details)
    assert result == search_response


def test_read_bug(rest_client, api_details):
    bug_details = {
        'faults': [],
        'bugs': [
            {'id': BUGZILLA_BUG}
        ]
    }
    rest_client.bug_read.return_value = bug_details
    bz_plugin = BugzillaPlugin(rest_client, api_details)
    result = bz_plugin.read_bug(BUGZILLA_BUG)
    assert result['bugs'][0]['id'] == BUGZILLA_BUG