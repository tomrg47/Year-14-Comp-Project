# imports the modules needed
import functools
import os
import subprocess
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from functools import partial


# sets up the new window
win2 = Tk()
win2.geometry("600x600")
win2.config(background="grey")

# set a list of all the file directories
photo_list: list = [file_name]
print(photo_list)


def sort(win2, photo_list):
    subprocess.run([sys.executable, '-c',neural_networks.py])
    #exec(open().read())
    win2.destroy()
    return photo_list

sort_button = Button(win2, text='Sort',
                     command=partial(sort, win2, photo_list))  # sets the button to execute the imported sort command
sort_button.place(x=300, y=300)  # places the button on the screen
win2.mainloop()
