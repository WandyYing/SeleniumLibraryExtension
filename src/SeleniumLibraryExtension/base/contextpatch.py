#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ying Jun<wandy1208@live.com>

from SeleniumLibrary.base.context import ContextAware

class ContextPatch(object):

    @property
    def element_finder(self):
        return self.ctx.element_finder

    @element_finder.setter
    def element_finder(self, ele_finder):
        self.ctx.element_finder = ele_finder

    # element_finder = property(get_element_finder, set_element_finder)
    ContextAware.element_finder = element_finder