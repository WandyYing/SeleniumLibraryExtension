#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (c) 2017, 2018 Ying Jun <WandyYing@users.noreply.github.com>

import time
from sys import exc_info
from time import sleep
from robot import utils
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import staleness_of, visibility_of
from selenium.webdriver.support.ui import WebDriverWait
from SeleniumLibrary.keywords import WaitingKeywords
from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibraryExtension.decorators import DocInherit
from SeleniumLibraryExtension.config import settings


@DocInherit
class WaitingKeywordsExtension(LibraryComponent):
    """WaitingKeywordsExtension are waiting related execution towards the requested browser."""


    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
