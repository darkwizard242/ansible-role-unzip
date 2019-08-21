import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


UNZIP_BINARY_PATH = '/usr/bin/unzip'
PACKAGE = 'unzip'


def test_unzip_package_installed(host):
    host.package("PACKAGE").is_installed


def test_unzip_binary_exists(host):
    host.file('UNZIP_BINARY_PATH').exists


def test_unzip_binary_file(host):
    host.file('UNZIP_BINARY_PATH').is_file


def test_unzip_binary_whereis(host):
    host.check_output('whereis unzip') == UNZIP_BINARY_PATH