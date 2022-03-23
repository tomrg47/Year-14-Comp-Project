from guizero import *
from tkinter import filedialog


def Browse_cmd():
    files = filedialog.askopenfiles()
    return files


class options_menu():
    def __init__(self, fnt_size, fnt_colour, bg_colour, app):
        self.size = fnt_size
        self.colour = fnt_colour
        self.bg = bg_colour

    def font_size_cmd(self, slider_value):
        self.size = slider_value
        title_text.size = self.size

    def n_win(self):
        self.win = Window(app, title='Options Menu')
        self.title = Text(self.win, text='Options Menu', size=self.size, color=self.colour)
        self.slider = Slider(self.win, start=10, end=80, command=font_size_cmd)


app = App()  # creates the file window
app.title = "Main Menu"  # Names the created window

title_text = Text(app, text='Image Recognision')  # Adds a Title within the window
options = options_menu(10, 'black', 'grey', app)
Browse_Button = PushButton(app, text='Open Files', command=Browse_cmd)  # creates a Push button on the app window.
Option_Button = PushButton(app, text='Options', command=options.n_win)
app.display()  # loops the window to keep the display showing
