#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary import SeleniumLibrary

from SeleniumLibraryExtension.decorators import DocInherit
from SeleniumLibraryExtension.version import get_version

__version__ = get_version()


@DocInherit
class ExtendedSeleniumLibrary(SeleniumLibrary):
    pass

if __name__=='__main__':
    esl = ExtendedSeleniumLibrary()
