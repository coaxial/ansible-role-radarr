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

def test_radarr_dir(host):
    install_dir = host.dir('/opt/Radarr')

    assert install_dir.exists
    assert install_dir.is_directory
    assert install_dir.user == 'radarr'
    assert install_dir.group == 'media'
    assert install_dir.mode == '0755'

def test_radarr_service(host):
    s = host.service('radarr')

    assert s.is_enabled
    assert s.is_running

def test_radarr_http(host):
    ui = host.addr('127.0.0.1/radarr')

    assert ui.port(80).is_reachable

def test_firewall(host):
    r = host.iptables.rules()

    assert (
        '-A INPUT -p tcp -m tcp --dport 80 '
        '-m conntrack --ctstate NEW,ESTABLISHED'
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'INPUT')
    assert (
        '-A OUTPUT -p tcp --sport 80 -m conntrack --ctstate ESTABLISHED'
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'OUTPUT')

