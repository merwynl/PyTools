import os
import tkinter as tk
from tkinter import filedialog
import shutil

# Initializes tKinter widget window
root = tk.Tk()
root.withdraw()

# Ask the user for a directory
file_path = filedialog.askdirectory()

# List of parent folders
folders = [
    "00_wip",
    "01_references",
    "02_scenes",
    "03_houdini",
    "04_marvelous",
    "05_gaea",
    "06_speedtree",
    "07_zbrush",
    "08_rizom",
    "09_meshes",
    "10_textures",
    "--FINALS--",
    "unreal",
]

# Path to parent folders
houdini_dir = os.path.join((file_path + "/" + folders[3]))
marvelous_dir = os.path.join((file_path + "/" + folders[4]))
gaea_dir = os.path.join((file_path + "/" + folders[5]))
speedtree_dir = os.path.join((file_path + "/" + folders[6]))
zbrush_dir = os.path.join((file_path + "/" + folders[7]))
rizom_dir = os.path.join((file_path + "/" + folders[8]))
meshes_dir = os.path.join((file_path + "/" + folders[9]))
textures_dir = os.path.join((file_path + "/" + folders[10]))
finals_dir = os.path.join((file_path + "/" + folders[11]))
unreal_dir = os.path.join((file_path + "/" + folders[12]))

# Sub-directories
finals_folders = ["360", "4k", "instagram", "marmoset", "substance"]
gaea_folders = ["out", "scene"]
houdini_folders = ["geo", "hda", "scripts", "tex"]
marvelous_folders = ["out", "scene"]
meshes_folders = ["baking", "blockout", "kit"]
rizom_folders = ["in", "out"]
speedtree_folders = ["out", "scene"]
texture_folders = [
    "bakes",
    "designer",
    "mixer",
    "painter",
    "psd",
    "output",
    "source",
    "working",
]
zbrush_folders = ["in", "out"]


def make_project_dir():

    # Create primary folders
    for f in folders:
        folder_path = os.path.join((file_path + "/" + f))
        try:
            os.mkdir(folder_path)
            print("Creating " + f + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Finals sub-directories
    for fin in finals_folders:
        finals_sub_dir = os.path.join((finals_dir + "/" + fin))
        try:
            os.mkdir(finals_sub_dir)
            print("Creating " + fin + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Gaea sub-directories
    for gaea in gaea_folders:
        gaea_sub_dir = os.path.join((gaea_dir + "/" + gaea))
        try:
            os.mkdir(gaea_sub_dir)
            print("Creating " + gaea + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Houdini sub-directories
    for hou in houdini_folders:
        houdini_sub_dir = os.path.join((houdini_dir + "/" + hou))
        try:
            os.mkdir(houdini_sub_dir)
            print("Creating " + hou + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Marvelous sub-directories
    for marvelous in marvelous_folders:
        marvelous_sub_dir = os.path.join((marvelous_dir + "/" + marvelous))
        try:
            os.mkdir(marvelous_sub_dir)
            print("Creating " + marvelous + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Meshes sub-directories
    for mesh in meshes_folders:
        meshes_sub_dir = os.path.join((meshes_dir + "/" + mesh))
        try:
            os.mkdir(meshes_sub_dir)
            print("Creating " + mesh + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Rizom sub-directories
    for rizom in rizom_folders:
        rizom_sub_dir = os.path.join((rizom_dir + "/" + rizom))
        try:
            os.mkdir(rizom_sub_dir)
            print("Creating " + rizom + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Speedtree sub-directories
    for speedtree in speedtree_folders:
        speedtree_sub_dir = os.path.join((speedtree_dir + "/" + speedtree))
        try:
            os.mkdir(speedtree_sub_dir)
            print("Creating " + speedtree + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Texture sub-directories
    for tex in texture_folders:
        textures_sub_dir = os.path.join((textures_dir + "/" + tex))
        try:
            os.mkdir(textures_sub_dir)
            print("Creating " + tex + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create Zbrush sub-directories
    for zbr in zbrush_folders:
        zbrush_sub_dir = os.path.join((zbrush_dir + "/" + zbr))
        try:
            os.mkdir(zbrush_sub_dir)
            print("Creating " + zbr + " folders...")
        except FileExistsError:
            print("Folder already exists!")


make_project_dir()
