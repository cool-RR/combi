#!/usr/bin/env python

# Copyright 2009-2017 Ram Rachum.
# This program is distributed under the MIT license.

'''
Script for launching `combi` tests when installed in local Python.
'''


import test_combi


if __name__ == '__main__':
    test_combi.invoke_nose()