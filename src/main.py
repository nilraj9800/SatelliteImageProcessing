from tkinter import Tk
from event_handling import Event
from gui import MyGui
import os
from chitra import modify

master = Tk()
window = MyGui(master)

image_path = os.path.join("SatelliteImageProcessing","image", "braunchm.tif")

# Create an instance of the modify class
mod = modify(image_path)

# Get the image array from the instance
image_holder, _ = mod.open_image()

img = window.load_image(image_holder)


# Initialize Event here, and pass whatever canvas/frame you have.
circle_drawing = Event(window.canvas, img, window.imageid, mod)

master.mainloop()