# Copyright 2009-2015 Ram Rachum.
# This program is distributed under the MIT license.

'''Testing module for `python_toolbox.re_tools`.'''

import re

from combi._python_toolbox import re_tools
from combi._python_toolbox.re_tools import searchall


def test_searchall():
    '''Test the basic workings of `searchall`.'''
    s = 'asdf df sfg s'
    result = searchall('(\w+)', s)
    assert len(result) == 4