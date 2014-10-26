# Copyright 2009-2015 Ram Rachum.
# This program is distributed under the MIT license.

'''
Defines the `EmittingOrderedSet` class.

See its documentation for more details.
'''

from .ordered_set import (
    OrderedSet, KEY, PREV, NEXT
)


class EmittingOrderedSet(OrderedSet):
    '''An ordered set that emits to `.emitter` every time it's modified.'''
    
    def __init__(self, emitter, items=()):
        if emitter:
            from python_toolbox.emitting import Emitter
            assert isinstance(emitter, Emitter)
        self.emitter = emitter
        OrderedSet.__init__(self, items)

        
    def add(self, key):
        """ Add an element to a set.
    
        This has no effect if the element is already present. """
        if key not in self._map:
            end = self._end
            curr = end[PREV]
            curr[NEXT] = end[PREV] = self._map[key] = [key, curr, end]
            if self.emitter:
                self.emitter.emit()

                
    def discard(self, key):
        """ Remove an element from a set if it is a member.
        
        If the element is not a member, do nothing. """
        if key in self._map:        
            key, prev, next = self._map.pop(key)
            prev[NEXT] = next
            next[PREV] = prev
            if self.emitter:
                self.emitter.emit()

                
    def set_emitter(self, emitter):
        '''Set `emitter` to be emitted with on every modification.'''
        self.emitter = emitter