from guizero import *
from tkinter import filedialog
from Neural_network import *
from Neural_network import model
import numpy as np

awidth = 300
aheight = 300

app = App(height=aheight, width=awidth)  # creates the file window
app.title = "Main Menu"  # Names the created window

Rural_list = []
Urban_list = []


def Save_screen(Rural_list, Urban_list, Sorting_txt):
    Sorting_txt.hide()

    def rural():
        print("hi")
        save = filedialog.asksaveasfile(initialfile=Rural_list)

    def urban():
        print("hello")
        save = filedialog.asksaveasfile(initialfile=Urban_list)

    app.title = "Save Screen"
    app.update()
    Save_text = Text(app, text="Save Menu")
    Sort_text = Text(app, text="Sorting Complete")
    Landscape_save_txt = Text(app, text="Save Landscape Photos:")
    l_Save_button = PushButton(app, text="Save Photos", command=rural)

    Urban_save_txt = Text(app, text='Save Urban Photos:')
    u_Save_button = PushButton(app, text="Save Photos", command=urban)


def Browse_cmd():
    def Back_cmd():
        title_text.show()
        Browse_Button.show()
        app.title = "Main Menu"
        Sort_ttext.hide()
        Sort_button.hide()
        Back_button.hide()

    def Sort_cmd():

        x = 0
        class_names = ["Landscape", "Urban"]

        while x <= len(files) - 1:
            Sort_ttext.hide()
            Sort_button.hide()
            Back_button.hide()
            Sorting_txt = Text(app, text='Sorting...')

            img = tf.keras.utils.load_img(files[x], target_size=(256, 256))  # 256,256 works
            img_array = tf.keras.utils.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)
            predictions = model.predict(img_array)
            print(predictions)
            score = tf.nn.softmax(predictions[0])
            print("This image most likely belongs to {} with a {:.2f} percent confidence".format(
                class_names[np.argmax(score)],
                100 * np.max(score)))

            if class_names[np.argmax(score)] == "Urban":
                Urban_list.append(img)
                print(Urban_list)

            if class_names[np.argmax(score)] == "Landscape":
                Rural_list.append(img)
                print(Rural_list)

            x = x + 1

        Save_screen(Rural_list, Urban_list, Sorting_txt)

    files = filedialog.askopenfilenames()
    print(files)

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
    win = Window(app, title='Options Menu', layout="auto", width=500)

    def change_bg_colour(x, y):
        colour_bg = bg_waffle[x, y].color
        app.bg = colour_bg
        win.bg = colour_bg

    def change_txt_colour(x, y):
        colour = txt_waffle[x, y].color
        title_text.text_color = colour
        test_text.text_color = colour

    def change_txt_size(slider_value):
        app.text_size = slider_value
        win.text_size = slider_value

    colours = ["red", "green", "blue", "pink", "orange", "black", "grey", "white", None]
    txt_waffle = Waffle(win, height=3, width=3, align="left", command=change_txt_colour, pad=20)
    slider = Slider(win, start=10, end=80, command=change_txt_size, align='left')

    m = 0
    n = 0
    for v in range(0, 9):
        txt_waffle[m, n].color = colours[v]
        m = m + 1
        if m == 3:
            m = 0
            n = n + 1

    bg_waffle = Waffle(win, height=3, width=3, align="right", command=change_bg_colour, pad=20)
    x = 0
    y = 0
    for i in range(0, 9):
        bg_waffle[x, y].color = colours[i]
        x = x + 1
        if x == 3:
            x = 0
            y = y + 1
    global s_txt
    test_text = Text(win, text='hello', align="top")

    close_button = PushButton(win, text='Close', command=win.destroy, align='bottom')


title_text = Text(app, text='Image Recognition')  # Adds a Title within the window
Browse_Button = PushButton(app, text='Open Files', command=Browse_cmd)  # creates a Push button on the app window.
Exit_Button = PushButton(app, text='Exit', command=quit, align='bottom')  # quits the app on the button click event
Option_Button = PushButton(app, text='Options', command=options, align='bottom')

app.display()  # loops the window to keep the display showing
