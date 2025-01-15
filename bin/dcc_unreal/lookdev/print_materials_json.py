import unreal
import json

'''
Dumps a material list out to as json file
'''

DIR_PATH = '/Game/A02_Materials/Materials'
material_list = "H:/materials.json"
# Print out the names of assets based on their class type.
def getMaterialNameSimple():
        glblShaderList = []
        glblShaderDict = {}
        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
        for m in assets:
                material_class = str(m.asset_class)
                material_name = str(m.asset_name)
                # Runs a check to see if an asset is of a particular class
                if material_class == 'MaterialInstanceConstant' :
                        glblShaderList.append(str(m.asset_name))
                        path = str( m.get_full_name() )
                        pathSplit = path.split("/")
                        pathSplit.pop()
                        parent = pathSplit[-1]
                        if parent not in glblShaderDict:
                            glblShaderDict[ parent ] = [ str( m.asset_name ) ]
                        else:
                            glblShaderDict[ parent ].append( str( m.asset_name ) )
                        with open(material_list, "w") as json_file:
                            json.dump(glblShaderDict, json_file, indent=4)

getMaterialNameSimple()