# This file is placed in the Public Domain.
#
# pylint: disable=R0903


"mixin"


import unittest


from otpcr.lib.object import Object


class Mix:

    "class to mixin."

    a = "b"


class Mixin(Mix, Object):

    "mixin class"


class TestMixin(unittest.TestCase):

    "test mixin classes."

    def test_mixin(self):
        "mixin test."
        mix = Mixin()
        self.assertTrue(isinstance(mix, Mixin))
