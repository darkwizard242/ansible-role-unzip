import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_unzip(host):
    unzipfile = host.file('/usr/bin/unzip')
    unzippackage = host.package("unzip")

    assert unzipfile.exists
    assert unzipfile.user == 'root'
    assert unzipfile.group == 'root'
    assert unzipfile.mode == 0o755
    assert unzippackage.is_installed
