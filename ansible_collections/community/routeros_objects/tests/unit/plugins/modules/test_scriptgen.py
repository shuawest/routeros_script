# Copyright (c) 2016 Red Hat Inc.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import json

from ansible_collections.community.routeros_objects.tests.unit.compat.mock import patch
# from ansible_collections.community.routeros_objects.plugins.modules import command
from ansible_collections.community.routeros_objects.tests.unit.plugins.modules.utils import set_module_args
from .routeros_objects_module import TestRouterosObjectsModule, load_fixture


from ansible_collections.community.routeros_objects.plugins.modules import scriptgen
# import json
import unittest
import logging
import sys

class TestRouterosScriptgenModule(TestRouterosObjectsModule):

    module = scriptgen

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        super(TestRouterosScriptgenModule, self).setUp()
        self.mock_run_commands = patch('ansible_collections.community.routeros_objects.plugins.modules.scriptgen')
        self.run_commands = self.mock_run_commands.start()

    def tearDown(self):
        super(TestRouterosScriptgenModule, self).tearDown()
        self.mock_run_commands.stop()

    def test_scriptgen_simple(self):
        logging.info("scriptgen got here")
        set_module_args(dict(
            commands=[
                dict(
                    desc="command A",
                    path="/interface bridge",
                    state="present",
                    values=[
                        dict(
                            attr="name",
                            value="bridge1",
                        ),
                        dict(
                            attr="fast-forward",
                            value="no",
                        ),
                    ],
                    match=[
                        dict(
                            attr="name",
                            value="bridge1",
                        ),
                    ],
                ),
                dict(
                    desc="command B",
                    path="/interface bridge port",
                    state="absent",
                    values=[
                        dict(
                            attr="bridge",
                            value="bridge1",
                        ),
                        dict(
                            attr="interface",
                            value="interfaceA",
                        ),
                        dict(
                            attr="hw",
                            value="no",
                        ),
                    ],
                    match=[
                        dict(
                            attr="bridge",
                            value="bridge1",
                        ),
                        dict(
                            attr="interface",
                            value="interfaceA",
                        ),
                    ],
                ),
            ],
            ),
        )
        result = self.execute_module(changed=True)
        logging.info("scriptgen result:")
        logging.info(result)
        commandA = result['meta']['input'][0]
        self.assertEqual(commandA['desc'], 'command A')
        self.assertEqual(commandA['path'], '/interface bridge')
        self.assertEqual(commandA['state'], 'present')
        commandB = result['meta']['input'][1]
        self.assertEqual(commandB['desc'], 'command B')
        self.assertEqual(commandB['path'], '/interface bridge port')
        self.assertEqual(commandB['state'], 'absent')


    def test_get_argument_spec(self):
        argspec = scriptgen.get_argument_spec()
        print(argspec)
        #assert argspec.commands.elements.desc.required == True  # doesn't work - would need to parse
        assert argspec['commands']['options']['desc']['required'] == True


# Plan
# 1. add spec to scriptgen module
# 2. create test fixutres with sample commands - valid and invalid
# 3. process commands to routeros script
# 4. add validation


# ?????????
# create a fake module api
# create a test object for module
# - provide ros request object lists
# - consider scenarios that will generate different ros scripts
# - object per scenario
# create a test that uses the fake module to verify main
# implement scripgen happy path
# add module api and request valiation
# assert outputs of fake scenarios
# add execute module that depends on routeros.commands module



# class AddTester(unittest.TestCase):

#     def SetUp():
#         self.a = 10
#         self.b = 23

#     # this function will
#     def test_add():
#       c = 33
#       assert self.a + self.b == c

#    # this function will
#     def test_subtract():
#       c = -13
#       assert self.a - self.b == c

# class TestRouterosObjectsScriptgenModule(TestRouterosObjectsModule):

#     module = command

#     def setUp(self):
#         super(TestRouterosObjectsModule, self).setUp()

#         # self.mock_run_commands = patch('ansible_collections.community.routeros_objects.plugins.modules.scriptgen.main')
#         self.run_commands = self.mock_run_commands.start()

#     def tearDown(self):
#         super(TestRouterosObjectsModule, self).tearDown()
#         self.mock_run_commands.stop()

#     def load_fixtures(self, commands=None):

#         def load_from_file(*args, **kwargs):
#             module, commands = args
#             output = list()

#             for item in commands:
#                 try:
#                     obj = json.loads(item)
#                     command = obj
#                 except ValueError:
#                     command = item
#                 filename = str(command).replace(' ', '_').replace('/', '')
#                 output.append(load_fixture(filename))
#             return output

#         self.run_commands.side_effect = load_from_file

#     def test_simple(self):
#         set_module_args(dict(commands=['asdfasdf']))
#         result = self.execute_module(changed=True)
#         self.assertEqual(len(result['stdout']), 1)
#         self.assertTrue('foo: "bar"' in result['stdout'][0])

