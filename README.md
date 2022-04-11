# Radarr role

[![CI](https://github.com/coaxial/ansible-role-radarr/actions/workflows/ci.yml/badge.svg)](https://github.com/coaxial/ansible-role-radarr/actions/workflows/ci.yml)

Galaxy: https://galaxy.ansible.com/coaxial/radarr

## Instructions

This role will install Radarr and (optionally) install and configure NGINX to
serve the UI at `<server address>/radarr`.

## Variables and their defaults

| variable name               | default value     | description                                                                             |
| --------------------------- | ----------------- | --------------------------------------------------------------------------------------- |
| radarr\_\_config_directory  | `/var/lib/radarr` | Radarr configuration files directory                                                    |
| radarr\_\_install_directory | `/opt`            | Radarr installation directory (will use `<dir>/Radarr`)                                 |
| radarr\_\_username          | `radarr`          | Username under which to run Radarr                                                      |
| radarr\_\_password          | `!` (disabled)    | Radarr user's password                                                                  |
| radarr\_\_group             | `media`           | Radarr user's group                                                                     |
| radarr\_\_version           | `latest` (stable) | See https://github.com/Radarr/Radarr/releases                                           |
| radarr\_\_use_nginx         | `yes`             | Whether to install and configure nginx (`no` if you're installing/managing it yourself) |
