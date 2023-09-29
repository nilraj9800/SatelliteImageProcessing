import rasterio

class modify:
    def __init__(self, path):
        self.path = path
        self.array, self.transform = self.open_image()
        

    def open_image(self):
        with rasterio.open(self.path) as src:
            array = src.read(1) 
            profile = src.profile
            transform = profile["transform"]  
        return array, transform
    
    def pixel_to_coordinate(self, row, col):
        x, y = rasterio.transform.xy(self.transform, row, col)
        return x, y

    
            