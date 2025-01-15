import unreal

'''
資産名とパスを照会するための一連の小さなスニペット
'''

DIR_PATH = '/Game/'

# AssetData構造体全体を印刷します。
def printAssetData():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset

# 資産名だけを印刷します。
def printAssetName():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.asset_name

# 資産クラスタイプを印刷します。
def printAssetClass():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.asset_class
    
# DIR_PATHにuassetsのパッケージパスを印刷します。
def printPackagePath():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.package_path

# DIR_PATHにuassetsのパッケージ名を印刷します。
def printPackageName():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.package_name

# DIR_PATHに各uassetのオブジェクトパスを印刷します。
def printObjectPath():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for asset in assets:
        print asset.object_path

# 特定のクラスタイプに基づいて資産名を印刷する.
def listAssets():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(DIR_PATH, recursive=True)
    for m in assets:
        material_class = str(m.asset_class)
        # Runs a check to see if an asset is of a particular class
        if material_class == 'MaterialInstanceConstant':
                print m.asset_name
