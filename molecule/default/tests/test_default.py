import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'unzip'
PACKAGE_BINARY = '/usr/bin/unzip'


def test_unzip_package_installed(host):
    """
    Tests if unzip is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_unzip_binary_exists(host):
    """
    Tests if unzip binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_unzip_binary_file(host):
    """
    Tests if unzip binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_unzip_binary_which(host):
    """
    Tests the output to confirm unzip's binary location.
    """
    assert host.check_output('which unzip') == PACKAGE_BINARY
