from tkinter import *
from PIL import Image, ImageTk
from chitra import modify

class Event:
    def __init__(self, canvas, orig_img, image_id, mod):
        self.canvas = canvas
        self.coordinate = []
        self.orig_img = orig_img
        print(type(self.orig_img))
        self.image_id = image_id
        self.mod = mod
        self.scale = 1.0
        self.imageid = None
        self.delta = 0.75
        self.canvas.bind("<Button-1>", self.capture_coordinate)
        self.canvas.bind("<MouseWheel>", self.zoom_function)

    def capture_coordinate(self,event):
        e_x, e_y = event.x, event.y
        x, y = self.mod.pixel_to_coordinate(e_x, e_y)
        self.coordinate.append((x, y))
        self.create_circle(x, y)
        return self.coordinate

    def create_circle(self, x, y):
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, outline='red')

    def zoom_function(self, event):
        if event.delta == -120:
            self.scale *= 1.1
            
        elif event.delta == 120:
            self.scale *= 0.9
            
        # Resize the image
        new_size = (int(self.orig_img.size[0]*self.scale), int(self.orig_img.size[1]*self.scale))
        resized_img = self.orig_img.resize(new_size, Image.BICUBIC)
        # Update the image on the canvas
        self.tk_img = ImageTk.PhotoImage(resized_img)
        self.canvas.itemconfig(self.image_id, image=self.tk_img)










