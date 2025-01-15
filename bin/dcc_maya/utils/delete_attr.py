"""
project documentation
"""
import sys
import pymel.core as pm


def delete_attr(name='enterName'):
    """
    deleteAttr [summary]
    
    :param name: [description], defaults to 'enterName'
    :type name: str, optional
    """
    sel = pm.selected()
    attr_name = name
    for i in sel:
        pm.deleteAttr(i, at=attr_name)
    sys.__stdout__.write(str(attr_name) + '完成しました!' + '\n')
    print('\n' + str(attr_name) + ' == 削りました!' + '\n')
