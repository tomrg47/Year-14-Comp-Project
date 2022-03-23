import Neural_Network
from Neural_Network import *
import tkinter as tk
from tkinter import *

print(photo_list)
print('high')
root = Tk()
root.geometry("600x600")
root.config(background='grey')

sort_label = tk.Label(root, text='Sorting...', font='Arial 30')
sort_label.place(x=245, y=50)

model_ans = Neural_Network.model.predict(photo_list, batch_size=None, verbose=0)

if model_ans == 1:
    print("hello")
if model_ans == 0:
    print("hi")
else:
    print("jeff")

root.mainloop()
