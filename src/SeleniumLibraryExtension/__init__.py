#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary import SeleniumLibrary

from SeleniumLibraryExtension.decorators import DocInherit
from SeleniumLibraryExtension.version import get_version

from SeleniumLibraryExtension.keywords import ElementKeywordsExtension

from SeleniumLibraryExtension.base.contextpatch import ContextPatch

__version__ = get_version()


@DocInherit
class SeleniumLibraryExtension(SeleniumLibrary):
    # ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, timeout=5.0, implicit_wait=0.0,
                 run_on_failure='Capture Page Screenshot',
                 screenshot_root_directory=None):

        # self._builtin = BuiltIn()
        SeleniumLibrary.__init__(self, timeout=timeout, implicit_wait=implicit_wait,
                                 run_on_failure=run_on_failure,
                                 screenshot_root_directory=screenshot_root_directory)
        # ContextPatch.__init__(self)
        self.add_library_components([ElementKeywordsExtension(self)])

if __name__=='__main__':
    esl = SeleniumLibraryExtension()
    print(dir(esl))
    print(esl.__init__.__doc__)
