import unreal

project_id = "207"
project_name = "HeightfieldTest"

prefix = ["S", "H1704"]
sub_directories = ["materials", "textures", "meshes", "blueprints"]

directory = unreal.EditorAssetLibrary()
directory_path = "/Game/" + prefix[0] + project_id + "_" + project_name

level = unreal.EditorLevelLibrary()
level_name = prefix[1] +"_"+ project_name
level_asset = directory_path + "/" + level_name

def asset_hierarchy():
    does_exist = True
    if directory.does_directory_exist == does_exist:
        level.new_level(level_asset)
        print(str(directory_path) + ' already exists')
    else:
        directory.make_directory(directory_path)
        for i in sub_directories:
            directory.make_directory(directory_path + "/" + i)
        level.new_level(level_asset)
        print(str(directory_path) + ' created')

asset_hierarchy()