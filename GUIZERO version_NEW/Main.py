from guizero import *
from tkinter import filedialog
#from Neural_network import *

app = App()  # creates the file window
app.title = "Main Menu"  # Names the created window


def Browse_cmd():
    def Back_cmd():
        title_text.show()
        Browse_Button.show()
        app.title = "Main Menu"
        Sort_ttext.hide()
        Sort_button.hide()
        Back_button.hide()

    def Sort_cmd():
                pass
    files = filedialog.askopenfiles()
    if len(files) >= 1:
        title_text.hide()
        Browse_Button.hide()
        Option_Button.hide()
        Exit_Button.hide()
        app.title = "Sort Menu"
        Sort_ttext = Text(app, text='Sort Menu')
        Sort_button = PushButton(app, text='Sort', command=Sort_cmd)
        Option_Button.show()
        Back_button = PushButton(app, text='Back', command=Back_cmd)
        Exit_Button.show()

    else:
        pass


def options():
    win = Window(app, title='Options Menu')

    def change_bg_colour(x, y):
        colour_bg = bg_waffle[x, y].color
        app.bg = colour_bg
        win.bg = colour_bg

    def change_txt_colour(x, y):
        colour = txt_waffle[x, y].color
        title_text.text_color = colour
        test_text.text_color = colour

    def change_txt_size(slider_value):
        title_text.size = slider_value
        test_text.size = slider_value
        return slider_value

    slider = Slider(win, start=10, end=80, command=change_txt_size)
    colours = ["red", "green", "blue", "pink", "orange", "black", "grey", "white", "yellow"]
    txt_waffle = Waffle(win, height=3, width=3, align="left", command=change_txt_colour)
    m = 0
    n = 0
    for v in range(0, 9):
        txt_waffle[m, n].color = colours[v]
        m = m + 1
        if m == 3:
            m = 0
            n = n + 1

    bg_waffle = Waffle(win, height=3, width=3, align="right", command=change_bg_colour)
    x = 0
    y = 0
    for i in range(0, 9):
        bg_waffle[x, y].color = colours[i]
        x = x + 1
        if x == 3:
            x = 0
            y = y + 1
    test_text = Text(win, text='hello')

    close_button = PushButton(win, text='Close', command=win.destroy)


title_text = Text(app, text='Image Recognition')  # Adds a Title within the window
# options = options_menu(10, 'black', 'grey', app)
Browse_Button = PushButton(app, text='Open Files', command=Browse_cmd)  # creates a Push button on the app window.
Option_Button = PushButton(app, text='Options', command=options)
Exit_Button = PushButton(app, text='Exit', command=quit)  # quits the app on the button click event

app.display()  # loops the window to keep the display showing
