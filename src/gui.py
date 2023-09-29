
import numpy as np
from tkinter import *
from PIL import Image, ImageTk


class MyGui:
    def __init__(self, master):
        self.master = master 
        master.title("Raster Analysis")
        master.configure(width=700, height=600)
        master.configure(bg="lightgray")
        
    def load_image(self, array):
        array = ((array - array.min()) / (array.max() - array.min()) * 255)
        array = array.astype("uint8")
        image = Image.fromarray(array, 'L')
        resized_image = image.resize((400,305), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas = Canvas(self.master, width=700, height =500)
        self.canvas.pack()
        self.canvas.place(anchor = "center", relx=0.5, rely=0.5)
        self.imageid = self.canvas.create_image(350,250, image = self.tk_image)

        return resized_image

        



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          