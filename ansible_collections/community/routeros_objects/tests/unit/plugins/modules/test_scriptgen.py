# Copyright (c) 2016 Red Hat Inc.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# import json

# from ansible_collections.community.routeros_objects.tests.unit.compat.mock import patch
# from ansible_collections.community.routeros_objects.plugins.modules import command
# from ansible_collections.community.routeros_objects.tests.unit.plugins.modules.utils import set_module_args
# from .routeros_objects_module import TestRouterosObjectsModule, load_fixture


import unittest

class AddTester(unittest.TestCase):

    def SetUp():
        self.a = 10
        self.b = 23

    # this function will
    def test_add():
      c = 33
      assert self.a + self.b == c

   # this function will
    def test_subtract():
      c = -13
      assert self.a - self.b == c

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

