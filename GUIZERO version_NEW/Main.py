import skimage.io
from guizero import *
from tkinter import filedialog
from Neural_network import *
from Neural_network import model
import numpy as np
from PIL import *
import cv2
from skimage import *

awidth = 400
aheight = 300

app = App(height=aheight, width=awidth)  # creates the file window
app.title = "Main Menu"  # Names the created window
opend_imgs = []
Rural_list = []
Urban_list = []
r_Save_list = []
test = ['', '']


def Save_screen(r_Save_list, Urban_list, Sorting_txt):
    Sorting_txt.hide()

    def rural():  # saving function for rural(landscape) images
        print("hi")
        save = filedialog.asksaveasfilename(defaultextension=".*",
                                            filetypes=(
                                                ("Jpeg file", "*.jpg"), ("Jfif File", "*.jfif"), ("All Files", "*.*")))
        x = 0
        print(save)
        if save:
            # arr = np.ndarray(r_Save_list)
            # print(arr)
            ext = save
            # print(ext)
            # print(ext[0])
            filetype = str(ext).split('.')[::-1]
            # print(filetype)
            combined = str(filetype[1]) + '.' + str(filetype[0])
            # print(combined)
            # save = open(save, 'w')
            # arr = np.ndarray(r_Save_list)
            # print(arr)
            # arr2 = np.array(test)

            # concat = np.concatenate([arr, arr2])
            # print(concat)
            # saveas = (str(combined, arr))
            image = r_Save_list[0]
            # resize_D = (image.shape[0]//10, image.shape[1]//10, image.shape[2])
            # resize = skimage.transform.resize(image =image, output_shape = resize_D)
            # resize = skimage.img_as_ubyte(resize)
            skimage.io.imsave(fname=str(combined), arr=image)

    def urban():  # The saving function for the Urban save button
        print("hello")
        saves = filedialog.asksaveasfilename(defaultextension=".*",
                                             filetypes=(
                                                 ("Jpeg file", "*.jpg"), ("Jfif File", "*.jfif"), ("All Files", "*.*")))
        # Above is the code to open the save as filedialog so the user can save the images where and
        # under what ever name they want without disrupting the original.

        if saves:  # if the user has typed in a name and selected a file extension this code runs
            exts = saves  # place holder variable to get the name of the file and the file extension
            filetype = str(exts).split('.')[::-1]  # splits the file type off of the user input file name
            combined2 = str(filetype[1]) + '.' + str(filetype[0])  # combines the file type back with the file name
            image2 = Urban_list[0]  # moves the data for the image need to a variable
            skimage.io.imsave(fname=str(combined2), arr=image2)  # creates the file using the file name and declared
            # type and writes the data to it.

    app.title = "Save Screen"
    app.update()
    Save_text = Text(app, text="Save Menu")
    Sort_text = Text(app, text="Sorting Complete")

    Landscape_save_txt = Text(app, text="Save Landscape Photos:")
    if len(r_Save_list) >= 1:  # checks if any photos have been sorted into the catagory
        l_Save_button = PushButton(app, text="Save Photos", command=rural)  # if there has displays save button
    else:
        l_lable = Text(app, text=' There are no Landscape Photos to save! ')  # if there isn't displays this text.

    Urban_save_txt = Text(app, text='Save Urban Photos:')
    if len(Urban_list) >= 1:

        u_Save_button = PushButton(app, text="Save Photos", command=urban)
    else:
        U_lable = Text(app, text=' There are no Urban Photos to save! ')


def Browse_cmd():  # browse button function.
    def Back_cmd():  # back button function
        title_text.show()
        Browse_Button.show()
        app.title = "Main Menu"
        Sort_ttext.hide()
        Sort_button.hide()
        Back_button.hide()

    def Sort_cmd():  # sort button function
        temp_List = []
        x = 0
        class_names = ["Landscape", "Urban"]

        while x <= len(files) - 1:
            Sort_ttext.hide()
            Sort_button.hide()
            Back_button.hide()
            Sorting_txt = Text(app, text='Sorting...')  # displays while the neural network sorts the images

            img = tf.keras.utils.load_img(files[x], target_size=(256, 256))  # 256,256 works # opens the images needed
            # in a keras compatible format

            img_array = tf.keras.utils.img_to_array(img)  # adds all the images to an array
            img_array = tf.expand_dims(img_array, 0)  # expands the dimensions of the array to an compatible size for
            # the neual network

            predictions = model.predict(img_array)
            print(predictions)
            score = tf.nn.softmax(predictions[0])
            print("This image most likely belongs to {} with a {:.2f} percent confidence".format(
                class_names[np.argmax(score)],
                100 * np.max(score)))

            if class_names[np.argmax(score)] == "Urban":  # takes the argmax value of score to decide if it urban
                current_img2 = skimage.io.imread(files[x])  # opens the current image in a compatible type for saving
                Urban_list.append(current_img2)

            if class_names[np.argmax(score)] == "Landscape":  # takes argmax value of score to decide if rural
                current_img = skimage.io.imread(files[x])

                # Rural_list.append(files[x])

                # for item in Rural_list:
                #   temp = item[::-1]

                #  ttemp = temp.split('/', 1)[0][::-1]

                r_Save_list.append(current_img)  # appends image to a list to be saved

                # print(Rural_list)

            x = x + 1

        Save_screen(r_Save_list, Urban_list, Sorting_txt)

    global files
    files = filedialog.askopenfilenames(filetypes=(
        ("Jpeg file", "*.jpg"), ("Jfif File", "*.jfif"), ("All Files", "*.*")))
    print(files)

    if len(files) >= 1:
        title_text.hide()
        Browse_Button.hide()
        Option_Button.hide()
        Exit_Button.hide()
        app.title = "Sort Menu"
        Sort_ttext = Text(app, text='Sort Menu')
        Sort_button = PushButton(app, text='Sort', command=Sort_cmd) #  runs the images though the NN to be sorted
        Option_Button.show()
        Back_button = PushButton(app, text='Back', command=Back_cmd)
        Exit_Button.show()

    else:
        pass


def options():
    win = Window(app, title='Options Menu', layout="auto", width=500)

    def change_bg_colour(x, y):  # function for changing background colour
        colour_bg = bg_waffle[x, y].color
        app.bg = colour_bg
        win.bg = colour_bg

    def change_txt_colour(x, y):  # function for changing text colour
        colour = txt_waffle[x, y].color
        app.text_color = colour
        win.text_color = colour

    def change_txt_size(slider_value):  # function for changing text size
        app.text_size = slider_value
        win.text_size = slider_value

    colours = ["red", "green", "blue", "pink", "orange", "black", "grey", "white", None]
    heading = Text(win, text='Text Colour     Text Size     Background Colour')
    txt_waffle = Waffle(win, height=3, width=3, align="left", command=change_txt_colour, pad=20)
    slider = Slider(win, start=10, end=80, command=change_txt_size, align='left')

    m = 0
    n = 0
    for v in range(0, 9):
        txt_waffle[m, n].color = colours[v]  # fills the waffle with the colours
        m = m + 1
        if m == 3:
            m = 0
            n = n + 1

    bg_waffle = Waffle(win, height=3, width=3, align="right", command=change_bg_colour, pad=20)
    x = 0
    y = 0
    for i in range(0, 9):
        bg_waffle[x, y].color = colours[i]  # fills the waffle with the colours
        x = x + 1
        if x == 3:
            x = 0
            y = y + 1

    test_text = Text(win, text='hello', align="top")

    close_button = PushButton(win, text='Close', command=win.destroy, align='bottom')   # when clicked the program returns to the main menu


title_text = Text(app, text='Image Recognition')  # Adds a Title within the window
Browse_Button = PushButton(app, text='Open Files', command=Browse_cmd)  # creates a Push button on the app window.
Exit_Button = PushButton(app, text='Exit', command=quit, align='bottom')  # quits the app on the button click event
Option_Button = PushButton(app, text='Options', command=options, align='bottom') # The button to open the options menu.

app.display()  # loops the window to keep the display showing
