import os
import hou

asset_dir = hou.ui.selectFile(title='Choose asset import directory', file_type=hou.fileType.Directory)
asset_dir_expanded = hou.expandString(asset_dir)

asset_files = os.listdir(asset_dir_expanded)

file_nodes = []
importer = hou.node('/obj').createNode('geo', 'asset_loader')

for asset in asset_files:
    asset_file_node = importer.createNode('file', asset)
    asset_file_node.parm('file').set(asset_dir + asset)
    asset_file_node.parm('missingframe').set(1)

    file_nodes.append(asset_file_node)

merge_assets = importer.createNode('merge', 'asset_merged')

for node in file_nodes:
    merge_assets.setNextInput(node)

importer.layoutChildren()

merge_assets.setDisplayFlag(True)
merge_assets.setRenderFlag(True)