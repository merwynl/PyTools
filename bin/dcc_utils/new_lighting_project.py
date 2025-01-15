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
    "03_meshes",
    "04_textures",
    "--FINALS--",
    "unreal",
]

# Path to parent folders
finals_dir = os.path.join((file_path + "/" + folders[0]))
textures_dir = os.path.join((file_path + "/" + folders[4]))

# Sub-directories
finals_folders = ["360", "4k", "artstation", "instagram"]
texture_folders = ["source", "working", "output"]


def make_project_dir():

    # Create primary folders
    for f in folders:
        folder_path = os.path.join((file_path + "/" + f))
        try:
            os.mkdir(folder_path)
            print("Creating " + f + " folders...")
        except FileExistsError:
            print("Folder already exists!")

    # Create finals sub-directories
    for fin in finals_folders:
        finals_sub_dir = os.path.join((finals_dir + "/" + fin))
        try:
            os.mkdir(finals_sub_dir)
            print("Creating " + fin + " folders...")
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


make_project_dir()