import unreal

project_id = "000"
project_name = "MaterialsTest" 

prefix = ["ENV", "Master"]
sub_directories = ["materials", "textures", "meshes", "blueprints"]

directory = unreal.EditorAssetLibrary()
directory_path = "/Game/" + prefix[0] + project_id + "_" + project_name

level = unreal.EditorLevelLibrary()
level_name = prefix[1] + "_" + project_name
level_asset = directory_path + "/" + level_name


def make_directory():
    does_exist = True
    if directory.does_directory_exist == does_exist:
        print(str(directory_path) + ' already exists')
    else:
        directory.make_directory(directory_path)        
        for i in sub_directories:
            directory.make_directory(directory_path + "/" + i)
        print(str(directory_path) + ' created')


make_directory()
