#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (c) 2017, 2018 Ying Jun <WandyYing@users.noreply.github.com>

import unittest
import sys
sys.path.append('src')
from SeleniumLibraryExtension.decorators import DocInherit


class X(object):
    def please_implement(self):
        """
        I have a very thorough documentation
        :return:
        """
        raise NotImplementedError

    @property
    def speed(self):
        """
        Current speed in knots/hour.
        :return:
        """
        return 0

    @speed.setter
    def speed(self, value):
        """

        :param value:
        :return:
        """
        pass


class SpecialX(X):
    def please_implement(self):
        return True

    @property
    def speed(self):
        return 10

    @speed.setter
    def speed(self, value):
        self.sp = value


class VerySpecial(X):
    def speed(self):
        """
        The fastest speed in knots/hour.
        :return: 100
        """
        return 100

    def please_implement(self):
        """
        I have my own words!
        :return bool: Always false.
        """
        return False

    def not_inherited(self):
        """
        Look at all these words!
        :return:
        """


class A(object):
    def please_implement(self):
        """
        This doc is not used because X is resolved first in the MRO.
        :return:
        """
        pass


class B(A):
    pass


class HasNoWords(SpecialX, B):
    def please_implement(self):
        return True

    @property
    def speed(self):
        return 10

    @speed.setter
    def speed(self, value):
        self.sp = value

class Test(unittest.TestCase):

    def test_null(self):
        class Foo(object):

            def frobnicate(self): pass

        @DocInherit
        class Bar(Foo):
            pass

        # self.assertEqual(Bar.__doc__, object.__doc__)
        # self.assertEqual(Bar().__doc__, object.__doc__)
        self.assertEqual(Bar.frobnicate.__doc__, None)

    def test_inherit_from_parent(self):
        class Foo(object):
            'Foo'

            def frobnicate(self):
                'Frobnicate this gonk.'

        @DocInherit
        class Bar(Foo):
            pass
        self.assertEqual(Foo.__doc__, 'Foo')
        self.assertEqual(Foo().__doc__, 'Foo')
        # self.assertEqual(Bar.__doc__, 'Foo')
        # self.assertEqual(Bar().__doc__, 'Foo')
        self.assertEqual(Bar.frobnicate.__doc__, 'Frobnicate this gonk.')

    def test_inherit_from_mro(self):
        class Foo(object):
            'Foo'

            def frobnicate(self):
                'Frobnicate this gonk.'
        class Bar(Foo):
            pass

        @DocInherit
        class Baz(Bar):
            pass

        # self.assertEqual(Baz.__doc__, 'Foo')
        # self.assertEqual(Baz().__doc__, 'Foo')
        self.assertEqual(Baz.frobnicate.__doc__, 'Frobnicate this gonk.')

    def test_inherit_metaclass_(self):
        class Foo(object):
            'Foo'

            def frobnicate(self):
                'Frobnicate this gonk.'

        @DocInherit
        class Bar(Foo):
            pass

        class Baz(Bar):
            pass
        # self.assertEqual(Baz.__doc__, 'Foo')
        # self.assertEqual(Baz().__doc__, 'Foo')
        self.assertEqual(Baz.frobnicate.__doc__, 'Frobnicate this gonk.')

    def test_property(self):
        class Foo(object):
            @property
            def frobnicate(self):
                'Frobnicate this gonk.'

        @DocInherit
        class Bar(Foo):
            @property
            def frobnicate(self): pass

        self.assertEqual(Bar.frobnicate.__doc__, 'Frobnicate this gonk.')
if __name__ == '__main__':
    sys.argv.insert(1, '--verbose')
    unittest.main(argv=sys.argv)