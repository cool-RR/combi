# Copyright 2009-2015 Ram Rachum.
# This program is distributed under the MIT license.

import combi._python_toolbox

from combi._python_toolbox.math_tools import binomial

from combi._python_toolbox.nifty_collections import (Bag, OrderedBag, FrozenBag,
                                              FrozenOrderedBag)

from .chain_space import ChainSpace
from .product_space import ProductSpace
from .map_space import MapSpace
from .selection_space import SelectionSpace

from .perming import (PermSpace, CombSpace, Perm, UnrecurrentedPerm, Comb,
                      UnrecurrentedComb, UnallowedVariationSelectionException)

__version_info__ = combi._python_toolbox.version_info.VersionInfo(0, 1, 0)
__version__ = __version_info__.version_text

