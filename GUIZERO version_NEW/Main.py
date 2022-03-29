from guizero import *
from tkinter import filedialog
app = App()  # creates the file window
app.title = "Main Menu"  # Names the created window

def Browse_cmd():
    files = filedialog.askopenfiles()
    return files


# class options_menu():
#     def __init__(self, fnt_size, fnt_colour, bg_colour, app):
#         self.size = fnt_size
#         self.colour = fnt_colour
#         self.bg = bg_colour
#
#     def n_win(self):
#         def font_size_cmd():
#             self.size = slider_value
#             title_text.size = slider_value
#
#         self.win = Window(app, title='Options Menu')
#         self.title = Text(self.win, text='Options Menu', size=self.size, color=self.colour)
#         slider = Slider(self.win, start=10, end=80, command=font_size_cmd)

def options():
    win= Window(app, title='Options Menu')
    def change_txt_size(slider_value):
        title_text.size = slider_value
        return slider_value


    slider = Slider(win, start=10, end=80, command=change_txt_size)

# app = App()  # creates the file window
# app.title = "Main Menu"  # Names the created window

title_text = Text(app, text='Image Recognition')  # Adds a Title within the window
#options = options_menu(10, 'black', 'grey', app)
Browse_Button = PushButton(app, text='Open Files', command=Browse_cmd)  # creates a Push button on the app window.
Option_Button = PushButton(app, text='Options', command=options)
Exit_Button = PushButton(app, text='Exit', command=quit)  # quits the app on the button click event

app.display()  # loops the window to keep the display showing
