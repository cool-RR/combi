# Copyright 2009-2015 Ram Rachum.
# This program is distributed under the MIT license.

'''
Python Toolbox is a collection of Python tools.

These tools include caching, context manager tools, data structures, binary
search, import tools, tools for manipulating Python's built-in types, and many
more.

Visit http://pypi.python.org/pypi/python_toolbox/ for more info.
'''

import combi._python_toolbox._bootstrap
import combi._python_toolbox
import combi._python_toolbox.monkeypatch_copyreg
import combi._python_toolbox.monkeypatch_envelopes
from .version_info import VersionInfo

__version_info__ = VersionInfo(0, 7, 0)
__version__ = __version_info__.version_text

