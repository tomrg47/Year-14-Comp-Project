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
from guizero import *

win = App(title='Options Menu')
title = Text(win, text='Hello')


def change_txt_size(slider_value):
    title.size = slider_value
    return slider_value


slider = Slider(win, start=10, end=80, command=change_txt_size)

win.display()
