from tkinter import *
from PySide6 import QtCore, QtWidgets, QtGui
from PIL import Image, ImageTk
import geopandas as gpd
import pandas as pd
import rasterio

class Event:
    def __init__(self, transform):
        self.transform = transform 
        self.coordinate = []

    def capture_coordinate(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
        x_trans, y_trans = rasterio.transform.xy(self.transform, x, y)
        print(x_trans, y_trans)

    def points_to_dataframe(self, x, y):
        df = pd.DataFrame({"x": [x], "y": [y]})
        geo_data = gpd.GeoDataFrame(df, geometry= gpd.points_from_xy(df.x, df.y), 
                                crs = "EPSG: 25832")
        return geo_data

    def create_circle(self, x, y):
        points = self.points_to_dataframe(x, y)
        buffer_point = points.geometry.buffer(5)
        return buffer_point

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










