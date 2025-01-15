"""
Spawns a material preview mesh for every material in the library
"""

import unreal

# unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor.static_class(), unreal.Vector(0, 0, 0),
# #unreal.Rotator(0, 0, 0))

PREVIEW_MESH = 'SM_MatPreviewMesh_02_Automotive'
DIR_PATH = "/Game/A02_Materials/Utilities/MaterialSphere/"
MAT_PATH = "/Game/A02_Materials/Materials/Instances/"


# Get the material and material instances needed for assignment
def get_material_instances():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    material_assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    materials_list = []

    # Iterating over each item in DIR_PATH to see if it's a Material or Material Instance that we can apply
    for m in material_assets:
        material_class = str(m.asset_class)
        # Add a valid material type to an empty list
        if material_class == 'MaterialInstanceConstant' or material_class == 'Material':
            materials_list.append(m)
        else:
            pass
    return materials_list


# Get mesh by name
def get_mesh_by_name(asset_name=PREVIEW_MESH):
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    asset_dict = []
    for asset in assets:
        if asset_name in str(asset.asset_name):
            obj_path = asset.object_path
    return obj_path


# Spawns an actor of static mesh class for every material in our library
def spawn_preview_mesh():
    materials = get_material_instances()
    material_asset_name = [str(m.asset_name) for m in materials]
    material_paths = [str(m.object_path) for m in materials]
    material_dictionary = sorted(dict(zip(material_asset_name, material_paths)), reverse=True)
    mesh = get_mesh_by_name()

    with unreal.ScopedSlowTask(len(material_dictionary), 'Spawning meshes... ') as slow_task:
        slow_task.make_dialog(True)
        for x in range(len(material_dictionary)):
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1, 'Assigning meshes... ' + str(x) + ' / ' + str(len(material_dictionary)))
            # unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor.static_class(), unreal.Vector(
            # 0, 0, 0), unreal.Rotator(0, 0, 0))
    for d in material_dictionary:
        print(d)


# Assigns our static mesh to the actors

# Assigns materials to our static meshes

# getMeshByName(asset_name=PREVIEW_MESH)
spawn_preview_mesh()
