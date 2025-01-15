import unreal

DIR_PATH = "\\Game\\ProjectName\\"

# Get Selected actor
actors = unreal.EditorLevelLibrary.get_selected_level_actors()


def get_meshes():
    static_meshes = []
    static_mesh_components = []

    # Gets the selected actors in the scene
    for actor in actors:

        # Get static mesh component
        mesh_comp = actor.get_components_by_class(unreal.StaticMeshComponent)

        # Iterating over each static mesh component
        for mesh in mesh_comp:

            # Adding each iteration item to a list
            static_mesh_components.append(mesh)

            # We need to cast tp a static mesh in order to get access to the set_material function
            sm = mesh.get_editor_property("StaticMesh")
            if unreal.StaticMesh.cast(sm):
                static_meshes.append(sm)
            else:
                print("nope")
                pass
    return [static_meshes, static_mesh_components]


# Get the materials needed for assignment
def get_material_instances():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    material_assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    materials_list = []

    # Iterating over each item in DIR_PATH to see if it's a Material or Material Instance that we can apply
    for m in material_assets:
        material_class = str(m.asset_class)

    # Add a valid material type to an empty list
    if material_class == "MaterialInstanceConstant" or material_class == "Material":
        materials_list.append(m)
    else:
        pass
    return materials_list


# # Gets the material slot names on the selected actors
def get_material_slot_information():
    mesh_component = get_meshes()
    material_dict = {}
    print(material_dict)
    material_information = []
    # Get the material slot name & index of the static mesh component to apply the material to
    for smc in mesh_component[1]:
        # Get material slot names
        material_slot = smc.get_material_slot_names()
        for slot_name in material_slot:
            # Gets the material slot index
            slot_index = str(smc.get_material_index(slot_name))

            # Stores the material index & slot name inside a dictionary to be referenced
            material_dict = dict(index=slot_index, name=str(slot_name))

            # Append the dictionary to an empty list so that we can iterate on each item separately
            material_information.append(material_dict)
    return material_information


# Assigns materials on the selected actors.
def assign_material():
    materials = get_material_instances()
    slot_info = get_material_slot_information()

    # Retrieves all the material instances
    material_asset_name = [m.asset_name for m in materials]
    material_path = [m for m in materials]

    # Retrieves the value information for each slot
    material_slot_values = [v.values() for v in slot_info]

    # Run a check to find a material in the library that matches the slot name
    for len in material_slot_values:
        material_index = len[0]
        print(material_index)
        material_name = len[1]
        if material_name in material_asset_name:
            static_mesh = get_meshes()
            print(static_mesh)
            found = "found " + str(material_name)
            print(found)
        else:
            print("no matches found")
            pass


assign_material()
