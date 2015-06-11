
Combi is a Pythonic package for `combinatorics`_.

Combi lets you explore spaces of `permutations`_ and `combinations`_ as if they
were Python sequences, but without generating all the permutations/combinations
in advance. It lets you specify a lot of special conditions on these spaces. It
also provides a few more classes that might be useful in combinatorics
programming.

Combi is released under the MIT license.

Combi documentation: https://combi.readthedocs.org/en/stable/

Combi on GitHub: https://github.com/cool-RR/combi

Combi on PyPI: https://pypi.python.org/pypi/combi

Changelog: https://combi.readthedocs.org/en/stable/changelog.html

Basic usage
===========

Use `PermSpace`_ to create a permutation space:

.. code:: python

   >>> from combi import *
   >>> perm_space = PermSpace('meow')
   
It behaves like a sequence:

.. code:: python

   >>> len(perm_space)
   24
   >>> perm_space[7]
   <Perm: ('e', 'm', 'w', 'o')>
   >>> perm_space.index('mowe')
   3
   
And yet the permutations are created on-demand rather than in advance.

Use `CombSpace`_ to create a combination space, where order doesn't
matter:

.. code:: python

   >>> comb_space = CombSpace(('vanilla', 'chocolate', 'strawberry'), 2)
   >>> comb_space
   <CombSpace: ('vanilla', 'chocolate', 'strawberry'), n_elements=2>
   >>> comb_space[2]
   <Comb, n_elements=2: ('chocolate', 'strawberry')>
   >>> len(comb_space)
   3

For more details, `try the tutorial`_ or see the `documentation contents`_.

Features
========

- `PermSpace`_ lets you explore a space of permutations as if it was a
  Python sequence.
  
  * Permutations are generated on-demand, so huge permutation spaces can be 
    created easily without big memory footprint.
  * `PermSpace`_ will notice if you have repeating elements in your sequence, 
    and treat all occurences of the same value as interchangable rather than 
    create redundant permutations.
  * A custom domain can be specified instead of just using index numbers.
  * You may specify some elements to be fixed, so they'll point to the same
    value in all permutations. (Useful for limiting an experiment to a subset 
    of the original permutation space.)
  * Permutation spaces may be limited to a certain degree of permutations. (A
    permutation's degree is the number of transformations it takes to make it.)
  * `k-permutations`_ are supported.
  * You may specify a custom type for the generated permutations, so you could 
    implement your own functionality on them.
    
- `CombSpace`_ lets you explore a space of combinations as if it was a
  Python sequence.
  
- `MapSpace`_ is like Python's built-in `map`_, except it's a
  sequence that allows index access.
  
- `ProductSpace`_ is like Python's `itertools.product`_, except
  it's a sequence that allows index access.
  
- `ChainSpace`_ is like Python's `itertools.chain`_, except
  it's a sequence that allows index access.
  
- `SelectionSpace`_ is a space of all selections from a sequence, of all
  possible lengths.
  
- The `Bag`_ class is a multiset like Python's `collections.Counter`_, except 
  it offers far more functionality, like more `arithmetic operations between 
  bags`_, `comparison between bags`_, and more. (It can do that because unlike 
  Python's `collections.Counter`_, it only allows natural numbers as keys.)
  
- Classes `FrozenBag`_, `OrderedBag`_ and `FrozenOrderedBag`_ are provided, 
  which are variations on `Bag`_.


Requirements
============

* Python, version 2.7 or 3.3 or above. If you're new to Python, `download
  the newest version from here <http://python.org/download>`_.
 
* `Setuptools`_.


Installation
============

Use `pip`_ to install Combi:

.. code:: bash

   $ pip install combi


Community
=========

Combi on GitHub: https://github.com/cool-RR/combi Feel free to fork and send
pull requests!

There are three Combi groups, a.k.a. mailing lists:

- If you need help with Combi, post a message on `the combi-users
  Google Group <https://groups.google.com/forum/#!forum/combi-users>`_.

- If you want to help on the development of Combi itself, come say
  hello on `the combi-dev Google Group
  <https://groups.google.com/forum/#!forum/combi-dev>`_.

- If you want to be informed on new releases of Combi, sign up for
  `the low-traffic combi-announce Google Group
  <https://groups.google.com/forum/#!forum/combi-announce>`_.
  

-------------------------------------------------------------------------------

Combi was created by Ram Rachum. I provide 
`Development services in Python and Django <https://chipmunkdev.com>`_.



.. _mailing list: https://groups.google.com/forum/#!forum/combi-users
.. _combinatorics: https://en.wikipedia.org/wiki/Combinatorics
.. _permutations: https://en.wikipedia.org/wiki/Permutation
.. _k-permutations: https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n
.. _combinations: https://en.wikipedia.org/wiki/Combination
.. _Setuptools: https://pypi.python.org/pypi/setuptools
.. _pip: https://pypi.python.org/pypi/pip

.. _PermSpace: https://combi.readthedocs.org/en/stable/perm_space_and_perm.html#permspace
.. _CombSpace: https://combi.readthedocs.org/en/stable/comb_space_and_comb.html#combspace
.. _MapSpace: https://combi.readthedocs.org/en/stable/other_classes.html#mapspace
.. _ProductSpace: https://combi.readthedocs.org/en/stable/other_classes.html#productspace
.. _ChainSpace: https://combi.readthedocs.org/en/stable/other_classes.html#chainspace
.. _SelectionSpace: https://combi.readthedocs.org/en/stable/other_classes.html#selectionspace
.. _Bag: https://combi.readthedocs.org/en/stable/bags.html#bag
.. _FrozenBag: https://combi.readthedocs.org/en/stable/bags.html#frozenbag
.. _OrderedBag: https://combi.readthedocs.org/en/stable/bags.html#orderedbag
.. _FrozenOrderedBag: https://combi.readthedocs.org/en/stable/bags.html#frozenorderedbag
.. _collections.Counter: https://docs.python.org/3/library/collections.html#collections.Counter
.. _try the tutorial: https://combi.readthedocs.org/en/stable/intro.html
.. _documentation contents: https://combi.readthedocs.org/en/stable/index.html
.. _map: https://docs.python.org/3/library/functions.html#map
.. _itertools.product: https://docs.python.org/3/library/itertools.html#itertools.product
.. _itertools.chain: https://docs.python.org/3/library/itertools.html#itertools.chain
.. _arithmetic operations between bags: https://combi.readthedocs.org/en/stable/bags.html#bags-operations
.. _comparison between bags: https://combi.readthedocs.org/en/stable/bags.html#bags-comparisons