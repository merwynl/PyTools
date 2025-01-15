import os
import tkinter as tk
from tkinter import filedialog

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
    "03_zbrush",
    "04_meshes",
    "05_textures",
    "--FINALS--",
]

# Path to parent folders
zbrush_dir = os.path.join((file_path + "/" + folders[3]))
meshes_dir = os.path.join((file_path + "/" + folders[4]))
textures_dir = os.path.join((file_path + "/" + folders[5]))
finals_dir = os.path.join((file_path + "/" + folders[6]))

# Sub-directories
finals_folders = ["360", "4k", "instagram", "marmoset", "substance"]
meshes_folders = ["baking", "blockout", "kit"]
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

    # Create Meshes sub-directories
    for mesh in meshes_folders:
        meshes_sub_dir = os.path.join((meshes_dir + "/" + mesh))
        try:
            os.mkdir(meshes_sub_dir)
            print("Creating " + mesh + " folders...")
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