"""
 ..module:: project documentation
    :platform: windows
    :synopsis: module for adding attrs
"""

import pymel.core as pm
import os
import sys


def add_attr(attrName, niceName):
    """
    addAttr [summary]
    
    :param attrName: [description]
    :type attrName: [type]
    :param niceName: [description]
    :type niceName: [type]
    """
    sel = pm.ls(sl=True)
    for i in sel:
        pm.addAttr(i,ln=attrName, nn=niceName, dt='bool')
        pm.setAttr(i,lock=True)
    sys.__stdout__.write( str(attrName) + ' 完成しました!' + '\n')
    print ('\n' + str(attrName) + ' == 含みました!' + '\n')


add_attr('TestAttr', 'Test Attr')