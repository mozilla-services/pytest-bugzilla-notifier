import pytest

from configobj import ConfigObj
from .plugin import BugzillaPlugin
from .bugzilla_rest_client import BugzillaRESTClient


def pytest_addoption(parser):
    parser.addoption(
        '--config',
        dest='dest_config',
        help='Path to bugzilla.cfg'
    )
    parser.addoption(
        '--bug',
        action='store',
        dest='dest_bug',
        help='Bugzilla bug ID'
    )
    parser.addoption(
        '--bugzilla-url',
        action='store',
        dest='dest_bugzilla_url',
        help='URL of Bugzilla instance you are sending results to',
    )


def pytest_configure(config):
    if config.option.dest_bug and config.option.dest_bugzilla_url and config.option.dest_config:
        try:
            co = ConfigObj(config.getoption('dest_config'))
            api_details = {
                'bugzilla_api_key': co['bugzilla_api_key'],
                'bug': config.getoption('dest_bug'),
                'bugzilla_host': config.getoption('dest_bugzilla_url'),
            }
        except AttributeError:
            print("Could not find Bugzilla API credentials in bugzilla.ini")
            exit(1)

        client = BugzillaRESTClient(api_details)
        config._bugzillaPlugin = BugzillaPlugin(
            client,
            api_details,
        )
        config.pluginmanager.register(config._bugzillaPlugin)


@pytest.fixture
def bug(request):
    return request.config.option.dest_bug


@pytest.fixture
def bugzilla_url(request):
    return request.config.option.dest_bugzilla_url
