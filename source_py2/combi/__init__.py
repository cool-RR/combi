# Copyright 2009-2015 Ram Rachum.
# This program is distributed under the MIT license.

'''
Combi is a Pythonic package for combinatorics.

Combi lets you explore spaces of permutations and combinations as if they were
Python sequences, but without generating all the permutations/combinations in
advance. It lets you specify a lot of special conditions on these spaces. It
also provides a few more classes that might be useful in combinatorics
programming.

Visit http://pypi.python.org/pypi/combi/ for more info.
'''

import combi._python_toolbox.version_info

from combi._python_toolbox.math_tools import binomial

from combi._python_toolbox.nifty_collections import (Bag, OrderedBag,
                                                     FrozenBag,
                                                     FrozenOrderedBag)

from .chain_space import ChainSpace
from .product_space import ProductSpace
from .map_space import MapSpace
from .selection_space import SelectionSpace

from .perming import (PermSpace, CombSpace, Perm, UnrecurrentedPerm, Comb,
                      UnrecurrentedComb, UnallowedVariationSelectionException)

__version_info__ = combi._python_toolbox.version_info.VersionInfo(1, 1, 1)
__version__ = __version_info__.version_text

