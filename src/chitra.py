import rasterio
import numpy as np

class Modify:
    def __init__(self, path):
        self.path = path
        self.array, self.transform = self.open_image()

    def open_image(self):
        with rasterio.open(self.path) as src:
            array = src.read(1)
            profile = src.profile
            transform = profile["transform"]
            image = (array / np.max(array) * 255).astype(np.uint8)
        return image, transform
    


    
            