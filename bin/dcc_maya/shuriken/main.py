import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
import maya.api.OpenMaya as OpenMaya

OpenMaya.MFnMesh.getAssignedUVs()

if cmds.workspaceControl("Shuriken", exists=True):
    cmds.deleteUI("Shuriken")

VERSION = "0.0.1"


def UI(*args):
    # Main Column layout
    cmds.columnLayout(adj=True, w=250, h=805)

    # Title
    cmds.separator(height=5, style='none')
    cmds.text(label='--- Shuriken Toolkit ---')
    cmds.separator(height=5, style='none')

    # ____________________________________________INFO
    # Information Layout
    information_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(label="INFO", collapsable=0, collapse=0, backgroundColor=[0.15, 0.15, 0.15])
    cmds.text('Log', l="  Shuriken " + VERSION, bgc=(0.2, 0.2, 0.2), h=30, align='left')

    cmds.setParent(information_layout)

    # ____________________________________________PRIMITIVES
    # Primitive Layout
    primitives_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(label="PRIMITIVES", collapsable=1, collapse=0, backgroundColor=[0.15, 0.15, 0.55])
    cmds.rowColumnLayout(numberOfColumns=5, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # Primitive section icon paths
    icon_sphere = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/primitive_sphere.png"
    icon_cube = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/primitive_cube.png"
    icon_cylinder = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/primitive_cylinder.png"
    icon_plane = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/primitive_plane.png"
    icon_torus = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/primitive_torus.png"

    # Buttons for creating primitives
    create_sphere_button = cmds.symbolButton(image=icon_sphere, command="create_sphere()", annotation="Create a Sphere")
    create_cube_button = cmds.symbolButton(image=icon_cube, command="create_cube()", annotation="Create a Cube ")

    # Buttons for creating cylinder on 3 different axis
    create_cylinder_button = cmds.symbolButton(image=icon_cylinder, command="create_cylinder_z()", annotation="Create a Cylinder. Default Axis: Z")
    cmds.popupMenu()
    cmds.menuItem(label='Cylinder X', command='create_cylinder_x()')
    cmds.menuItem(label='Cylinder Y', command='create_cylinder_y()')
    cmds.menuItem(label='Cylinder Z', command='create_cylinder_z()')

    # Buttons for creating a plane with 3 different axis options
    create_plane_button = cmds.symbolButton(image=icon_plane, command="create_plane_z()", annotation="Creates a Plane. Default Axis: Z")
    cmds.popupMenu()
    cmds.menuItem(label='Plane X', command='create_plane_x()')
    cmds.menuItem(label='Plane Y', command='create_plane_y()')
    cmds.menuItem(label='Plane Z', command='create_plane_z()')

    create_torus_button = cmds.symbolButton(image=icon_torus, command="create_torus()", annotation="Create a Torus")

    cmds.setParent(primitives_layout)
    cmds.separator(height=1, style='none')

    # ____________________________________________GRIDS
    # Grid Layout
    grid_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(label="GRID", collapsable=1, collapse=0, backgroundColor=[0.15, 0.35, 0.15])
    custom_grid_subdivision = cmds.intSliderGrp("Grid_Slide", l="Subdivisions", min=1, max=100, preventOverride=True, field=True,
                                                changeCommand="auto_grid_resize()", dragCommand="auto_grid_resize()", v=1, adj=0,
                                                columnAttach=[1, "left", 3], cw=[1, 80], annotation="Set Grid Subdivisions")
    cmds.rowColumnLayout(adj=True, numberOfColumns=5, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # UI buttons for setting different grid properties
    grid_subd_1 = cmds.button(l="1", command="grid_size_a()", w=50, bgc=[0.15, 0.15, 0.15])
    grid_subd_10 = cmds.button(l="10", command="grid_size_b()", w=50, bgc=[0.15, 0.15, 0.15])
    grid_subd_20 = cmds.button(l="20", command="grid_size_c()", w=50, bgc=[0.15, 0.15, 0.15])
    grid_subd_50 = cmds.button(l="50", command="grid_size_d()", w=50, bgc=[0.15, 0.15, 0.15])
    grid_subd_100 = cmds.button(l="100", command="grid_size_e()", w=50, bgc=[0.15, 0.15, 0.15])

    cmds.setParent(grid_layout)
    cmds.separator(height=1, style='none')

    # ____________________________________________RENAME
    # Renamer layout
    rename_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(l="RENAME", collapsable=1, collapse=1, backgroundColor=[0.15, 0.35, 0.35])

    cmds.columnLayout(adj=True)
    cmds.rowLayout(nc=2, adj=True)

    cmds.textField("rename_prefix", h=30, w=186, pht=" Prefix")
    prefix_ui_button = cmds.button(l="Add", bgc=[0.2, 0.2, 0.2], h=30, w=52, command="prefix_button()",
                                   annotation='LMB: Add Prefix // RMB: Choose input method or a preset')

    cmds.popupMenu(p=prefix_ui_button)
    prefix_selections = cmds.radioMenuItemCollection()
    cmds.menuItem("default", rb=True, cl=prefix_selections, l='Custom')
    cmds.menuItem("group", rb=True, cl=prefix_selections, l='_grp_')
    cmds.menuItem("assembly", rb=True, cl=prefix_selections, l='_assembly_')
    cmds.menuItem("kit", rb=True, cl=prefix_selections, l='_kit_')
    cmds.menuItem("geo", rb=True, cl=prefix_selections, l='_geo_')
    cmds.menuItem("trim", rb=True, cl=prefix_selections, l='_trim_')
    cmds.menuItem("curve", rb=True, cl=prefix_selections, l='_curve_')
    cmds.menuItem("lite", rb=True, cl=prefix_selections, l='_lite_')

    cmds.setParent('..')

    cmds.rowLayout(nc=2, adj=True)
    cmds.textField("rename_suffix", h=30, w=186, pht=" Suffix")
    suffix_ui_button = cmds.button(l="Add", bgc=[0.2, 0.2, 0.2], h=30, w=52, command="prefix_button()",
                                   annotation='LMB: Add Suffix // RMB: Choose input method or a preset')

    cmds.popupMenu(p=suffix_ui_button)
    suffix_selections = cmds.radioMenuItemCollection()
    cmds.menuItem("default", rb=True, cl=suffix_selections, l='Custom')
    cmds.menuItem("floor", rb=True, cl=suffix_selections, l='_straight_01')
    cmds.menuItem("wall", rb=True, cl=suffix_selections, l='_corner_01')
    cmds.menuItem("kit", rb=True, cl=suffix_selections, l='_unique_01')

    cmds.setParent('..')
    cmds.separator(h=3, style='none')
    cmds.separator(h=3, style='in')
    cmds.separator(h=3, style='none')

    cmds.textField("rename_search", h=30, w=240, pht=" Search")
    cmds.rowLayout(numberOfColumns=2, adj=True)
    cmds.textField("rename_replace", h=30, w=120, pht=" Replace")
    cmds.button(l="Replace It!", bgc=[0.2, 0.2, 0.2], h=28, w=85, c=suffix_selections, ann="Replace a string with another")
    cmds.setParent('..')

    cmds.separator(h=3, style='none')
    cmds.separator(h=3, style='in')
    cmds.separator(h=3, style='none')

    fix_dup_names_button = cmds.button(l="Fix Duplicate Names", bgc=[0.2, 0.2, 0.2], h=30, w=45, command="fix_dup_names()",
                                       annotation='Fix duplicate names')
    conform_names = cmds.button(l="Conform Names", bgc=[0.2, 0.2, 0.2], h=30, w=45, command="conform_names()",
                                annotation='Conform all node name based on types')
    format_lowercase = cmds.button(l="Format to Lowercase", bgc=[0.2, 0.2, 0.2], h=30, w=45, command="format_lowercase()",
                                   annotation='Formats the selected nodes into lowercase')

    cmds.setParent(rename_layout)
    cmds.separator(h=1, style='none')

    # __________________________________________________________________MATERIALS
    # Quick materials layout
    materials_layout = cmds.columnLayout(adj=True)

    shader_library = ['lambert', 'blinn', 'phong', 'phongE', 'surfaceShader', 'rampShader', 'useBackground']

    section_frame_layout = cmds.frameLayout(l="MATERIALS", cll=1, cl=0, bgc=[0.55, 0.15, 0.25])
    cmds.rowColumnLayout(numberOfColumns=6, columnWidth=[(1, 40), (2, 40), (3, 40), (4, 40), (5, 40), (6, 40)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center'), (6, 'center')])

    default_shading = cmds.internalVar(upd=True) + "scripts/Shuriken/Icons/material_quick_default.png"
    green_lambert = cmds.internalVar(upd=True) + "scripts/Shuriken/Icons/material_quick_green.png"
    red_lambert = cmds.internalVar(upd=True) + "scripts/Shuriken/Icons/material_quick_red.png"
    blue_lambert = cmds.internalVar(upd=True) + "scripts/Shuriken/Icons/material_quick_blue.png"
    yellow_lambert = cmds.internalVar(upd=True) + "scripts/Shuriken/Icons/material_quick_yellow.png"
    dark_grey_lambert = cmds.internalVar(upd=True) + "scripts/Shuriken/Icons/material_quick_dark_grey.png"

    default_lambert_button = cmds.symbolButton(image=default_shading, c="lambert1()", annotation="Assign default lambert")
    cmds.popupMenu(p=default_lambert_button)
    cmds.menuItem(l='Select Objects', c='select_assigned_default_lambert()')
    cmds.menuItem(l='Select Material', c='select_default_lambert()')
    cmds.menuItem(l='Transparency', c='default_material_transparency()')
    quick_material_type = cmds.radioMenuItemCollection()
    cmds.menuItem("lambert", rb=True, cl=quick_material_type, l='lambert')
    cmds.menuItem("blinn", rb=True, cl=quick_material_type, l='blinn')

    green_lambert_button = cmds.symbolButton(image=green_lambert, c="green_lambert()",
                                             annotation="Assign green material or create one first if none exists. Default type is set to blinn.")
    cmds.popupMenu()
    cmds.menuItem(l='Select Objects', c='select_assigned_green_lambert()')
    cmds.menuItem(l='Select Material', c='select_green_lambert()')
    cmds.menuItem(l='Transparency', c='green_material_transparency()')
    quick_material_type = cmds.radioMenuItemCollection()
    cmds.menuItem("lambert", rb=True, cl=quick_material_type, l='lambert')
    cmds.menuItem("blinn", rb=True, cl=quick_material_type, l='blinn')

    red_lambert_button = cmds.symbolButton(image=red_lambert, c="red_lambert()",
                                           annotation="Assign red material or create one first if none exists. Default type is set to blinn.")
    cmds.popupMenu()
    cmds.menuItem(l='Select Objects', c='select_assigned_red_lambert()')
    cmds.menuItem(l='Select Material', c='select_red_lambert()')
    cmds.menuItem(l='Transparency', c='red_material_transparency()')
    quick_material_type = cmds.radioMenuItemCollection()
    cmds.menuItem("lambert", rb=True, cl=quick_material_type, l='lambert')
    cmds.menuItem("blinn", rb=True, cl=quick_material_type, l='blinn')

    blue_lambert_button = cmds.symbolButton(image=blue_lambert, c="blue_lambert()",
                                            annotation="Assign blue material or create one first if none exists. Default type is set to blinn.")
    cmds.popupMenu()
    cmds.menuItem(l='Select Objects', c='select_assigned_blue_lambert()')
    cmds.menuItem(l='Select Material', c='select_blue_lambert()')
    cmds.menuItem(l='Transparency', c='blue_material_transparency()')
    quick_material_type = cmds.radioMenuItemCollection()
    cmds.menuItem("lambert", rb=True, cl=quick_material_type, l='lambert')
    cmds.menuItem("blinn", rb=True, cl=quick_material_type, l='blinn')

    yellow_lambert_button = cmds.symbolButton(image=yellow_lambert, c="yellow_lambert()",
                                              annotation="Assign yellow material or create one first if none exists. Default type is set to blinn.")
    cmds.popupMenu()
    cmds.menuItem(l='Select Objects', c='select_assigned_yellow_lambert()')
    cmds.menuItem(l='Select Material', c='select_yellow_lambert()')
    cmds.menuItem(l='Transparency', c='yellow_material_transparency()')
    quick_material_type = cmds.radioMenuItemCollection()
    cmds.menuItem("lambert", rb=True, cl=quick_material_type, l='lambert')
    cmds.menuItem("blinn", rb=True, cl=quick_material_type, l='blinn')

    dark_grey_lambert_button = cmds.symbolButton(image=dark_grey_lambert, c="dark_grey_lambert()",
                                                 annotation="Assign dark grey material or create one first if none exists. Default type is set to blinn.")
    cmds.popupMenu()
    cmds.menuItem(l='Select Objects', c='select_assigned_dark_grey_lambert()')
    cmds.menuItem(l='Select Material', c='select_dark_grey_lambert()')
    cmds.menuItem(l='Transparency', c='dark_grey_material_transparency()')
    quick_material_type = cmds.radioMenuItemCollection()
    cmds.menuItem("lambert", rb=True, cl=quick_material_type, l='lambert')
    cmds.menuItem("blinn", rb=True, cl=quick_material_type, l='blinn')

    cmds.setParent('..')

    # Material section icon paths
    icon_unused_materials = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/material_delete_unused.png"
    icon_load_hypershade = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/material_hypershade.png"
    icon_material_instance_names = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/material_names.png"
    icon_select_similar = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/material_select_similar.png"
    icon_checkered_material = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/material_checker.png"

    cmds.rowColumnLayout(numberOfColumns=5, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])
    open_hypershade = cmds.symbolButton(image=icon_load_hypershade, c="open_hypershade()", annotation="Opens the hypershade")
    clear_unused_materials = cmds.symbolButton(image=icon_unused_materials, c="clear_unused_materials()",
                                               annotation="Clear unused materials and shading groups")
    select_similar = cmds.symbolButton(image=icon_select_similar, c="select_similar()",
                                       annotation="Selects objects in the scene with the same material assignment as the currently selected one")
    use_checekered_material = cmds.symbolButton(image=icon_checkered_material, c="apply_checkered()",
                                                annotation="Applys a checkered material to the current selection")

    conform_material_names = cmds.symbolButton(image=icon_material_instance_names, c="material_conform()",
                                               annotation="Appends mi_ to all existing materials if prefix doesn't exist")
    cmds.popupMenu()
    remove_pasted_from_material = cmds.menuItem(l="Replace pasted__", command="replace_pasted_material()",
                                                annotation='Replaces any pasted__ with mi_')
    append_mi = cmds.menuItem(l="Append mi_", command="append_mi()", annotation='Appends mi_ to the material name')

    cmds.setParent('..')

    cmds.rowLayout(nc=3, adj=True)
    cmds.button(l="List", w=75, bgc=[0.15, 0.15, 0.15], c="list_materials()")
    cmds.button(l="Assign", w=75, bgc=[0.15, 0.15, 0.15], c="materials_assign()")
    cmds.button(l="Duplicate", w=75, bgc=[0.15, 0.15, 0.15], c="materials_duplicate")

    cmds.setParent('..')
    cmds.rowLayout(nc=1, h=1, adj=True)

    cmds.setParent('..')
    cmds.textScrollList("material_list", h=160, allowMultiSelection=True, doubleClickCommand="material_rename()",
                        deleteKeyCommand="material_delete()", selectCommand="select_material()")

    cmds.rowLayout(nc=2, adj=True)
    cmds.textField("create_material", h=30, w=120, pht="Enter material name...")
    custom_material_button = cmds.button(l="Make it!", bgc=[0.2, 0.2, 0.2], h=28, w=65, c="make_custom_material()",
                                         ann="Creates a material with a custom name and assigns it to the current selection. // Right click for options")

    cmds.popupMenu(p=custom_material_button)
    material_type = cmds.radioMenuItemCollection()
    cmds.menuItem("lambert", radioButton=True, collection=material_type, l='lambert')
    cmds.menuItem("blinn", radioButton=True, collection=material_type, l='blinn')
    cmds.menuItem("phong", radioButton=True, collection=material_type, l='phong')
    cmds.menuItem("phongE", radioButton=True, collection=material_type, l='phongE')
    cmds.menuItem("surfaceShader", radioButton=True, collection=material_type, l='surfaceShader')

    cmds.setParent(materials_layout)
    cmds.separator(h=1, style='none')

    # __________________________________________________________________UV's
    # UV Section Layout
    uv_tools_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(l="UV'S", cll=1, cl=1, bgc=[0.3, 0.05, 0.7])
    cmds.rowColumnLayout(numberOfColumns=5, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # UV section icon paths
    icon_planar = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/project_planar.png"
    icon_spherical = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/project_spherical.png"
    icon_cylindrical = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/project_cylindrical.png"
    icon_auto = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/project_auto.png"
    icon_camera = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/project_camera.png"

    # UV projection methods
    project_uv_planar = cmds.symbolButton(image=icon_planar, command="project_planar('z')",
                                          annotation="Performs a Planar Projection on uv's. // Defaults to z axis.")
    cmds.popupMenu()
    cmds.menuItem(l='x', c="project_planar('x')")
    cmds.menuItem(l='y', c="project_planar('y')")
    cmds.menuItem(l='z', c="project_planar('z')")

    project_uv_spherical = cmds.symbolButton(image=icon_spherical, command="project_spherical()", annotation="Project UV's Spherical")
    project_uv_cylindrical = cmds.symbolButton(image=icon_cylindrical, command="project_cylindrical()", annotation="Project UV's Cylindrical")
    project_uv_auto = cmds.symbolButton(image=icon_auto, command="project_auto()", annotation="Project UV's Auto")
    project_uv_camera = cmds.symbolButton(image=icon_camera, command="project_camera()", annotation="Project UV's Camera")

    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=5, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # UV section icon paths
    icon_auto_lightmap = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/uv_lightmap.png"
    icon_auto_layout = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/uv_layout.png"
    icon_unfold_3d = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/uv_unfold_3d.png"
    icon_unfold_legacy = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/uv_unfold_legacy.png"
    icon_stack_uv = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/uv_stack.png"

    uv_lightmap = cmds.symbolButton(image=icon_auto_lightmap, command="auto_lightmap()", annotation="Creates lightmap uvs using triplanar projection")
    uv_layout = cmds.symbolButton(image=icon_auto_layout, command="auto_layout()", annotation="Layout UV's automatically to a fit a 2k texture")
    uv_unfold_3d = cmds.symbolButton(image=icon_unfold_3d, command="uv_unfold_3d()", annotation="Unfold's UV using Unfold 3D")

    # Legacy unfold uv's
    uv_unfold = cmds.symbolButton(image=icon_unfold_legacy, command="uv_unfold_legacy()",
                                  annotation="Legacy unfold to unfold uv's. // Right click for options")
    cmds.popupMenu()
    cmds.menuItem(l='Unfold Both Directions', c='unfold_legacy()')
    cmds.menuItem(l='Unfold Vertical', c='unfold_vertical()')
    cmds.menuItem(l='Unfold Horizontal', c='unfold_horizontal()')

    uv_stack_uv = cmds.symbolButton(image=icon_stack_uv, command="stack_uv()", annotation="Stacks UV shells with identical surface area")

    cmds.setParent('..')

    # UV set tools
    cmds.columnLayout(rowSpacing=1, adj=True)
    conform_uvs = cmds.button(l="Conform UV Sets", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="conform_uv()", annotation='Conform UV Sets')
    delete_emp = cmds.button(l="Delete Empty UV Sets", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="delete_empty_set()",
                             annotation='Delete Empty UV Sets')
    uv_grid_subdivision = cmds.intSliderGrp("UV_Grid_Slide", l="UV Grid SubD", min=1, max=100, preventOverride=True, field=True,
                                            changeCommand="auto_grid_resize()", dragCommand="auto_grid_resize()", v=1, adj=0,
                                            columnAttach=[1, "left", 3], cw=[1, 90], annotation="Set UV Grid Subdivisions")

    cmds.rowColumnLayout(adj=True, numberOfColumns=5, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # UI buttons for setting different grid properties
    uv_grid_subd_1 = cmds.button(l="1", command="uv_grid_size_a()", w=50, bgc=[0.15, 0.15, 0.15])
    uv_grid_subd_10 = cmds.button(l="10", command="uv_grid_size_b()", w=50, bgc=[0.15, 0.15, 0.15])
    uv_grid_subd_20 = cmds.button(l="20", command="uv_grid_size_c()", w=50, bgc=[0.15, 0.15, 0.15])
    uv_grid_subd_50 = cmds.button(l="50", command="uv_grid_size_d()", w=50, bgc=[0.15, 0.15, 0.15])
    uv_grid_subd_100 = cmds.button(l="100", command="uv_grid_size_e()", w=50, bgc=[0.15, 0.15, 0.15])

    cmds.setParent('..')

    # Texel density tools
    cmds.rowLayout(nc=3, adj=True)
    cmds.textField("texel_density", h=30, w=186, pht=" Enter Map Size")
    get_texel_density = cmds.button(l="Get", bgc=[0.2, 0.2, 0.2], h=30, w=52, command="get_texel_density()",
                                    annotation='Determines the average texel density on selected objects based on a defined texture size')
    set_texel_density = cmds.button(l="Set", bgc=[0.2, 0.2, 0.2], h=30, w=52, command="set_texel_density()",
                                    annotation='Sets and matches based on a retrieved texel density value')

    cmds.setParent('..')

    cmds.rowLayout(nc=2, adj=True)
    cmds.text(label='Texel Density (px/unit)')
    cmds.textField(en=False, h=30, w=80, tx='px/m')

    cmds.setParent('..')
    cmds.rowLayout(nc=2, adj=True)
    cmds.text(label='Suggested Map Size')
    cmds.textField(en=False, h=30, w=90, tx='512px')

    cmds.setParent(uv_tools_layout)
    cmds.separator(h=1, style='none')

    # __________________________________________________________________MODELLING TOOLSET
    #
    modelling_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(l="MODELLING", cll=1, cl=0, bgc=[0.5, 0.4, 0.15])

    cmds.rowColumnLayout(numberOfColumns=6, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # Modelling section icon paths
    icon_quickcut = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_quickcut.png"
    icon_bevel = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_bevel.png"
    icon_symmetry = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_mirror.png"
    icon_boolean = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_boolean.png"
    icon_extrude = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_extrude.png"

    # Multi-cut and bevel tool
    model_quickcut = cmds.symbolButton(image=icon_quickcut, command="model_quickcut()", annotation="Activates the multi-cut tool")
    model_bevel = cmds.symbolButton(image=icon_bevel, command="model_bevel()", annotation="Applies a bevel on an object/s or edge/s")

    # Symmetry options
    model_symmetry = cmds.symbolButton(image=icon_symmetry, command="model_symmetry()", annotation="Mirror selected item. // Default is set to -z")
    cmds.popupMenu(p=model_symmetry)
    mirror_type = cmds.radioMenuItemCollection()
    cmds.menuItem("positive_x", rb=True, cl=mirror_type, l='+x')
    cmds.menuItem("negative_x", rb=True, cl=mirror_type, l='-x')
    cmds.menuItem("positive_y", rb=True, cl=mirror_type, l='+y')
    cmds.menuItem("negative_y", rb=True, cl=mirror_type, l='-y')
    cmds.menuItem("positive_z", rb=True, cl=mirror_type, l='+z')
    cmds.menuItem("negative_z", rb=True, cl=mirror_type, l='-z')

    model_boolean = cmds.symbolButton(image=icon_boolean, command="model_boolean_diff()",
                                      annotation="Activates boolean tool. // Default is set to difference")
    cmds.popupMenu()
    cmds.menuItem(label='Difference', command='model_boolean_diff()')
    cmds.menuItem(label='Intersection', command='model_boolean_intersect()')
    cmds.menuItem(label='Union', command='model_boolean_union()')
    cmds.menuItem(label='Interactive', command='model_boolean_interactive()')
    model_extrude = cmds.symbolButton(image=icon_extrude, command="model_extrude()", annotation="Activates the extrude tool.")

    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=6, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # Utilities section icon paths
    icon_connect = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_connect.png"
    icon_bridge = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_bridge.png"
    icon_detach = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_detach.png"
    icon_group = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_group.png"
    icon_transforms = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_freeze.png"

    model_connect = cmds.symbolButton(image=icon_connect, command="model_connect()", annotation="Activates the Connect tool")
    model_bridge = cmds.symbolButton(image=icon_bridge, command="model_bridge()", annotation="Bridges several edges to fill in a hole")

    model_detach = cmds.symbolButton(image=icon_detach, command="model_detach()", annotation="Detaches the currently selected faces.")
    cmds.popupMenu()
    cmds.menuItem(label='Clone', command='model_clone()')

    model_group = cmds.symbolButton(image=icon_group, command="model_group_select()",
                                    annotation="Groups the selected nodes and prompts for a group name.")
    model_freeze = cmds.symbolButton(image=icon_transforms, command="model_freeze()", annotation="Freezes transform and clears history.")
    cmds.popupMenu()
    cmds.menuItem(label='Unfreeze Transform', command='model_unfreeze_xform()')

    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=6, columnWidth=[(1, 48), (2, 48), (3, 48), (4, 48), (5, 48)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center')])

    # Deformations section icon paths
    icon_lattice = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/deform_lattice.png"
    icon_bend = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/deform_bend.png"
    icon_twist = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/deform_twist.png"
    icon_history = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_history.png"
    icon_pivot = cmds.internalVar(userPrefDir=True) + "scripts/Shuriken/Icons/model_pivot.png"

    deform_lattice = cmds.symbolButton(image=icon_lattice, command="deform_lattice()",
                                       annotation="Applies a lattice deformer to the current selection.")
    deform_bend = cmds.symbolButton(image=icon_bend, command="deform_bend()", annotation="Applies a bend deformer to the current selection.")
    deform_twist = cmds.symbolButton(image=icon_twist, command="deform_twist()", annotation="Applies a twist deformer to the current selection.")
    model_history = cmds.symbolButton(image=icon_history, command="model_history()", annotation="Clears history.")
    model_pivot = cmds.symbolButton(image=icon_pivot, command="model_center_pivot()",
                                    annotation="Center's the pivot of an object. //Right click for options")
    cmds.popupMenu()
    cmds.menuItem(label='Copy Pivot', command='model_copy_pivot()',
                  ann="Copies the pivot from one object to another. Requires two objects to be selected.")
    cmds.menuItem(label='Restore Pivot', command='model_restore_pivot()', ann="Restores the pivot xforms of an object.")

    cmds.setParent(modelling_layout)

    # __________________________________________________________________COLOUR TOOLSET
    #
    display_colour_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(l="COLOURIZE NODES", cll=1, cl=0, bgc=[0.349, 0.057, 0.159])

    cmds.rowColumnLayout(height=23, numberOfColumns=10,
                         columnWidth=[(1, 23), (2, 23), (3, 23), (4, 23), (5, 23), (6, 23), (7, 23), (8, 23), (9, 23), (10, 23)],
                         columnAlign=[(1, 'center'), (2, 'center'), (3, 'center'), (4, 'center'), (5, 'center'), (6, 'center'), (7, 'center'),
                                      (8, 'center'), (9, 'center'), (10, 'center')])

    display_red = cmds.button(l="", command="", h=23, w=23, bgc=[1.00, 0.224, 0.224])
    display_peach = cmds.button(l="", command="", h=23, w=23, bgc=[1.00, 0.399, 0.321])
    display_orange = cmds.button(l="", command="", h=23, w=23, bgc=[1.00, 0.479, 0.173])
    display_yellow = cmds.button(l="", command="", h=23, w=23, bgc=[1.00, 1.00, 0.390])
    display_green = cmds.button(l="", command="", h=23, w=23, bgc=[0.527, 1.00, 0.276])
    display_aqua = cmds.button(l="", command="", h=23, w=23, bgc=[0.321, 1.00, 0.869])
    display_blue = cmds.button(l="", command="", h=23, w=23, bgc=[0.256, 0.628, 1.0])
    display_pink = cmds.button(l="", command="", h=23, w=23, bgc=[1.0, 0.442, 0.706])
    display_purple = cmds.button(l="", command="", h=23, w=23, bgc=[0.763, 0.332, 0.892])
    display_indigo = cmds.button(l="", command="", h=23, w=23, bgc=[0.466, 0.200, 0.892])

    cmds.setParent('..')

    cmds.rowLayout(nc=3, adj=True)
    cmds.button(l="Select", w=75, bgc=[0.15, 0.15, 0.15], c="", ann='Selects object in the scene that use the same display colour.')
    cmds.button(l="Apply", w=75, bgc=[0.15, 0.15, 0.15], c="",
                ann='Applies a colour override to the currently selected node in the outliner and attaches those nodes to a display layer.')
    cmds.button(l="Reset", w=75, bgc=[0.15, 0.15, 0.15], c="", ann='Resets the current selected outliner nodes to the default colour setting')

    cmds.setParent('..')

    cmds.columnLayout(rowSpacing=1, adj=True)
    add_display_layer = cmds.button(l="Add to Display Layer", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="add_to_display()",
                                    annotation='Add current selection to display layer')
    remove_display_layer = cmds.button(l="Remove from Display Layer", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="remove_from_display()",
                                       annotation='Remove current selection from display layer')

    cmds.setParent(display_colour_layout)

    # __________________________________________________________________CLEANUP TOOLSET
    #
    cleanup_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(l="CLEANUP", cll=1, cl=0, bgc=[0.1, 0.3, 0.47])

    cmds.columnLayout(rowSpacing=1, adj=True)
    fix_orphan_nodes = cmds.button(l="Fix Orphan Shape Nodes", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="clear_orphan_shape()",
                                   annotation='Clear out orphan shape nodes')
    remove_pasted = cmds.button(l="Remove pasted__", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="remove_pasted()",
                                annotation='Remove pasted__ from scene nodes')
    clear_unused_transforms = cmds.button(l="Remove Empty Transforms", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="clean_transforms()",
                                          annotation='Remove unused transforms')
    clear_unused_shaders = cmds.button(l="Remove Unused Materials", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="clear_unused_materials()",
                                       annotation='Delete unused materials')
    validate = cmds.button(l="Validate Asset", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="validator()",
                           annotation='Runs the scene through a validator and checkes for any potential errors')

    cmds.setParent(cleanup_layout)

    # __________________________________________________________________EXPORT TOOLS
    #
    export_layout = cmds.columnLayout(adj=True)
    section_frame_layout = cmds.frameLayout(l="EXPORT", cll=1, cl=0, bgc=[0.356, 0.47, 0.3])

    cmds.rowLayout(nc=3, adj=True)
    cmds.button(l="All", w=75, bgc=[0.15, 0.15, 0.15], c="export_all()")
    cmds.button(l="Selection", w=75, bgc=[0.15, 0.15, 0.15], c="export_select()")
    cmds.button(l="Last", w=75, bgc=[0.15, 0.15, 0.15], c="export_last")

    cmds.setParent('..')

    cmds.columnLayout(rowSpacing=1, adj=True)
    open_export_folder = cmds.button(l="Open Export Folder", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="open_export_folder()",
                                     annotation='Opens the Export Folder')
    set_export_location = cmds.button(l="Set Export Location", bgc=[0.2, 0.2, 0.2], h=30, w=130, command="set_export_location()",
                                      annotation='Set the export location')

    cmds.setParent(export_layout)


cmds.workspaceControl("Shuriken", retain=False, floating=True, li=True, uiScript="UI()")


# INFO Message
def info_update(debug_log, _=False):
    cmds.text('Log', e=True, l='  %s' % debug_log)


# PRIMITIVES
def create_sphere():
    selection = cmds.ls(sl=True)
    if selection == []:
        sphere_object = cmds.polySphere(radius=100, subdivisionsX=20, subdivisionsY=12, axis=[0, 0, 1], createUVs=2, constructionHistory=1,
                                        name='sphere_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(sphere_object)
        mel.eval("setToolTo ShowManips;")

    else:
        mel.eval("setToolTo $gMove;")
        sphere_object = cmds.polySphere(radius=100, subdivisionsX=20, subdivisionsY=12, axis=[0, 0, 1], createUVs=2, constructionHistory=1,
                                        name='sphere_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(sphere_object)
        mel.eval("setToolTo ShowManips;")


def create_cube():
    selection = cmds.ls(sl=True)
    if selection == []:
        cube_object = cmds.polyCube(width=100, height=100, depth=100, sx=1, sy=1, sz=1, axis=[0, 0, 1], createUVs=4, constructionHistory=1,
                                    name='cube_001')
        cmds.select(cube_object)
        mel.eval("setToolTo ShowManips;")

    else:
        mel.eval("setToolTo $gMove;")
        cube_object = cmds.polyCube(width=100, height=100, depth=100, sx=1, sy=1, sz=1, axis=[0, 0, 1], createUVs=4, constructionHistory=1,
                                    name='cube_001')
        cmds.select(cube_object)
        mel.eval("setToolTo ShowManips;")


def create_cylinder_x():
    selection = cmds.ls(sl=True)
    if selection == []:
        cylinder_object = cmds.polyCylinder(radius=100, height=200, sy=1, sz=0, axis=[1, 0, 0], sc=1, createUVs=3, constructionHistory=1,
                                            subdivisionsAxis=24, name='cylinder_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(cylinder_object)
        mel.eval("setToolTo ShowManips;")

    else:
        mel.eval("setToolTo $gMove;")
        cylinder_object = cmds.polyCylinder(radius=100, height=200, sy=1, sz=0, axis=[1, 0, 0], sc=1, createUVs=3, constructionHistory=1,
                                            subdivisionsAxis=24, name='cylinder_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(cylinder_object)
        mel.eval("setToolTo ShowManips;")


def create_cylinder_y():
    selection = cmds.ls(sl=True)
    if selection == []:
        cylinder_object = cmds.polyCylinder(radius=100, height=200, sy=1, sz=0, axis=[0, 1, 0], sc=1, createUVs=3, constructionHistory=1,
                                            subdivisionsAxis=24, name='cylinder_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(cylinder_object)
        mel.eval("setToolTo ShowManips;")

    else:
        mel.eval("setToolTo $gMove;")
        cylinder_object = cmds.polyCylinder(radius=100, height=200, sy=1, sz=0, axis=[0, 1, 0], sc=1, createUVs=3, constructionHistory=1,
                                            subdivisionsAxis=24, name='cylinder_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(cylinder_object)
        mel.eval("setToolTo ShowManips;")


def create_cylinder_z():
    selection = cmds.ls(sl=True)
    if selection == []:
        cylinder_object = cmds.polyCylinder(radius=100, height=200, sy=1, sz=0, axis=[0, 0, 1], sc=1, createUVs=3, constructionHistory=1,
                                            subdivisionsAxis=24, name='cylinder_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(cylinder_object)
        mel.eval("setToolTo ShowManips;")

    else:
        mel.eval("setToolTo $gMove;")
        cylinder_object = cmds.polyCylinder(radius=100, height=200, sy=1, sz=0, axis=[0, 0, 1], sc=1, createUVs=3, constructionHistory=1,
                                            subdivisionsAxis=24, name='cylinder_001')
        cmds.polySoftEdge(angle=45, constructionHistory=1)
        cmds.select(cylinder_object)
        mel.eval("setToolTo ShowManips;")


def create_plane_x():
    selection = cmds.ls(sl=True)
    if selection == []:
        plane_object = cmds.polyPlane(width=100, height=100, sx=1, sy=1, axis=[1, 0, 0], createUVs=2, constructionHistory=1, name='plane_001')
        cmds.select(plane_object)
        mel.eval("setToolTo ShowManips;")



    else:
        mel.eval("setToolTo $gMove;")
        plane_object = cmds.polyPlane(width=100, height=100, sx=1, sy=1, axis=[1, 0, 0], createUVs=2, constructionHistory=1, name='plane_001')
        cmds.select(plane_object)
        mel.eval("setToolTo ShowManips;")


def create_plane_y():
    selection = cmds.ls(sl=True)
    if selection == []:
        plane_object = cmds.polyPlane(width=100, height=100, sx=1, sy=1, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='plane_001')
        cmds.select(plane_object)
        mel.eval("setToolTo ShowManips;")



    else:
        mel.eval("setToolTo $gMove;")
        plane_object = cmds.polyPlane(width=100, height=100, sx=1, sy=1, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='plane_001')
        cmds.select(plane_object)
        mel.eval("setToolTo ShowManips;")


def create_plane_z():
    selection = cmds.ls(sl=True)
    if selection == []:
        plane_object = cmds.polyPlane(width=100, height=100, sx=1, sy=1, axis=[0, 0, 1], createUVs=2, constructionHistory=1, name='plane_001')
        cmds.select(plane_object)
        mel.eval("setToolTo ShowManips;")



    else:
        mel.eval("setToolTo $gMove;")
        plane_object = cmds.polyPlane(width=100, height=100, sx=1, sy=1, axis=[0, 0, 1], createUVs=2, constructionHistory=1, name='plane_001')
        cmds.select(plane_object)
        mel.eval("setToolTo ShowManips;")


def create_torus():
    selection = cmds.ls(sl=True)
    if selection == []:
        torus_object = cmds.polyTorus(radius=100, sectionRadius=50, sx=20, sy=20, axis=[0, 0, 1], createUVs=2, constructionHistory=1,
                                      name='torus_001')
        cmds.select(torus_object)
        mel.eval("setToolTo ShowManips;")



    else:
        mel.eval("setToolTo $gMove;")
        torus_object = cmds.polyTorus(radius=100, sectionRadius=50, sx=20, sy=20, axis=[0, 0, 1], createUVs=2, constructionHistory=1,
                                      name='torus_001')
        cmds.select(torus_object)
        mel.eval("setToolTo ShowManips;")

    # GRID


# Auto resizes the viewport grid using a slider
def auto_grid_resize():
    grid_subd_weight = cmds.intSliderGrp("Grid_Slide", q=True, value=True)
    cmds.grid(size='2000', spacing='100', divisions=grid_subd_weight)


# Grid preset with 1 division
def grid_size_a():
    cmds.grid(size='2000', spacing='100', divisions=1)


# Grid preset with 10 division
def grid_size_b():
    cmds.grid(size='2000', spacing='100', divisions=10)


# Grid preset with 20 division
def grid_size_c():
    cmds.grid(size='2000', spacing='100', divisions=20)


# Grid preset with 50 division
def grid_size_d():
    cmds.grid(size='2000', spacing='100', divisions=50)


# Grid preset with 100 division
def grid_size_e():
    cmds.grid(size='2000', spacing='100', divisions=100)


# RENAME


# Function for adding a prefix


# Function for adding a suffix


# Search field for identifying a sequence of string characters based on user input


# replace field for setting the strgin we want to replace it with


# Actives and renames a string based on the search & replace field


# Find transform & mesh nodes in the scene that are duplicate names and makes them unique


# Conforms the names to convention and add's underscores where applicable


# Formats the names of selected nodes to the lowercase


# QUICK MATERIALS
def lambert1():
    cmds.hyperShade(assign="lambert1")


def green_lambert():
    selection = cmds.ls(sl=True)
    if cmds.objExists('green_lambert'):
        cmds.hyperShade(assign="green_lambert")
    else:
        LambertGreen = cmds.shadingNode("lambert", asShader=True)
        cmds.setAttr(LambertGreen + ".color", 0.0, 0.798, 0.292, type='double3')
        cmds.rename("green_lambert")
        cmds.select(selection)
        cmds.hyperShade(assign="green_lambert")


def red_lambert():
    selection = cmds.ls(sl=True)
    if cmds.objExists('red_lambert'):
        cmds.hyperShade(assign="red_lambert")
    else:
        LambertRed = cmds.shadingNode("lambert", asShader=True)
        cmds.setAttr(LambertRed + ".color", 0.7, 0.011, 0.011, type='double3')
        cmds.rename("red_lambert")
        cmds.select(selection)
        cmds.hyperShade(assign="red_lambert")


def blue_lambert():
    selection = cmds.ls(sl=True)
    if cmds.objExists('blue_lambert'):
        cmds.hyperShade(assign="blue_lambert")
    else:
        LambertBlue = cmds.shadingNode("lambert", asShader=True)
        cmds.setAttr(LambertBlue + ".color", 0, 0.432, 0.7, type='double3')
        cmds.rename("blue_lambert")
        cmds.select(selection)
        cmds.hyperShade(assign="blue_lambert")


def yellow_lambert():
    selection = cmds.ls(sl=True)
    if cmds.objExists('yellow_lambert'):
        cmds.hyperShade(assign="yellow_lambert")
    else:
        LambertYellow = cmds.shadingNode("lambert", asShader=True)
        cmds.setAttr(LambertYellow + ".color", 0.9, 0.450, 0.0, type='double3')
        cmds.rename("yellow_lambert")
        cmds.select(selection)
        cmds.hyperShade(assign="yellow_lambert")


def dark_grey_lambert():
    selection = cmds.ls(sl=True)
    if cmds.objExists('dark_grey_lambert'):
        cmds.hyperShade(assign="dark_grey_lambert")
    else:
        LambertGreyDark = cmds.shadingNode("lambert", asShader=True)
        cmds.setAttr(LambertGreyDark + ".color", 0.05, 0.05, 0.05, type='double3')
        cmds.rename("dark_grey_lambert")
        cmds.select(selection)
        cmds.hyperShade(assign="dark_grey_lambert")


def select_assigned_default_lambert():
    if cmds.objExists('lambert1'):
        cmds.hyperShade(objects="lambert1")
    else:
        print ("Please First Create this FaceColor Shader")


def select_assigned_green_lambert():
    if cmds.objExists('green_lambert'):
        cmds.hyperShade(objects="green_lambert")
    else:
        print ("Please First Create this FaceColor Shader")


def select_assigned_red_lambert():
    if cmds.objExists('red_lambert'):
        cmds.hyperShade(objects="red_lambert")
    else:
        print ("Please First Create this FaceColor Shader")


def select_assigned_blue_lambert():
    if cmds.objExists('blue_lambert'):
        cmds.hyperShade(objects="blue_lambert")
    else:
        print ("Please First Create this FaceColor Shader")


def select_assigned_yellow_lambert():
    if cmds.objExists('yellow_lambert'):
        cmds.hyperShade(objects="yellow_lambert")
    else:
        print ("Please First Create this FaceColor Shader")


def select_assigned_dark_grey_lambert():
    if cmds.objExists('dark_grey_lambert'):
        cmds.hyperShade(objects="dark_grey_lambert")
    else:
        print ("Please First Create this FaceColor Shader")


def green_material_transparency():
    if cmds.objExists('green_lambert'):
        cmds.window(title='Green Transparency')
        cmds.columnLayout()
        cmds.attrColorSliderGrp(at='green_lambert.transparency')
        cmds.showWindow()
    else:
        print ("Please First Create this FaceColor Shader")


def select_green_lambert():
    if cmds.objExists('green_lambert'):
        cmds.select('green_lambert')
    else:
        print ("Please First Create this FaceColor Shader")


def default_material_transparency():
    if cmds.objExists('lambert1'):
        cmds.window(title='Lambert Transparency')
        cmds.columnLayout()
        cmds.attrColorSliderGrp(at='lambert1.transparency')
        cmds.showWindow()
    else:
        print ("Please First Create this FaceColor Shader")


def select_default_lambert():
    if cmds.objExists('lambert1'):
        cmds.select('lambert1')
    else:
        print ("Please First Create this FaceColor Shader")


def red_material_transparency():
    if cmds.objExists('red_lambert'):
        cmds.window(title='Red Transparency')
        cmds.columnLayout()
        cmds.attrColorSliderGrp(at='red_lambert.transparency')
        cmds.showWindow()
    else:
        print ("Please First Create this FaceColor Shader")


def select_red_lambert():
    if cmds.objExists('red_lambert'):
        cmds.select('red_lambert')
    else:
        print ("Please First Create this FaceColor Shader")


def blue_material_transparency():
    if cmds.objExists('blue_lambert'):
        cmds.window(title='Blue Transparency')
        cmds.columnLayout()
        cmds.attrColorSliderGrp(at='blue_lambert.transparency')
        cmds.showWindow()
    else:
        print ("Please First Create this FaceColor Shader")


def select_blue_lambert():
    if cmds.objExists('blue_lambert'):
        cmds.select('blue_lambert')
    else:
        print ("Please First Create this FaceColor Shader")


def yellow_material_transparency():
    if cmds.objExists('yellow_lambert'):
        cmds.window(title='Yellow Transparency')
        cmds.columnLayout()
        cmds.attrColorSliderGrp(at='yellow_lambert.transparency')
        cmds.showWindow()
    else:
        print ("Please First Create this FaceColor Shader")


def select_yellow_lambert():
    if cmds.objExists('yellow_lambert'):
        cmds.select('yellow_lambert')
    else:
        print ("Please First Create this FaceColor Shader")


def dark_grey_material_transparency():
    if cmds.objExists('dark_grey_lambert'):
        cmds.window(title='GreyDark Transparency')
        cmds.columnLayout()
        cmds.attrColorSliderGrp(at='dark_grey_lambert.transparency')
        cmds.showWindow()
    else:
        print ("Please First Create this FaceColor Shader")


def select_dark_grey_lambert():
    if cmds.objExists('dark_grey_lambert'):
        cmds.select('dark_grey_lambert')
    else:
        print ("Please First Create this FaceColor Shader")

    # Function for opening up the Hypershade


def open_hypershade():
    mel.eval("HypershadeWindow;")


# Function for deleting unused material nodes
def clear_unused_materials():
    delete_unused = cmds.textScrollList("material_list", q=True, si=True)
    cmds.select(delete_unused)
    mel.eval('MLdeleteUnused;')
    list_materials()
    info_update("Unused materials have been nuked.")


# Function for selecting object with the same currently highlighted material
def select_similar(_=False):
    assigned_material = cmds.textScrollList("material_list", q=True, si=True)
    if assigned_material == None:
        info_update('No materials selected')
    elif len(assigned_material) > 1:
        info_update('Please select only one material.')
    else:
        cmds.hyperShade(objects="%s" % assigned_material[0])
        get_total_faces = cmds.polyEvaluate(fc=True)
        get_shaded_objects = cmds.ls(sl=True)
        if len(get_shaded_objects) == 0:
            info_update('No matches found.')
        else:
            shaded_faces = []
            for f in get_shaded_objects:
                if "f[" in f:
                    shaded_faces.append(f)

            if len(shaded_faces) == 0:
                info_update("Found %s object(s)." % len(get_shaded_objects))



            else:
                info_update("Found %s object(s) and %s face(s)." %
                            (len(get_shaded_objects) - len(shaded_faces), get_total_faces))


# Apply a checkered grid texture to the current selection
def apply_checkered(_=False):
    pass


# Conforms the material names to include an mi_ prefix
def material_conform(_=False):
    pass


# Replaces any pasted__ in the material name with mi_
def replace_pasted_material(_=False):
    fix_pasted_materials = cmds.ls(mat=True)
    for i in fix_pasted_materials:
        if 'pasted__' in i:
            fix_prefix = i.replace("pasted__", "mi_")
            cmds.rename(i, fix_prefix)
        else:
            pass

    list_materials()
    info_update("Pasted__ removed from materials")


# Appends mi_ prefix to the material name if it doesn't exist
def append_mi(_=False):
    fix_pasted_materials = cmds.ls(mat=True)
    for i in fix_pasted_materials:
        if 'pasted__' in i:
            fix_prefix = i.replace("pasted__", "mi_")
            cmds.rename(i, fix_prefix)
        else:
            pass

    list_materials()
    info_update("mi_ prefix added")


def list_materials(_=False):
    materials_list = cmds.ls(mat=True)
    materials_list.sort()
    material_list_update = cmds.textScrollList("material_list", q=True, ni=True)
    if material_list_update > 0:
        debug_log = "List updated."
    else:
        debug_log = ""
    cmds.textScrollList("material_list", e=True, ra=True)
    for i in materials_list:
        if i == "particleCloud1":
            continue
        else:
            cmds.textScrollList("material_list", e=True, a=(i))
            info_update(" %s %s material(s) found." % (debug_log, (len(materials_list) - 1)))


def select_material(_=False):
    material_select = cmds.textScrollList("material_list", q=True, si=True)
    if material_select == None:
        info_update('Please select a material from the list.')
    elif len(material_select) > 1:
        pass
    else:
        cmds.select(material_select)
        mel.eval('AttributeEditor;')


def material_rename(_=False):
    material_rename_select = cmds.textScrollList("material_list", q=True, si=True)
    if material_rename_select == None:
        info_update('Please select a shader from the list.')
    elif len(material_rename_select) > 1:
        info_update('Please select only one shader.')
    elif material_rename_select[0] == "lambert1":
        info_update("'lambert1' cannot be renamed!")
    elif material_rename_select[0] == "standardSurface1":
        info_update("'standardSurface1' cannot be renamed!")
    else:
        material_rename_dialog = cmds.promptDialog(
            title='Rename', message='Enter new name:', button=['OK', 'Cancel'],
            defaultButton='OK', cancelButton='Cancel', dismissString='Cancel', tx=("%s" % material_rename_select[0]))
        if material_rename_dialog == 'OK':
            material_name_replace = cmds.promptDialog(query=True, text=True)
            cmds.rename(material_rename_select, material_name_replace)
            list_materials()


def material_delete(_=False):
    delete_materials_list = cmds.textScrollList("material_list", q=True, si=True)
    if delete_materials_list == None:
        info_update('Please select a shader from the list.')
    else:
        for i in delete_materials_list:
            fix_shading_group_names()

        for i in delete_materials_list:
            if i == "lambert1":
                info_update("You cannot delete 'lambert1'.")
                continue
            elif i == "standardSurface1":
                info_update("You cannot delete 'standardSurface1'.")
                continue
            else:
                delete_shading_group = cmds.listConnections(i, type='shadingEngine')
                cmds.hyperShade(objects="%s" % delete_shading_group[0])
                select_deleting_material = cmds.ls(sl=True)

                if len(select_deleting_material) > 0:
                    for k in select_deleting_material:
                        cmds.sets(e=True, fe='initialParticleSE')

                cmds.select(i)
                cmds.delete()
                cmds.delete(delete_shading_group[0])

                list_materials()

                info_update("Deleted Shader(s).")


# Fix shadingGroup names
def fix_shading_group_names(_=False):
    sg_material_list = cmds.textScrollList("material_list", q=True, si=True)
    for i in sg_material_list:
        if i == "lambert1" or i == "particleCloud1":
            continue
        else:
            try:
                shading_groups = cmds.listConnections(i, type='shadingEngine')
                cmds.rename(shading_groups[0], "%sSG" % i)
            except:
                cmds.sets(r=True, nss=True, em=True, name="%sSG" % i)
                cmds.defaultNavigation(ce=True, s="%s" % i, d="%sSG" % i)

    info_update("Fixed SG Names.")


def materials_assign(_=False):
    assignSha = cmds.textScrollList("material_list", q=True, si=True)
    if len(cmds.ls(sl=True, tr=True)) == 0:
        info_update("Please select an object.")
    elif assignSha == None:
        info_update('Please select a shader from the list.')
    elif assignSha[0] == "lambert1":
        cmds.sets(e=True, fe='initialShadingGroup')
        info_update("Assigned '%s'." % assignSha[0])
    elif len(assignSha) > 1:
        info_update('Please select only one shader.')
    else:
        cmds.hyperShade(a="%s" % assignSha[0])

        info_update("Assigned '%s'." % assignSha[0])


def materials_duplicate(_=False):
    dup_material_list = cmds.textScrollList("material_list", q=True, si=True)
    if dup_material_list == None:
        info_update('Please select a shader from the list.')
    elif dup_material_list[0] == 'lambert1':
        info_update("You cannot duplicate 'lambert1'.")
    else:
        cmds.select(dup_material_list)
        cmds.hyperShade(dup=True)
        list_materials()
        info_update("Duplicated Shader(s).")


def make_custom_material(_=False):
    pass


def project_planar():
    pass


# MODELLING
def model_quickcut():
    mel.eval('dR_multiCutTool;')


def model_bevel():
    mel.eval('performBevelOrChamfer;')


def model_symmetry():
    pass


def model_boolean_diff():
    pass


def model_boolean_intersect():
    pass


def model_boolean_union():
    pass


def model_boolean_interactive():
    pass


def model_extrude():
    mel.eval('performPolyExtrude 0;')


def model_connect():
    mel.eval('dR_connectTool;')


def model_bridge():
    mel.eval('performPolyBridgeEdge 0;')


def model_detach():
    pass


def model_clone():
    pass


def model_group_select():
    pass


def model_group_name():
    pass


def model_group_kit():
    pass


def model_reset_xform():
    selection = cmds.ls(sl=True)
    for s in selection:
        cmds.makeIdentity(apply=True)
        mel.eval('CenterPivot;')
        cmds.delete(ch=True)


def model_freeze():
    selection = cmds.ls(sl=True)
    for s in selection:
        cmds.makeIdentity(s, apply=True)
        cmds.delete(s, ch=True)


def model_history():
    selection = cmds.ls(sl=True)
    for s in selection:
        cmds.delete(s, ch=True)


def model_center_pivot():
    selection = cmds.ls(sl=True)
    for s in selection:
        mel.eval('CenterPivot;')


# COLOURIZE


# CLEAN UP
def clear_orphan_shape(_=False):
    for sel in pm.selected():
        for intermediate_obj in [s for s in sel.getShapes() if s.intermediateObject.get()]:
            if len(intermediate_obj.connections()) == 0:
                print("Deleting..." + intermediate_obj)
                pm.delete(intermediate_obj)
                pm.select(clear=True)
    print("Orphan shape node deleted!")


def remove_pasted(_=False):
    fix_pasted = cmds.ls(tr=True, g=True, s=True)
    for pasted in fix_pasted:
        if 'pasted__' in pasted:
            fix_prefix_nodes = pasted.replace("pasted__", "")
            cmds.rename(pasted, fix_prefix_nodes)
        else:
            pass
    info_update("pasted__ removed from nodes")


def clean_transforms():
    pass


def validator():
    pass

# EXPORT