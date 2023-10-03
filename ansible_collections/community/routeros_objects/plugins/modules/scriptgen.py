#!/usr/bin/python

DOCUMENTATION = '''
---
module: scriptgen
short_description: Generate Mikrotik RouterOS script
'''

EXAMPLES = '''
- name: Create a github Repo
  scriptgen:
    commands: | 
        asdf1
        asdf2
  register: result
'''

# RETURN = '''

# '''

import json
from ansible.module_utils.basic import *
import requests

def main():
    fields = {
        "commands": { "required": True, "type": "str" },
    }
    
    module = AnsibleModule(argument_spec=fields)

    commands = module.params["commands"]
    result = {
        "foo": "bar",
        "cmds": commands,
    }

    module.exit_json(changed=True, meta=result)


if __name__ == '__main__':
    main()

#   msg:
#   - changed: true
#     failed: false
#     meta:
#       cmds: |-
#         test1
#         test2
#       foo: bar