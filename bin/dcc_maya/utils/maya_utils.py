import os
import sys
import pymel.core as pm
import maya.cmds as cmds
import PySide2


# List Shape Relatives
def get_shapes():
    sel = pm.ls(sl=True)
    shapes_list = []
    for s in sel:
        shapes = pm.listRelatives(s, shapes=True)
        add_shapes = shapes_list.append(shapes)
    print(shapes_list)
    return shapes_list
    # for shape in shapes:
    #     print shape


# Group each
def group_each():
    sel = pm.ls(sl=True)
    for g in sel:
        pm.group(g, name='sm_')


# Rename selection
def replace_name():
    sel = pm.ls(sl=True)
    for g in sel:
        new_name = g.replace('geo_', '')
        pm.rename(g, new_name)


replace_name()
