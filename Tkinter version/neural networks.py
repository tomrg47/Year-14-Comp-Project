import tkinter as tk
# noinspection PyCompatibility
from tkinter import filedialog
from editBar import EditBar
from imageViewer import ImageViewer


filename = filedialog.askopenfiles(mode = 'rb')


image = []
#''.join(format(ord(x),'b')for x in image)
image.append(filename)


filesave= filedialog.asksaveasfile(mode = 'w', defaultextension = '.JPG',filetypes=[("Jpeg File",".JPG"),("Zipped File",".zip")])
cv2.inwrite(filesave,image)
#filesave.write(str(image))

