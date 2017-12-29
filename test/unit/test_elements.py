#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (c) 2017, 2018 Ying Jun <WandyYing@users.noreply.github.com>

from sys import path
path.append('src')
import unittest
from unittest import mock
from SeleniumLibraryExtension.keywords import ElementKeywordsExtension
from selenium.webdriver.remote.webelement import WebElement
from SeleniumLibrary.keywords import ElementKeywords

class ElementKeywordsTests(unittest.TestCase):
    """Extended element keyword test class."""

    def setUp(self):
        """Instantiate the extended element class."""
        ctx = mock.Mock()
        self.driver = mock.Mock()
        self.driver.session_id = 'session'
        self.element = ElementKeywordsExtension(ctx)
        self.element._current_browser = mock.Mock()
        self.element._info = mock.Mock()

    def test_should_inherit_keywords(self):
        """Extended element instance should inherit Selenium 3 element instances."""
        self.assertIsInstance(self.element, ElementKeywords)

    def test_should_click_element(self):
        """Should click an element."""
        # pylint: disable=protected-access
        pass