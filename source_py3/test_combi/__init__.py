# Copyright 2009-2017 Ram Rachum.
# This program is distributed under the MIT license.

import sys
try:
    import pathlib
except:
    from combi._python_toolbox.third_party import pathlib


import nose


if nose.__versioninfo__ < (1, 0, 0):
    raise Exception('Nose version 1.0.0 or higher is required to run tests.')


def __bootstrap():
    '''
    Add needed packages in repo to path if we can't find them.
    
    This adds `combi`'s root folder to `sys.path` if it can't
    currently be imported.
    '''
    import os
    import sys
    import imp

    def exists(module_name):
        '''
        Return whether a module by the name `module_name` exists.
        
        This seems to be the best way to carefully import a module.
        
        Currently implemented for top-level packages only. (i.e. no dots.)
    
        Doesn't support modules imported from a zip file.
        '''
        assert '.' not in module_name
        try:
            imp.find_module(module_name)
        except ImportError:
            return False
        else:
            return True
    
    if not exists('combi'):
        combi_candidate_path = pathlib(__file__).parent.parent.absolute()
        sys.path.append(combi_candidate_path)
        
        
__bootstrap()


_default_nose_arguments = [   
    '--verbosity=3',
    '--detailed-errors',
    '--with-xunit',
    '--cover-erase',
    '--cover-package=combi,test_combi',
    '--exe', # Needed because `setup.py` makes our test modules executable
]


def invoke_nose(arguments=_default_nose_arguments):
    '''Start Nose using this `test_combi` test package.'''
    nose.run(defaultTest='test_combi',
             argv=(arguments + sys.argv[1:]))
