---
title: 'Weather Report'
place: "Paris"
wind: 33
thanks: 'true'
...

## {{title}}

* The temperature in {{ place.upper() }}
  was {{temperature|default('0')}} degrees.
* The humidity was {{humidity|float * 100 }} %
* The wind speed was {{wind |default(0)}} km/h

## It works in code blocks too !


```bash
echo 'hello {{place}} !'
```

## It can be disabled on certain codeblocks

``` { .yaml pandoc-jinja-disable=true }
---
- name: "Ansible Playbook"
   hosts: "{{ inventory_hosts }}"
   gather_facts: yes
...
```

## Basic conditionals

{{ 'Thank you' if thanks|bool else 'Goodbye !' }}


