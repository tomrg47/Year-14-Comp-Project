# imports all the necessary modules
import os
import subprocess
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from typing import Union, List, Any, TextIO

global filename

# creates and sets value for the global variables for accessibility settings
global default_font
global bg_colour
global text_colour
bg_colour = 'grey'
colours = ['Grey', 'Black', 'White', 'Blue', 'Red', 'Pink', 'Green']
text_colour = colours[1]
# text_colour = 'black'

# sets up a tl window to interact with
win = Tk()
win.title('File Explorer')
win.geometry("1500x720")
default_font = font.Font(family='Helvetica', size="15")
# colour_font = font.Font(default_font, default_font.cget("font"),forground= )

win.config(background=bg_colour)


# starts a func to allow photos to be uploaded
def file_browse():
    file_name = filedialog.askopenfiles(filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.tiff', '.tif', '.RAW',
                                                                    '.dir'])])  # opens a temp window for file to be

    # loaded
    if len(file_name) is None:
        return None
    elif len(file_name) >= 1:

        win.destroy()  # destroys the current window to open the main window
        exec(open('main.py').read())  # opens the new window
        file_name = file_name
        return file_name


# class Options(win):
#   def __init__(self):
#      self.x = 300
#     self.y = 300
#
#   def menu(self, win):
#      c = Canvas(win, width = 300, height= 300)
#     c.create_rectangle(200, 50, 550, 550,fill='grey')

def destroy():
    Canvas.destroy(c)


def options():
    global c

    def font_c_chooser(e):
        text_colour = text_c_listbox.get(text_c_listbox.curselection())
        default_font.tag_configure("coloured", font=colour_font, fg=text_c_listbox.get(text_c_listbox.curselection()))
        return text_colour

    def font_s_chooser(e):
        default_font.config(size=text_s_listbox.get(text_s_listbox.curselection()))

    def bg_c_chooser():
        pass

    c = Canvas(win, width=1000, height=700)
    c.create_rectangle(1, 1, 1000, 700, outline='black', fill=bg_colour)
    c.pack()
    option = tk.Label(c, text='Options Menu', fg=text_colour, font=default_font, bg=bg_colour)
    option.place(x=420, y=20)
    button_exit = Button(c, text='Close', command=destroy)
    button_exit.place(x=250, y=450)
    text_c_label = tk.Label(c, text='Text Colour:', fg=text_colour, font=default_font, bg=bg_colour)
    text_s_label = tk.Label(c, text='Text Size:', fg=text_colour, font=default_font, bg=bg_colour)
    bg_c_label = tk.Label(c, text='Background:', fg=text_colour, font=default_font, bg=bg_colour)
    text_c_label.place(x=140, y=150)
    text_s_label.place(x=400, y=150)
    bg_c_label.place(x=650, y=150)
    text_c_listbox = Listbox(c, selectmode=SINGLE, width=20)
    text_c_listbox.place(x=145, y=200)
    text_s_listbox = Listbox(c, selectmode=SINGLE, width=20)
    text_s_listbox.place(x=395, y=200)
    bg_c_listbox = Listbox(c, selectmode=SINGLE, width=20)
    bg_c_listbox.place(x=645, y=200)

    font_sizes = [8, 10, 12, 14, 16, 18, 20, 24, 26, 28, 36]
    for size in font_sizes:
        text_s_listbox.insert('end', f'    {size}')

    colours = ['Grey', 'Black', 'White', 'Blue', 'Red', 'Pink', 'Green']
    for colour in colours:
        text_c_listbox.insert('end', f'    {colour}')
        bg_c_listbox.insert('end', f'    {colour}')

    text_c_listbox.bind('<ButtonRelease-1>', font_c_chooser)
    text_s_listbox.bind('<ButtonRelease-1>', font_s_chooser)
    bg_c_listbox.bind('<ButtonRelease-1>', bg_c_chooser)


button_browse = Button(win, text='Browse', command=file_browse)  # allows the button to activate the file_browse func
button_stop = Button(win, text='EXIT', command=exit)  # allows the exit button to halt the program
button_option = Button(win, text='Options', command=options)
title = tk.Label(win, text='Image Sorter', fg='blue', font='Arial 30 bold',
                 bg='grey').pack()  # allows the text to be placed on the screen

# places the buttons
button_browse.place(x=300, y=300)
button_stop.place(x=300, y=400)
button_option.place(x=300, y=500)

win.mainloop()  # runs the window and loops it to keep it activated as long as needed.
