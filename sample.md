---
title: 'Weather Report'
place:
  city: "Paris"
  country: "France"
wind: 33
thanks: 'true'
...

## {{title}}

* The temperature in {{ place.city | upper }}
  was {{temperature|default('0')}} degrees.
* The humidity was {{humidity|float * 100 }} %
* The wind speed was {{wind |default(0)}} km/h

## It works in code blocks too !


```bash
echo 'hello {{ place.country }} !'
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

{{ 'Thank you' if thanks|bool }} Paris


