import pymel.core as pm

SUFFIXES = {
    'mesh': 'geo',
    'joint': 'jpt',
    'locator': 'loc',
    'aiAreaLight': 'lgt',
    'camera': None
}

DEFAULT_SUFFIX = 'grp'


def rename():
    selection = pm.ls(selection=True)
    if len(selection) == 0:
        selection = pm.ls(dag=True, long=True)
    # selection.sort(key=len, reverse=True)
    for obj in selection:
        short_name = obj.split("|")[-1]

        children = pm.listRelatives(obj, children=True, fullPath=True) or []

        if len(children) == 1:
            child = children[0]
            obj_type = pm.objectType(child)
        else:
            obj_type = pm.objectType(obj)

        suffix = SUFFIXES.get(obj_type, DEFAULT_SUFFIX)

        if not suffix:
            continue

        if obj.endswith(suffix):
            continue

        new_name = short_name + '_' + suffix
        pm.rename(obj, new_name)


rename()
