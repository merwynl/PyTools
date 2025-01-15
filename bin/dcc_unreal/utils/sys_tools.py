"""
Series of snippets for UE4 system queries
"""

import unreal
import os
import sys

def print_py_path():
    '''
    Prints all the Unreal Py paths
    NOTE: Not all paths printed exists on disk
    '''
    for path in sys.path:
        print path


def start_file():
    '''
    Starts a file with an associated program.
    NOTE: In this scenario, the path entered does not exists on disk.
    A directory will be created but there is no file on disk to start.
    Creating a file & restarting the engine will solve the issue
    '''
    os.startfile("C:/Users/touka/Desktop/git-dev/pylab/unreal/unrealProject/test/Content/Python")


def log_to_unreal():
    '''
    Prints something to unreals output log
    '''
    unreal.log('Awesomesauce')


def log_warning_to_unreal():
    '''
    Prints something to unreals output log
    '''
    unreal.log_warning('Awesomesauce')


def makeDirs():
    '''
    Makes a directory at the specified path
    '''
    os.makedirs("C:/Users/m/Desktop/git-dev/pylab/unreal")
