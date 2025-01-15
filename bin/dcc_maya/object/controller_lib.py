"""This is a used as an example for importing a separate Python package.
"""

from maya import cmds
import os
import json
import pprint


# Get the user prefs dir
userAppDir = cmds.internalVar(userAppDir=True)
DIRECTORY = os.path.join(userAppDir, 'controllerLibrary')

def create_directory(directory=DIRECTORY):
    """Creates the given directory if it doesn't already exist
    
    Keyword Arguments:
        directory {[type]} -- [description] (default: {DIRECTORY})
    """    
    if not os.path.exists(directory):
        os.mkdir(directory)