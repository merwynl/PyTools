"""
Test script that assigns materials to selected static meshes based on their slot names
"""

import unreal
import json

DIR_PATH = "/Game/A01_General/materials/"
material_list = "S:/logs/json/material.json"

# Get Selected actor
actors = unreal.EditorLevelLibrary.get_selected_level_actors()


def getMeshes():
    static_meshes = []
    static_mesh_components = []

    # Gets the selected actors in the scene
    for actor in actors:

        # Get static mesh component
        mesh_comp = actor.get_components_by_class(unreal.StaticMeshComponent)

        # Iterating over each static mesh component
        for mesh in mesh_comp:

            # Adding each static mesh component to a list
            static_mesh_components.append(mesh)

            # We need to cast to static mesh in order to get access to the set_material function
            sm = mesh.get_editor_property("StaticMesh")
            if unreal.StaticMesh.cast(sm):
                static_meshes.append(sm)
            else:
                print ("cast to static mesh failed")
    return [static_meshes, static_mesh_components]


# Get the material and material instances needed for assignment
def getMaterialInstances():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    material_assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    materialsList = []

    # Iterating over each item in DIR_PATH to see if it's a Material or Material Instance that we can apply
    for m in material_assets:
        material_class = str(m.asset_class)
        # Add a valid material type to an empty list
        if material_class == "MaterialInstanceConstant" or material_class == "Material":
            materialsList.append(m)
        elif material_class == "Material":
            materialsList.append(m)
        else:
            pass
    return materialsList


# Gets the material slot names on the selected actors
def getMaterialSlotInformation():
    # Gets the static meshes that we want
    mesh_component = getMeshes()

    # Empty lists and dictionaries for storing material information
    material_dict = {}
    material_information = []

    # Get the material slot name & index of the static mesh component that we want to assign our materials to
    for smc in mesh_component[1]:

        # Get material slot names
        material_slot = smc.get_material_slot_names()
        for slot_name in material_slot:

            # Gets the material slot index
            slot_index = str(smc.get_material_index(slot_name))

            # Stores the material index & slot name inside a dictionary to be referenced
            material_dict = dict(index=slot_index, name=str(slot_name))

            # We append our dicionary to an empty list so that we can iterate over each item
            material_information.append(material_dict)

    return material_information


# Assigns materials on the selected actors.
def setMaterialBySlotName():

    # Gets all materials instances & material slot info dict
    materials = getMaterialInstances()
    slot_info = getMaterialSlotInformation()

    # Collects the name of our materials and their paths
    material_asset_name = [str(m.asset_name) for m in materials]
    material_paths = [str(m.object_path) for m in materials]

    # Create a dictionary from two lists with the material name used as the key
    material_dictionary = dict(zip(material_asset_name, material_paths))

    # Dumps dictionary into a json file
    # with open(material_list, "w") as write_file:
    # json.dump(material_dictionary, write_file, sort_keys=True, indent=4)

    # Retrieves the value information for each slot
    material_slot_values = [v.values() for v in slot_info]

    # Begins a slow task dialog box for unique material slot
    with unreal.ScopedSlowTask(len(material_slot_values)) as slow_task:
        slow_task.make_dialog(True)
        for x in range(len(material_slot_values)):
            # Add an option to cancel out of the material assignment
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(
                1,
                "Assigning materials to slots... "
                + str(x)
                + " / "
                + str(len(material_slot_values)),
            )
            for v in material_slot_values:
                material_index = v[0]
                material_name = v[1]
                # Runs a check to find a match material in our library
                if material_name in material_dictionary:

                    # Collects  our static mesh
                    static_mesh = getMeshes()
                    mesh = static_mesh[0]
                    # print 'found ' + material_name

                    # Sets the material path for our material
                    material_path = material_dictionary[material_name]

                    # Iterates over each static mesh, takes our material slot info, and sets the material
                    for d in mesh:
                        mesh_path = d.get_full_name()
                        mesh_example = unreal.EditorAssetLibrary.load_asset(mesh_path)
                        material_example = unreal.EditorAssetLibrary.load_asset(
                            material_path
                        )
                        mesh_example.set_material(int(material_index), material_example)
                else:
                    pass
                    print ("no matches found")


setMaterialBySlotName()
