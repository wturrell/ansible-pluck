Ansible Pluck Filter
====================

This borrows heavily from [this Ansible custom Jinja2 filters blog post](https://opensolitude.com/2016/05/21/ansible-jinja2-filter-plugins.html) by Jordan Bach from May 2016.

You can use this filter to easily extract a single key from a dictionary.

      - { name: "web", cluster: "gamma", url: 'http://www.example.com' }
      - { name: "worker", cluster: "alpha" }
      - { name: "relay", cluster: "omega" }

Usage
-----

    debug:
      var: "{{ your_dictionary | pluck('name') }}"

I've modified the filter so that it can cope with keys that are missing from some entries.  For example, in the above 
dictionary, if you pluck 'url' you will get a list with a single item.

Returns
-------

A list. (Run the test playbook to see some debug output.)

Installation:
-------------
- Copy `pluck.py` to your ansible/filter_plugins directory
  (if directory does not exist, create it)
- Run the following playbook to test it works: 

`ansible-playbook pluck-test.yml`

Tested with:
- Ansible 2.5.0
- Python 2.7.14

Alternatives built-in to Ansible:
------------------------

     your_dictionary | map(attribute='name') | list
    
In this case, where a key doesn't exist in all records, the output will look like this:

    "urls": "[u'http://example.com', Undefined, Undefined]", 

[Jinja Documentation](http://jinja.pocoo.org/docs/dev/templates/#map)
