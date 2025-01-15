import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askdirectory()
folders = ['houdini', 'marmoset', 'maya', 'meshes', 'reference', 'textures', 'unreal']
houdini_folders = ['geo', 'hda', 'scripts', 'tex']
texture_folders = ['designer', 'painter', 'output', 'mixer']
marmoset_folders = ['wips', 'renders', 'scene']


def make_project_dir():
    houdini_dir = os.path.join((file_path + '/' + folders[0]))
    textures_dir = os.path.join((file_path + '/' + folders[5]))
    marmoset_dir = os.path.join((file_path + '/' + folders[1]))
    for f in folders:
        folder_path = os.path.join((file_path + '/' + f))
        try:
            os.mkdir(folder_path)
            print('Creating ' + f + ' folders...')
        except FileExistsError:
            print('Folder already exists!')
    for hou in houdini_folders:
        houdini_sub_dir = os.path.join((houdini_dir + '/' + hou))
        try:
            os.mkdir(houdini_sub_dir)
            print('Creating ' + hou + ' folders...')
        except FileExistsError:
            print('Folder already exists!')
    for tex in texture_folders:
        textures_sub_dir = os.path.join((textures_dir + '/' + tex))
        try:
            os.mkdir(textures_sub_dir)
            print('Creating ' + tex + ' folders...')
        except FileExistsError:
            print('Folder already exists!')
    for out in marmoset_folders:
        marmoset_sub_dir = os.path.join((marmoset_dir + '/' + out))
        try:
            os.mkdir(marmoset_sub_dir)
            print('Creating ' + out + ' folders...')
        except FileExistsError:
            print('Folder already exists!')


make_project_dir()
