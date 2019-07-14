Ansible Role: unzip
=========

Role to install (_by default_) `unzip` package  or uninstall (_if  passed as var_)  on **Ubuntu** systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
app: unzip
desired_state: present
```

Variable `app`: Defines the app to install i.e. **unzip**

Variable `desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **unzip** package) in ansible playbooks.

    - hosts: servers
      roles:
         - role: darkwizard242.unzip


For customizing behavior of role (i.e. installation of latest **unzip** package) in ansible playbooks.

    - hosts: servers
      roles:
         - role: darkwizard242.unzip
           vars:
             desired_state: latest
             
For customizing behavior of role (i.e. un-installation of **unzip** package) in ansible playbooks.

    - hosts: servers
      roles:
         - role: darkwizard242.unzip
           vars:
             desired_state: absent
         
         
License
-------

[MIT](https://github.com/darkwizard242/ansible-role-unzip/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).