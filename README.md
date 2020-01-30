[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-unzip.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-unzip) ![Ansible Role](https://img.shields.io/ansible/role/42038?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/42038?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/42038?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-unzip&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-unzip) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-unzip?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-unzip?color=orange&style=flat-square)

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

Variable            | Value (default) | Description
------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
unzip_app           | unzip           | Defines the app to install i.e. **unzip**
unzip_desired_state | present         | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **unzip** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.unzip
```

For customizing behavior of role (i.e. installation of latest **unzip** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.unzip
      vars:
        unzip_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **unzip** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.unzip
      vars:
        unzip_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-unzip/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
