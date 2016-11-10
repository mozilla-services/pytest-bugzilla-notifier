import configparser
import pytest

from .plugin import BugzillaPlugin
from .bugzilla_rest_client import BugzillaRESTClient


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        dest='env',
        help='Environment to post results to'
    )
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


@pytest.fixture
def env(request):
    request.config.getoption("--env")


def pytest_configure(config):
    env = config.getoption('env')

    if config.option.dest_bug and config.option.dest_bugzilla_url and config.option.dest_config:
        # try:
        cp = configparser.ConfigParser()
        cp.read(config.getoption('dest_config'))
        api_details = {
            'username': cp[env]['username'],
            'password': cp[env]['password'],
            'product': cp[env]['product'],
            'component': cp[env]['component'],
            'bug': config.getoption('dest_bug'),
            'bugzilla_host': config.getoption('dest_bugzilla_url'),
        }
        # except AttributeError:
        #    print("Could not find Bugzilla API credentials in bugzilla.cfg for ".format(env))
        #    exit(1)

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
