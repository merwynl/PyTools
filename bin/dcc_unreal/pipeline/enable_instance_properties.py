import unreal

'''
資産名とパスを照会するための一連の小さなスニペット
'''

DIR_PATH = '/Game/SE001_MidnightDiner/materials'

# 資産クラスタイプを印刷します。
def listAssets():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for m in assets:
        mi_class = str(m.asset_class)
        # Runs a check to see if an asset is of a particular class
        if mi_class == 'MaterialInstanceConstant':
                print m.asset_name
listAssets()