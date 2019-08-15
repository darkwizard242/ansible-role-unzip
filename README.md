[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-unzip.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-unzip)

Ansible Role: unzip
=========

Role to install (_by default_) `unzip` package  or uninstall (_if  passed as var_)  on **Ubuntu** and **CentOS** systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
unzip_app: unzip
unzip_desired_state: present
```

Variable `unzip_app`: Defines the app to install i.e. **unzip**

Variable `unzip_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Dependencies
------------

None

Example Playbook
----------------

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

License
-------

[MIT](https://github.com/darkwizard242/ansible-role-unzip/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
