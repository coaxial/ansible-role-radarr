import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    u = host.user('radarr')

    assert u.exists
    assert 'radarr' in u.groups
    assert 'media' in u.groups
    assert u.password == '!'
    assert u.shell == '/usr/bin/env nologin'


def test_radarr_install_dir(host):
    d = host.file('/opt/Radarr')

    assert d.exists
    assert d.is_directory
    assert d.user == 'radarr'
    assert d.group == 'radarr'
    assert d.mode == 0o755


def test_radarr_config_dir(host):
    d = host.file('/var/lib/radarr')

    assert d.exists
    assert d.is_directory
    assert d.user == 'radarr'
    assert d.group == 'media'
    assert d.mode == 0o755


def test_radarr_service(host):
    s = host.service('radarr')

    assert s.is_enabled
    assert s.is_running


def test_radarr_http(host):
    html = host.run('curl http://localhost/radarr').stdout

    assert 'Radarr' in html


def test_firewall(host):
    i = host.iptables

    assert (
        '-A INPUT -p tcp -m tcp --dport 80 '
        '-m conntrack --ctstate NEW,ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'INPUT')
    assert (
        '-A OUTPUT -p tcp -m tcp --sport 80 '
        '-m conntrack --ctstate ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'OUTPUT')
