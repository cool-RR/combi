# Copyright 2009-2017 Ram Rachum.
# This program is distributed under the MIT license.

'''Defines exceptions.'''

from combi._python_toolbox.exceptions import CuteException


class SleekRefDied(CuteException):
    '''You tried to access a sleekref's value but it's already dead.'''