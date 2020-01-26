import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_unzip_package_installed(host):
    assert host.package("unzip").is_installed


def test_unzip_binary_exists(host):
    assert host.file('/usr/bin/unzip').exists


def test_unzip_binary_file(host):
    assert host.file('/usr/bin/unzip').is_file


def test_unzip_binary_which(host):
    assert host.check_output('which unzip') == '/usr/bin/unzip'
