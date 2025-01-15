"""Gear creator
"""


from maya import cmds
import pymel.core as pm


def create_gear(teeth=10, length=0.3):
    """This creates a gear with the given parameter

    Keyword Arguments:
        teeth {int} -- Number of teeth to create (default: {10})
        length {float} -- Length of each gear teeth (default: {0.3})

    Returns:
        [type] -- A tuple of the transform, constructor and extrude node
    """
    # Teeth are every alternate face so spans x 2
    spans = teeth * 2
    transform, constructor = pm.polyPipe(subdivisionsAxis = spans)
    side_faces = range(spans*2, spans*3, 2)
    pm.select(clear=True)

    for face in side_faces:
        pm.select('%s.f[%s]' % (transform, face), add=True )
    extrude = pm.polyExtrudeFacet(localTranslateZ=length)[0]
    return transform, constructor, extrude


def change_teeth(constructor, extrude, teeth=10, length=0.3):
    spans = teeth*2
    pm.polyPipe(constructor, edit=True, subdivisionsAxis=spans)
    side_faces = range(spans*2, spans*3, 2)
    # print side_faces
    face_names = []

    for face in side_faces:
        face_name = 'f[%s]' % face
        face_names.append(face_name)

    print(face_names)

    pm.setAttr('%s.inputComponents' % extrude, len(face_names), *face_names, type='componentList')

    pm.polyExtrudeFacet(extrude, edit=True, ltz=length)