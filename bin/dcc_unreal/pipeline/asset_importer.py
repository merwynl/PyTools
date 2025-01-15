import unreal


# Create an import task
import_task = unreal.AssetImportTask

# Set directories & names on import task


# Suppress UI
import_task.automated = True


# FBX Import UI
'''
Set the options on an FBX import dialog
'''
options = unreal.FBXImportUI()
