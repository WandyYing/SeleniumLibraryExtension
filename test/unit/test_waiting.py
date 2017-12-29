#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (c) 2017, 2018 Ying Jun <WandyYing@users.noreply.github.com>

import unittest

from mockito import mock, unstub, when

# from SeleniumLibrary.keywords import WaitingKeywords
from SeleniumLibraryExtension.keywords import WaitingKeywordsExtension


class KeywordArgumentsWaitingKeywordsTest(unittest.TestCase):

    def setUp(self):
        self.ctx = mock()
        self.ctx.driver = mock()
        self.ctx.timeout = 0.01
        self.waiting = WaitingKeywordsExtension(self.ctx)

    def tearDown(self):
        unstub()

    def test_wait_for_condition(self):
        condition = 'return document.getElementById("intro")'
        error = 'did not become true'
        with self.assertRaisesRegex(AssertionError, error):
            self.waiting.wait_for_condition(condition)
        with self.assertRaisesRegex(AssertionError, 'foobar'):
            self.waiting.wait_for_condition(condition, 'None', 'foobar')

    def test_wait_until_page_contains(self):
        text = 'text'
        when(self.waiting).is_text_present(text).thenReturn(None)
        with self.assertRaisesRegex(AssertionError, "Text 'text' did not"):
            self.waiting.wait_until_page_contains(text)
        with self.assertRaisesRegex(AssertionError, "error"):
            self.waiting.wait_until_page_contains(text, 'None', 'error')

    def test__wait_for_ready_state_complete(self):
        timeout = 3
        # when(self.waiting)._wait_for_ready_state_complete.thenReturn(None)
        error = "never fully loaded"
        when(self.ctx.driver).execute_script("return document.readyState").thenReturn(None)
        with self.assertRaisesRegex(Exception, error):
            self.waiting._wait_for_ready_state_complete(2)


