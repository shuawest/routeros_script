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
#import requests

def get_argument_spec():
    argument_spec = dict(
        commands=dict(type='list', elements='dict', options={
                'desc': dict(type='str', required=True),
                'path': dict(type='str', required=True),
                'state': dict(type='str', choices=['present','absent'], default='present'),
                'values': dict(type='list', elements='dict', options={
                    'attr': dict(type='str', required=True),
                    'value': dict(type='str', required=True),
                }),
                'match': dict(type='list', elements='dict', options={
                    'attr': dict(type='str', required=True),
                    'value': dict(type='str', required=True),
                }),
                # consider merging values with match
                #  use property to match, set, or both
            },
        )
    )
    return argument_spec

def main():
    argument_spec = get_argument_spec()
    #module = AnsibleModule(argument_spec=argument_spec)
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    commands = module.params["commands"]
    result = {
        "input": commands,
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