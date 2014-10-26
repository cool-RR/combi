#!/usr/bin/env python

# Copyright 2009-2015 Ram Rachum.
# This program is distributed under the MIT license.

'''Setuptools setup file for `combi`.'''

import os
import setuptools
import sys

### Confirming correct Python version: ########################################
#                                                                             #
if sys.version_info[:2] <= (2, 6):
    raise Exception(
        "You're using Python <= 2.6, but this package requires either Python "
        "2.7, or 3.3 or above, so you can't use it unless you upgrade your "
        "Python version."
    )
if sys.version_info[0] == 3 and sys.version_info[1] <= 2:
    raise Exception(
        "You're using Python <= 3.2, but this package requires either Python "
        "3.3 or above, or Python 2.7, so you can't use it unless you upgrade "
        "your Python version."
    )
#                                                                             #
### Finished confirming correct Python version. ###############################

if sys.version_info[0] == 3:
    source_folder = 'source_py3'
else:
    source_folder = 'source_py2'


def get_combi_packages():
    '''
    Get all the packages in `combi`.
    
    Returns something like:
    
        ['combi', 'combi.perming', ... ]
        
    '''
    return ['combi.' + p for p in
            setuptools.find_packages('%s/combi' % source_folder)] + \
           ['combi']


def get_test_combi_packages():
    '''
    Get all the packages in `test_combi`.
    
    Returns something like:
    
        ['test_combi', 'test_combi.test_whatever', ... ]
        
    '''
    return ['test_combi.' + p for p in
            setuptools.find_packages('%s/test_combi' % source_folder)] + \
           ['test_combi']


def get_packages():
    '''
    Get all the packages in `combi` and `test_combi`.
    
    Returns something like:
    
        ['test_combi', 'combi', 'combi.perming', ... ]
        
    '''
    return get_combi_packages() + get_test_combi_packages()


my_long_description = \
'''
blocktododoc from blog post
'''

my_classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent', 
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
]


install_requires = ['setuptools']
    

setuptools.setup(
    name='combi',
    version='0.1',
    test_suite='nose.collector',
    install_requires=install_requires,
    tests_require=['nose>=1.0.0',
                   'docutils>=0.8'],
    description='A Pythonic framework for combinatoricss',
    author='Ram Rachum',
    author_email='ram@rachum.com',
    package_dir={'': source_folder}, 
    packages=get_packages(),
    scripts=['%s/test_combi/scripts/_test_combi.py' % source_folder],
    long_description=my_long_description,
    license='MIT',
    classifiers=my_classifiers,
    include_package_data=True,
    zip_safe=False,
)

