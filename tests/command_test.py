#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import tests.context
from tests.helpers import run_as_unit_test


class TestCommands(unittest.TestCase):

    def test_start(self):
        result = run_as_unit_test('start')

        self.assertEqual(result, 'vagrant up && vagrant ssh')

    def test_pause(self):
        result = run_as_unit_test('pause')

        self.assertEqual(result, 'vagrant suspend')

    def test_stop(self):
        result = run_as_unit_test('stop')

        self.assertEqual(result, 'vagrant halt')

    def test_restart(self):
        result = run_as_unit_test('restart')

        self.assertEqual(result, 'vagrant halt && vagrant up && vagrant ssh')

    def test_status(self):
        result = run_as_unit_test('status')

        self.assertEqual(result, 'vagrant status')

    def test_login(self):
        result = run_as_unit_test('login')

        self.assertEqual(result, 'vagrant ssh')

    def test_delete(self):
        result = run_as_unit_test('delete')

        self.assertEqual(result, 'vagrant destroy --force')

    def test_reinstall(self):
        result = run_as_unit_test('reinstall')

        self.assertEqual(result, 'vagrant destroy --force && vagrant up && vagrant ssh')

    def test_share(self):
        result = run_as_unit_test('share')

        self.assertEqual(result, 'vagrant share')


if __name__ == '__main__':
    unittest.main()
