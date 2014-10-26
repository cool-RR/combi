# Copyright 2009-2015 Ram Rachum.
# This program is distributed under the MIT license.

'''Testing module for `python_toolbox.abc_tools.AbstractStaticMethod`.'''

import sys
import abc

import nose

from python_toolbox.abc_tools import AbstractStaticMethod


def test_instantiate_without_subclassing():
    '''Test you can't instantiate a class with an `AbstractStaticMethod`.'''
    
    class A(object):
        __metaclass__ = abc.ABCMeta
        
        @AbstractStaticMethod
        def f():
            pass
         
    nose.tools.assert_raises(TypeError, lambda: A())
    
        
def test_override():
    '''
    Can't instantiate subclass that doesn't override `AbstractStaticMethod`.
    '''
    
    class B(object):
        __metaclass__ = abc.ABCMeta
        
        @AbstractStaticMethod
        def f():
            pass
    
    class C(B):
        @staticmethod
        def f():
            return 7
        
    c = C()
    
    assert C.f() == c.f() == 7
    
    