import unreal
import sys
import os

'''
資産名とパスを照会するための一連の小さなスニペット
'''

MESH = 'Mesh01'
DIR_PATH = '/Game/'
actors = unreal.EditorLevelLibrary.get_selected_level_actors()

# Print paths
def print_py_path():
    '''
    Prints all the Unreal Py paths
    NOTE: Not all paths printed exists on disk
    '''
    for path in sys.path:
        print (path)

# AssetData構造体全体を印刷します。
def printAssetData():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print (asset)

# 資産名だけを印刷します。
def printAssetName():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print (asset.asset_name)

# 資産クラスタイプを印刷します。
def printAssetClass():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print (asset.asset_class)
    
# DIR_PATHにuassetsのパッケージパスを印刷します。
def printPackagePath():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print (asset.package_path)

# DIR_PATHにuassetsのパッケージ名を印刷します。
def printPackageName():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print (asset.package_name)

# DIR_PATHに各uassetのオブジェクトパスを印刷します。
def printObjectPath():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print (asset.object_path)

# 特定のクラスタイプに基づいて資産名を印刷する.
def listAssets():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for m in assets:
        material_class = str(m.asset_class)
        if material_class == 'MaterialInstanceConstant':
                print (m.asset_name)

# Get Static Mesh Assets
def getMeshes():
    static_meshes = []
    static_mesh_components = []
    for actor in actors:
        mesh_comp = actor.get_components_by_class(unreal.StaticMeshComponent)
        for mesh in mesh_comp:
            static_mesh_components.append(mesh)
            sm = mesh.get_editor_property("StaticMesh")
            if unreal.StaticMesh.cast(sm):
                static_meshes.append(sm)
            else:
                print ("cast to static mesh failed")
    return [static_meshes, static_mesh_components]


# Get the material and material instances information
def getMaterialInstances():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    material_assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    materialsList = []
    for m in material_assets:
        material_class = str(m.asset_class)
        if material_class == "MaterialInstanceConstant" or material_class == "Material":
            materialsList.append(m)
        elif material_class == "Material":
            materialsList.append(m)
        else:
            pass
    return materialsList

# Gets the material slot names on the selected actors
def getMaterialSlotInformation():
    mesh_component = getMeshes()
    material_information = []
    for smc in mesh_component[1]:
        material_slot = smc.get_material_slot_names()
        for slot_name in material_slot:
            slot_index = str(smc.get_material_index(slot_name))
            material_dict = dict(index=slot_index, name=str(slot_name))

            material_information.append(material_dict)

    return material_information

# Get mesh by name
def get_mesh_by_name(asset_name=MESH):
    obj_path = []
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    asset_dict = []
    for asset in assets:
        if asset_name in str(asset.asset_name):
            obj_path = asset.object_path
    return obj_path

def print_py_path():
    '''
    Prints all the Unreal Py paths
    NOTE: Not all paths printed exists on disk
    '''
    for path in sys.path:
        print (path)


def start_file():
    '''
    Starts a file with an associated program.
    NOTE: In this scenario, the path entered does not exists on disk.
    A directory will be created but there is no file on disk to start.
    Creating a file & restarting the engine will solve the issue
    '''
    os.startfile("")


def log_to_unreal():
    '''
    Prints something to unreals output log
    '''
    unreal.log('Log: ')


def log_warning_to_unreal():
    '''
    Prints something to unreals output log
    '''
    unreal.log_warning('Warning: ')


def makeDirs():
    '''
    Makes a directory at the specified path
    '''
    os.makedirs("../../")