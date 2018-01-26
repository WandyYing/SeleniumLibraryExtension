#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (c) 2017, 2018 Ying Jun <WandyYing@users.noreply.github.com>

import unittest

from mockito import mock, unstub, when
from robot.api import logger

from SeleniumLibraryExtension.keywords import ElementKeywordsExtension


class KeywordArgumentsElementTest(unittest.TestCase):

    def setUp(self):
        ctx = mock()
        ctx._browser = mock()
        self.element = ElementKeywordsExtension(ctx)

    def tearDown(self):
        unstub()

    def test_click_element_js(self):
        locator = '//div'
        element = mock()
        when(self.element).find_element(locator).thenReturn(element)
        element.click_element_js(locator)