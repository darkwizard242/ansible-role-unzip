[![build-test](https://github.com/darkwizard242/ansible-role-unzip/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-unzip/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-unzip/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-unzip/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/42038?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/42038?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/42038?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-unzip&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-unzip) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-unzip&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-unzip) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-unzip&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-unzip) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-unzip&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-unzip) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-unzip?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-unzip?color=orange&style=flat-square)

# Ansible Role: unzip

Role to install (_by default_) `unzip` package or uninstall (_if passed as var_) on **Ubuntu** and **CentOS** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
unzip_app: unzip
unzip_desired_state: present
```

### Variables table:

Variable            | Description
------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
unzip_app           | Defines the app to install i.e. **unzip**
unzip_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **unzip** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.unzip
```

For customizing behavior of role (i.e. installation of latest **unzip** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.unzip
  vars:
    unzip_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **unzip** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.unzip
  vars:
    unzip_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-unzip/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
